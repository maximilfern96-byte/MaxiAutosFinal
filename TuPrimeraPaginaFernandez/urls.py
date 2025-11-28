from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views   # 👈 Import necesario para "proximamente"

urlpatterns = [
    path('admin/', admin.site.urls),

    # App principal
    path('', include('blog.urls')),

    # Usuarios
    path('usuarios/', include('usuarios.urls')),

    # 👉 Ruta para los botones del footer (Opción 2: "Próximamente")
    path('proximamente/', blog_views.proximamente, name='proximamente'),
]

# Archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
