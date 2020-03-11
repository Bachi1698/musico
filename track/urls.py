from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('blog', views.blog, name='blog'),
     path('contact', views.contact, name='contact'),
     path('elements', views.elements, name='elements'),
     path('main', views.main, name='main'),
     path('single_blog', views.single_blog, name='single-blog'),
     path('track', views.track, name='track'),
     path('about', views.about, name='about'),
]