from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('subcriber', views.subscriber_list, name='subscriber_list'),
    path('subscriber/<int:pk>/', views.subscriber_detail, name='subscriber_detail'),
    path('subscriber/create/', views.subscriber_create, name='subscriber_create'),
    path('subscriber/<int:pk>/update/', views.subscriber_update, name='subscriber_update'),
    path('subscriber/<int:pk>/delete/', views.subscriber_delete, name='subscriber_delete'),
  
]
