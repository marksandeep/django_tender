# log/urls.py
from django.conf.urls import url
from . import views
from django.contrib.auth import views as login_view
from login.forms import LoginForm
# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^login/$', views.login, {'template_name': 'login.html'})
    url(r'^login/$', login_view.login,),
    url(r'^logout/$', login_view.logout, {'next_page': '/login'})
]