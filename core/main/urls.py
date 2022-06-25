from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('about/', views.AboutListView.as_view(), name='about')
]