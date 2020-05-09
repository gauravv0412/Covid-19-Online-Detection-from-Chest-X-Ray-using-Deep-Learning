from django.urls import path
from main import views
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [
    path('', views.index, name = 'index'),
]

if settings.DEBUG: 
    print('settings.debug is also true')
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 