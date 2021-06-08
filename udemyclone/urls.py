from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from udemyclone import settings

admin.site.site_header = "EduFlix Admin"
admin.site.site_title = "EduFlix Admin Portal"
admin.site.index_title = "Welcome to EduFlix Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('', include('accounts.urls')),
    path('', include('udemy.urls')),
    path('', include('courses.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
