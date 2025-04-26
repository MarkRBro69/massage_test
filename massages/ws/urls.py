from django.urls import path

from ws.views.views import index, register, login, comments, new_comment

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('comments/', comments, name='comments'),
    path('new_comment/', new_comment, name='new_comment'),
]
