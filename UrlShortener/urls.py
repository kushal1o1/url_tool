from django.urls import path ,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('create_short_url', views.createShortUrl, name='create'),
    path('<str:pk>', views.go, name='go'),
    
    
]
urlpatterns += [
    re_path(r'^.*$',views.notFound,name='notFound')
]
