from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning.urls')),
    path('admin/defender/', include('defender.urls')),
    path('accounts/', include('allauth.urls')),
    # path('^inbox/notifications/', include(notifications.urls, namespace='notifications'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
