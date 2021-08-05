from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('desajono/', include('desajono.urls')),
    path('admin/', admin.site.urls),
]