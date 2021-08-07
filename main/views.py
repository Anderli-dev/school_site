from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import (Document,
                     Employees,
                     Vacancy,
                     Finance,
                     FinanceFiles,
                     BlogPsychologa,
                     News,
                     Bullying,
                     DistanceStudy,
                     )


def index(request):
    return render(request, 'index.html')


class JoinUsView(ListView):
    model = Document
    template_name = 'join.html'


class DocumentPageView(DetailView):
    model = Document
    template_name = 'document-page.html'


class EmployeesView(ListView):
    model = Employees
    template_name = 'nash-kolektiv.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeesView, self).get_context_data(**kwargs)
        context['Employees'] = Employees.objects.all()
        context['Vacancy'] = Vacancy.objects.all()
        context['first-line'] = Employees.objects.all()[0:5]
        return context


class FinanceView(ListView):

    model = Finance
    template_name = 'finance.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super(FinanceView, self).get_context_data(**kwargs)
        context['FinanceFiles'] = FinanceFiles.objects.all()
        return context


class FinanceDetailView(DetailView):
    # тут возможно логика неправильная
    model = Finance
    template_name = 'finance-details.html'

    def get_context_data(self, **kwargs):
        context = super(FinanceDetailView, self).get_context_data(**kwargs)
        context['FinanceFiles'] = FinanceFiles.objects.all()
        context['Finance'] = Finance.objects.order_by('-id')
        return context


class BlogPsychologaView(ListView):

    model = BlogPsychologa
    template_name = 'blog-psychologa.html'
    ordering = ['-id']


class BlogPsychologaDetailView(DetailView):

    model = BlogPsychologa
    template_name = 'post-psychologa.html'


class NewsView(ListView):

    model = News
    template_name = 'news.html'
    ordering = ['-id']


class NewsDetailView(DetailView):

    model = News
    template_name = 'news-detail.html'


class BullyingView(DetailView):

    model = Bullying
    template_name = 'bullying-page.html'


class DistanceStudyView(DetailView):

    model = DistanceStudy
    template_name = 'distance-study.html'
