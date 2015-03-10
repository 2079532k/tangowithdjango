from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
import settings


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/rango/'


urlpatterns = patterns('',
                       url(r'^$', 'rango.views.index', name="index"),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^rango/', include('rango.urls')),
                       url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                       (r'^accounts/', include('registration.backends.simple.urls')),
)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static', (r'^media/(?P<path>.*)', 'serve',
                                                    {'document_root': settings.MEDIA_ROOT}), )