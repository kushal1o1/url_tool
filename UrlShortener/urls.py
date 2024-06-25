from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_short_url', views.createShortUrl, name='create'),
    path('<str:pk>', views.go, name='go')
]