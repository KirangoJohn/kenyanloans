from django.urls import path

from . import views

app_name = 'loans'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('loans/loantypes', views.loantypes, name='loantypes'),
    path('loans/faqs', views.faqs, name='faqs'),
    path('loans/quickloans', views.quickloans, name='quickloans'),
]