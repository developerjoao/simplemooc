from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from views import register
#from views import

urlpatterns =[
    url(r'^cadastrar/$', register,  name='register'),
    url(r'^entrar/$', auth_views.login, {'template_name' : 'login.html'}, name='login'),
]
