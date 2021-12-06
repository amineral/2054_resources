from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main/<int:dp>/', views.main_page, name="main"),
    path('main/<int:dp>/comps/', views.comps, name='dp_comps'),
    path('main/<int:dp>/boards/', views.boards, name='dp_boards'),
    path('api/comps', views.comp_list, name='api_comp_list'),
    path('api/comps/<int:pk>', views.comp_details, name='api_comp_details'),
    path('api/boards', views.board_list, name='api_board_list'),
    path('api/boards/<int:pk>', views.board_details, name='api_board_details')
]