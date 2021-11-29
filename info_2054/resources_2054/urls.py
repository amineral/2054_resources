from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main/<int:dp>/', views.main_page, name="main"),
    path('main/<int:dp>/comps/', views.comps, name='dp_comps'),
    path('main/<int:dp>/boards/', views.boards, name='dp_boards'),
    path('proceed_filter/', views.proceed_filter, name="filter")
]