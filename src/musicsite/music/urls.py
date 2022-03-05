from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:music_id>/', views.detail, name='detail'),
    path('register/', views.register_music, name='register_music'),
]