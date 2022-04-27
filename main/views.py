from itertools import chain

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
    # TODO what going on
    model = Finance
    template_name = 'finance.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super(FinanceView, self).get_context_data(**kwargs)
        context['FinanceFiles'] = FinanceFiles.objects.all()
        return context


class FinanceDetailView(DetailView):
    # тут возможно логика неправильная
    # TODO look what going on
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


class BullyingView(ListView):
    model = Bullying
    template_name = 'bullying.html'
    ordering = ['-id']


class BullyingDetailView(DetailView):

    model = Bullying
    template_name = 'bullying-detail.html'


class InfoPageView(DetailView):

    model = InfoPage
    template_name = 'info-page.html'
