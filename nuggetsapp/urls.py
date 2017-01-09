from django.conf.urls import url, include
from . import views, api_controllers, token

urlpatterns = [
    url(r'^api/v0/user/(?P<user_id>[0-9]+)/nuggets/$', api_controllers.nuggets_op_by_user, name='nuggets_op_by_user'),
    url(r'^api/v0/user/(?P<user_id>[0-9]+)/nuggets/(?P<nugget_id>[0-9]+)$', api_controllers.nuggets_op_by_user_and_nugget, name='nuggets_op_by_user_and_nugget'),
    url(r'^api/v0/nuggets/$', api_controllers.nuggets_op_by_url, name='nuggets_op_by_url'),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', token.obtain_auth_token),

    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^add-nugget$', views.add_nugget, name='add-nugget'),
    url(r'^add-nugget-post$', views.add_nugget_post),
    url(r'^my-nuggets$', views.my_nuggets, name='my-nuggets'),
]
