from django.db import models
from django.contrib.auth.models import User


# -------------------------
#       CATEGORÍA
# -------------------------
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


# -------------------------
#        VEHÍCULO
# -------------------------
class Vehiculo(models.Model):
    titulo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    tipo = models.CharField(max_length=100, help_text='Ej: Auto, Moto, SUV, etc.')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='vehiculos')
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='vehiculos/', null=True, blank=True)

    # ⭐ NUEVO CAMPO PRECIO ⭐
    precio = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Ejemplo: 1250000.00"
    )

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f"{self.titulo} - {self.marca}"


# -------------------------
#   GALERÍA DE FOTOS (PRO)
# -------------------------
class FotoVehiculo(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE,
        related_name="fotos"
    )
    imagen = models.ImageField(upload_to="vehiculos/fotos/")

    def __str__(self):
        return f"Foto de {self.vehiculo.titulo}"


# -------------------------
#        FAVORITOS
# -------------------------
class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'vehiculo')

    def __str__(self):
        return f"{self.usuario.username} → {self.vehiculo.titulo}"
