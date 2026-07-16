from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # <-- Esto activa la conexión real con Google
    path('', TemplateView.as_view(template_name='index.html'), name='home'), # <-- Esto quita el error Not Found
]
