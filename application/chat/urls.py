from django.urls import path, include
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('logout', views.logout, name='chat'),
    # path('', include('application.urls', namespace='application')),
]