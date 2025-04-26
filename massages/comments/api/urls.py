from django.urls import path, include

urlpatterns = [
    path('v1/', include('comments.api.v1.urls')),
]
