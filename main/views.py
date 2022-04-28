from itertools import chain
from datetime import datetime

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
                     InfoPage,
                     )


def index(request):
    employees = Employees.objects.filter(type=2)[:3]
    if employees.count() <= 3:
        employees = list(chain(employees, Employees.objects.filter(type=1)[:4-employees.count()]))

    return render(request, 'index.html', context={"employees": employees})


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
        context['Count'] = Employees.objects.filter(type=1).count()
        return context


class FinanceView(ListView):
    model = Finance
    template_name = 'finance.html'

    def get_context_data(self, **kwargs):
        context = super(FinanceView, self).get_context_data(**kwargs)
        context['FinanceZvit'] = FinanceFiles.objects.get(Finance=Finance.objects.get(year=datetime.now().year))
        return context


class FinanceDetailView(DetailView):
    model = Finance
    template_name = 'finance-details.html'

    def get_context_data(self, **kwargs):
        context = super(FinanceDetailView, self).get_context_data(**kwargs)
        context['FinanceZvit'] = FinanceFiles.objects.get(Finance=self.object)
        context['FinancesYear'] = Finance.objects.only("year")
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
    ordering = ['-id']


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
