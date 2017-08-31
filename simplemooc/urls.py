from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^', include( 'core.urls', namespace = 'core' )),
    url(r'^cursos/', include( 'courses.urls', namespace = 'courses' )),
    url(r'^conta/', include( 'accounts.urls', namespace = 'accounts' )),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
