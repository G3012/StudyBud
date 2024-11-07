from django.contrib import admin
from django.urls import path, include #we import 'include' to include base.urls 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')), #It just directs all the routings of our core project to base.urls
    path('api/',include('base.api.urls')),
]
