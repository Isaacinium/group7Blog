from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single-post/', views.single_post, name='single-post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.category, name='category'),

]
