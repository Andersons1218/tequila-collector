from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tequila/', views.tequila_index, name='index'),
    path('tequila/<int:tequila_id>/', views.tequila_detail, name='detail'),
    path('tequila/create/', views.TequilaCreate.as_view(), name='tequila_create'),
    path('tequila/<int:pk>/update/', views.TequilaUpdate.as_view(), name='tequila_update'),
    path('tequila/<int:pk>/delete/', views.TequilaDelete.as_view(), name='tequila_delete'),
]