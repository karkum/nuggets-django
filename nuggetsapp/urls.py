from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^add-nugget$', views.add_nugget, name='add-nugget'),
    url(r'^add-nugget-post$', views.add_nugget_post),
    url(r'^my-nuggets$', views.my_nuggets, name='my-nuggets'),
    # APIs
    url(r'^api/get-my-nuggets$', views.api_get_my_nuggets, name='api-get-my-nuggets'),
    url(r'^api/add-nugget$', views.api_add_nugget, name='api-add-nugget'),
    # React entry-point
    url(r'^react$', views.react, name='react')
]
