from django.contrib import admin
from .models import Categoria, Vehiculo, FotoVehiculo, Favorito


# ============================================================
#   INLINE PARA SUBIR VARIAS FOTOS DESDE ADMIN
# ============================================================
class FotoVehiculoInline(admin.TabularInline):
    model = FotoVehiculo
    extra = 1          # Cuántos campos vacíos se muestran
    max_num = 10       # Máximo de fotos permitidas
    fields = ('imagen',)  # Campo visible
    readonly_fields = ()  # Si querés bloquear campos ponelos acá


# ============================================================
#   ADMIN DE CATEGORÍAS
# ============================================================
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'slug')


# ============================================================
#   ADMIN DE VEHÍCULOS (con galería Pro)
# ============================================================
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'marca', 'anio', 'tipo', 'categoria')
    list_filter = ('categoria', 'tipo', 'anio')
    search_fields = ('titulo', 'marca')
    inlines = [FotoVehiculoInline]   # ⭐ ACTIVA SUBIDA DE VARIAS FOTOS


# ============================================================
#   ADMIN DE FAVORITOS
# ============================================================
@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'vehiculo', 'fecha')
    list_filter = ('usuario', 'fecha')

