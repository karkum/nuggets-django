from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^api/v1/nuggets/(?P<user_id>[0-9]+)/$', views.nuggets_for_user, name='nuggets_for_user'),
    url(r'^api-auth/', include('rest_framework.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^add-nugget$', views.add_nugget, name='add-nugget'),
    url(r'^add-nugget-post$', views.add_nugget_post),
    url(r'^my-nuggets$', views.my_nuggets, name='my-nuggets'),
]
