from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^projects/', include('projects.urls')),
    url(r'^files/', include('files.urls')),
    url(r'^authentication/', include('authentication.urls')),
    url(r'^contentbox/', include('contentbox.urls')),
    url(r'^tags/', include('tags.urls')),
    url(r'^login/', views.login, name='login'),
    url(r'^filter/(?P<tag>.*)/', views.index, name='filter'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
