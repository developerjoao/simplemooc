from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from views import register, dashboard


urlpatterns =[
    url(r'^$', dashboard,  name='dashboard'),
    url(r'^cadastrar/$', register,  name='register'),
    url(r'^entrar/$', auth_views.login, {'template_name' : 'login.html'}, name='login'),
    url(r'^sair/$', auth_views.logout, {'next_page' : 'core:home'}, name='logout'),
]
