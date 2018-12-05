from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('radmin/', admin.site.urls),
    path('apirest/', include('webapimd.urls')),
    path(r'', include('core.urls')),
    path(r'', include('redweb.urls')),
    path('', include('pwa.urls')),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
