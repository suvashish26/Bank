from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    
    path('admin/', include('admin_honeypot.urls')), #admin page honeypot
    path('secret/', admin.site.urls), #actual admin page
    path('', include('myapp.urls')),
]