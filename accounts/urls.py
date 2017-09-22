from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from views import register, dashboard, edit, edit_password


urlpatterns =[
    url(r'^$', dashboard,  name='dashboard'),
    url(r'^cadastrar/$', register,  name='register'),
    url(r'^editar/$', edit , name='edit'),
    url(r'^editar-senha/$', edit_password , name='edit_password'),
    url(r'^entrar/$', auth_views.login, {'template_name' : 'login.html'}, name='login'),
    url(r'^sair/$', auth_views.logout, {'next_page' : 'core:home'}, name='logout'),
]
