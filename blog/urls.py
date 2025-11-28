from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),

    # Vehículos
    path('vehiculos/', views.VehiculoListView.as_view(), name='lista_vehiculos'),
    path('vehiculos/buscar/', views.VehiculoBuscarView.as_view(), name='buscar_vehiculos'),
    path('vehiculos/categoria/<slug:slug>/', views.vehiculos_por_categoria, name='vehiculos_por_categoria'),
    path('vehiculos/<int:pk>/', views.VehiculoDetailView.as_view(), name='detalle_vehiculo'),
    path('vehiculos/crear/', views.VehiculoCreateView.as_view(), name='crear_vehiculo'),
    path('vehiculos/<int:pk>/editar/', views.VehiculoUpdateView.as_view(), name='editar_vehiculo'),
    path('vehiculos/<int:pk>/eliminar/', views.VehiculoDeleteView.as_view(), name='eliminar_vehiculo'),

    # Pagina quienes somos
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),

    # Favoritos
    path("favoritos/", views.ver_favoritos, name="favoritos"),
    path("favorito/<int:pk>/agregar/", views.agregar_favorito, name="agregar_favorito"),
    path("favorito/<int:pk>/quitar/", views.quitar_favorito, name="quitar_favorito"),
]
