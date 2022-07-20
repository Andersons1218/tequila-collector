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
    path('tequila/<int:tequila_id>/add_taste/', views.add_taste, name='add_taste'),
    path('mix/', views.MixList.as_view(), name='mix_list'),
    path('mix/<int:pk>/', views.MixDetail.as_view(), name='mix_detail'),
    path('mix/create/', views.MixCreate.as_view(), name='mix_create'),
    path('mix/<int:pk>/update/', views.MixUpdate.as_view(), name='mix_update'),
    path('mix/<int:pk>/delete/', views.MixDelete.as_view(), name='mix_delete'),
    path('tequila/<int:tequila_id>/assoc_mix/<int:mix_id>/', views.assoc_mix, name='assoc_mix'),
]