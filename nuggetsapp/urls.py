from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^add-nugget$', views.add_nugget, name='add-nugget'),
    url(r'^add-nugget-post$', views.add_nugget_post),
    url(r'^my-nuggets$', views.my_nuggets, name='my-nuggets'),
    url(r'^react$', views.react, name='react'),
]
