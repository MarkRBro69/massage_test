from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


api_urls = [
    path('', include('users.api.urls')),
    path('', include('comments.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('', include('ws.urls')),
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
