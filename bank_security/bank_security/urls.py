# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     # Honeypot URLs (fake admin)
#     path('admin/', include('myapp.honeypot.urls')),  # Fake admin dashboard
    
#     # Real admin (protected)
#     path('secret-admin/', admin.site.urls),  # Actual admin
    
#     # Main app
#     path('', include('myapp.urls')),  # Regular app URLs
# ]

#before latest
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', include('myapp.honeypot.urls')),  # Fake admin
#     path('secret-admin/', admin.site.urls),  # Real admin
#     path('', include('myapp.urls')),  # Main app
# ]

# bank_security/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),  # Main app
    path('secret-admin/', admin.site.urls),  # Real admin
    path('admin/', include('admin_honeypot.urls')),  # Fake admin (honeypot)
]