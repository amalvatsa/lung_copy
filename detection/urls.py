from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Route for the homepage
    path('lung-cancer-form/', views.lung_cancer_form, name='lung_cancer_form'),  # Route for the form upload
    path('result/<str:result>/', views.result_page, name='result'),  # Route for the result page
]
