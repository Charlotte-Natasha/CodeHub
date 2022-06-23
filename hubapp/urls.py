from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('resources/', views.resources, name='resources'),
    path('community/', views.community, name='community'),
    path('process/', views.process, name='process'),
    path('post/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('details/', views.details, name='details'),
]