from django.contrib import admin
from django.urls import path,include
from .routers import router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'apirest/', include('webapimd.urls')),
    path(r'', include('core.urls')),
    path(r'', include('redweb.urls')),
    path('', include('pwa.urls')),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
