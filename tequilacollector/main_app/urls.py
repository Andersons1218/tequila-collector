from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tequila/', views.tequila_index, name='index'),
    path('tequila/<int:tequila_id>/', views.tequila_detail, name='detail'),
]