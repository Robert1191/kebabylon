from django.conf.urls import url
from MainWebApp import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^about/', views.about, name='about'),
    # url(r'^contact/', views.contact, name='contact'),
    # url(r'^menu/', views.menu, name='menu'),
]