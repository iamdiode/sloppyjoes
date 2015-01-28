from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'content.views.index', name='sloppy_home'),
    url(r'menu/(?P<slug>[\w-]+)/$', 'content.views.menu', name='sloppy_menu'),
    url(r'menu/$', 'content.views.menu', name='sloppy_menus'),
    url(r'franchise/$', 'content.views.franchise', name='sloppy_franchise'),
    url(r'feedback/$', 'content.views.feedback', name='sloppy_feedback'),
)


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
