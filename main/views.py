import os
from datetime import datetime
from itertools import chain

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from preschool_educational_institution import settings
from .forms import TextArea
from .models import (Document,
                     DocumentFiles,
                     Employees,
                     Vacancy,
                     Finance,
                     FinanceFiles,
                     BlogPsychologa,
                     News,
                     Bullying,
                     InfoPage, 
                     EnterSchool,
                     DistanceLessons,
                     )


def index(request):
    employees = Employees.objects.filter(type=2)[:3]
    if employees.count() <= 3:
        employees = list(chain(employees, Employees.objects.filter(type=1)[:4-employees.count()]))

    return render(request, 'index.html', context={"employees": employees})


class JoinUsView(View):
    def get(self, request):
        if EnterSchool.objects.filter(pk=1):
            return render(request, 'join.html', context={"data": EnterSchool.objects.get(pk=1)})
        else:
            return render(request, 'join.html')


class DocumentPageView(DetailView):
    model = Document
    template_name = 'document-page.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentPageView, self).get_context_data(**kwargs)
        context['document_files'] = DocumentFiles.objects.all()
        return context


class EmployeesView(ListView):
    model = Employees
    template_name = 'nash-kolektiv.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeesView, self).get_context_data(**kwargs)
        context['Employees'] = Employees.objects.all()
        context['Vacancy'] = Vacancy.objects.all()
        context['Count'] = Employees.objects.filter(type=1).count()
        return context


class FinanceView(ListView):
    model = Finance
    template_name = 'finance.html'
    ordering = ['-year']

    def get_context_data(self, **kwargs):
        context = super(FinanceView, self).get_context_data(**kwargs)
        try:
            context['FinanceZvit'] = FinanceFiles.objects.filter(Finance=Finance.objects.order_by('year').last())
        except Finance.DoesNotExist:
            context['FinanceZvit'] = False
        return context


class FinanceDetailView(DetailView):
    model = Finance
    template_name = 'finance-details.html'

    def get_context_data(self, **kwargs):
        context = super(FinanceDetailView, self).get_context_data(**kwargs)
        context['FinanceZvit'] = FinanceFiles.objects.filter(Finance=self.object)
        context['FinancesYear'] = Finance.objects.only("year").order_by("-year")
        return context


class BlogPsychologaView(ListView):
    paginate_by = 10
    model = BlogPsychologa
    template_name = 'blog-psychologa.html'
    ordering = ['-id']


class BlogPsychologaDetailView(DetailView):
    model = BlogPsychologa
    template_name = 'post-psychologa.html'


class NewsView(ListView):
    paginate_by = 10
    model = News
    template_name = 'news.html'
    ordering = ['-post_date']


class NewsDetailView(DetailView):
    model = News
    template_name = 'news-detail.html'


class BullyingView(ListView):
    paginate_by = 10
    model = Bullying
    template_name = 'bullying.html'
    ordering = ['-id']


class BullyingDetailView(DetailView):
    model = Bullying
    template_name = 'bullying-detail.html'


class InfoPageView(DetailView):
    model = InfoPage
    template_name = 'info-page.html'


class EnterPageView(View):
    template_name = 'admin/join-us-page.html'
    model = EnterSchool

    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(EnterPageView, self).dispatch(*args, **kwargs)

    def get(self, request):
        form = TextArea()
        if EnterSchool.objects.filter(pk=1):
            document = EnterSchool.objects.get(pk=1).document
            return render(request, self.template_name, {"form": form, "document": document})
        else:
            return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = TextArea(request.POST, request.FILES)
        if form.is_valid():
            data = form.data
            # -- something wierd O_O --
            # this try except catch situation
            # when object more than one
            try:
                # this code below do if not exist
                if "document" in request.FILES:
                    EnterSchool.objects.create(content=data["content"], document=request.FILES["document"])
                    with open(os.path.join(settings.MEDIA_ROOT, "files"), 'rb') as fh:
                        print(os.path.join(settings.MEDIA_ROOT, "files"))
                        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(os.path.join(settings.MEDIA_ROOT, "/files"))
                        return response
                else:
                    print("else")
                    EnterSchool.objects.create(content=data["content"])
            except ValidationError:
                # this code if object exist
                EnterSchool.objects.filter(pk=1).update(content=data["content"])
                if request.FILES:
                    EnterSchool.objects.filter(pk=1).update(document=request.FILES["document"])
                    with open(os.path.join(settings.MEDIA_ROOT, 'files', str(request.FILES["document"])), 'wb+') as destination:
                        for chunk in request.FILES['document'].chunks():
                            destination.write(chunk)
            return redirect("admin:index")
        else:
            print(form.errors)
        return render(request, self.template_name, {"form": form})

    def delete(self, request):
        page = EnterSchool.objects.get(pk=1)
        page.document = None
        page.save()
        return redirect("admin:index")


class DistanceLessonsView(ListView):
    model = DistanceLessons
    template_name = "distance-lessons.html"
