from django.urls import path
from main import views
from main.views import (DocumentPageView,
                        EmployeesView,
                        FinanceView,
                        FinanceDetailView,
                        BlogPsychologaView,
                        BlogPsychologaDetailView,
                        NewsView,
                        NewsDetailView,
                        BullyingView,
                        JoinUsView,
                        DistanceStudyView,
                        )

urlpatterns = [
    path('', views.index, name='home'),
    path('join', JoinUsView.as_view(), name='join'),
    path('news', NewsView.as_view(), name='news'),
    path('news/<slug:slug>', NewsDetailView.as_view(), name='news-detail'),
    path('nash-kolektiv', EmployeesView.as_view(), name='nash-kolektiv'),
    path('finance', FinanceView.as_view(), name='finance'),
    path('finance/<slug:slug>', FinanceDetailView.as_view(), name='finance-details'),
    path('document/<slug:slug>', DocumentPageView.as_view(), name='document-page'),
    path('distance-study/<slug:slug>', DistanceStudyView.as_view(), name='distance-study'),
    path('blog-psychologa', BlogPsychologaView.as_view(), name='blog-psychologa'),
    path('blog-psychologa/<slug:slug>', BlogPsychologaDetailView.as_view(), name='post-psychologa'),
    path('protidiya-bulingu/<slug:slug>', BullyingView.as_view(), name='bullying')
]
