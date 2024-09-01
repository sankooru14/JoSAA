# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('menu_page/', views.menu_page, name='menu_page'),
    path('choice_predictor/', views.choice_predictor, name='choice_predictor'),
    path('institute_wise_trends/', views.institute_wise_trends,
         name='institute_wise_trends'),
    path('branch_wise_trends/', views.branch_wise_trends,
         name='branch_wise_trends'),
    path('choice_predictor/choice_predictor_display',
         views.choice_predictor_display, name='choice_predictor_display'),
    path('branch_wise_trends/branch_wise_trends_display/',
         views.branch_wise_trends_display, name='branch_wise_trends_display'),
    path('institute_wise_trends/institute_wise_trends_display/',
         views.institute_wise_trends_display, name='institute_wise_trends_display')
]
