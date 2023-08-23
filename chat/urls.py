from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("checkview", views.checkview, name="checkview"),
    path('<str:room_name>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room_id>/', views.getMessages, name='getMessages')
]