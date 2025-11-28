from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required
from .models import Vehiculo, Categoria, Favorito
from .forms import VehiculoForm


# -------------------------------------------------------
# 🔒 Mixin para permitir SOLO al staff (admin)
# -------------------------------------------------------
class SoloStaffMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied("No tenés permisos para realizar esta acción.")
        return super().dispatch(request, *args, **kwargs)


# -------------------------------------------------------
# 🏠 INICIO
# -------------------------------------------------------
class InicioView(TemplateView):
    template_name = 'inicio.html'


# -------------------------------------------------------
# 🚗 LISTA DE VEHÍCULOS
# -------------------------------------------------------
class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'vehiculos/lista_vehiculos.html'
    context_object_name = 'vehiculos'
    paginate_by = 8


# -------------------------------------------------------
# 🔍 BUSCADOR
# -------------------------------------------------------
class VehiculoBuscarView(View):
    def get(self, request):
        query = request.GET.get("q", "").strip()

        if query == "":
            return render(
                request,
                "vehiculos/lista_vehiculos.html",
                {
                    "vehiculos": [],
                    "query": "",
                    "no_results": False,
                    "mostrar_sin_cargar": False,
                }
            )

        vehiculos = Vehiculo.objects.filter(titulo__icontains=query)
        no_results = vehiculos.count() == 0

        return render(
            request,
            "vehiculos/lista_vehiculos.html",
            {
                "vehiculos": vehiculos,
                "query": query,
                "no_results": no_results,
                "mostrar_sin_cargar": False,
            }
        )


# -------------------------------------------------------
# 📄 DETALLE DEL VEHÍCULO
# -------------------------------------------------------
class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'vehiculos/detalle_vehiculo.html'
    context_object_name = 'vehiculo'


# -------------------------------------------------------
# ✏️ CRUD (solo admin)
# -------------------------------------------------------
class VehiculoCreateView(LoginRequiredMixin, SoloStaffMixin, CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculos/vehiculo_form.html'
    success_url = reverse_lazy('lista_vehiculos')


class VehiculoUpdateView(LoginRequiredMixin, SoloStaffMixin, UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculos/vehiculo_form.html'
    success_url = reverse_lazy('lista_vehiculos')


class VehiculoDeleteView(LoginRequiredMixin, SoloStaffMixin, DeleteView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('lista_vehiculos')


# -------------------------------------------------------
# 🏷️ FILTRAR POR CATEGORÍA
# -------------------------------------------------------
def vehiculos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)

    vehiculos = Vehiculo.objects.filter(categoria=categoria)

    query = request.GET.get("q", "").strip()
    no_results = False

    if query:
        vehiculos = vehiculos.filter(titulo__icontains=query)
        if not vehiculos.exists():
            no_results = True

    context = {
        "categoria": categoria,
        "vehiculos": vehiculos,
        "query": query,
        "no_results": no_results,
    }

    return render(request, "vehiculos/lista_vehiculos.html", context)


# -------------------------------------------------------
# ❓ QUIÉNES SOMOS
# -------------------------------------------------------
def quienes_somos(request):
    return render(request, 'quienes_somos.html')


# -------------------------------------------------------
# ❤️ FAVORITOS
# -------------------------------------------------------
@login_required
def agregar_favorito(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    Favorito.objects.get_or_create(usuario=request.user, vehiculo=vehiculo)

    messages.success(request, f"{vehiculo.titulo} fue agregado a tus favoritos.")
    return redirect("detalle_vehiculo", pk=pk)


@login_required
def ver_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, "vehiculos/favoritos.html", {"favoritos": favoritos})


@login_required
def quitar_favorito(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    Favorito.objects.filter(usuario=request.user, vehiculo=vehiculo).delete()

    messages.success(request, f"{vehiculo.titulo} fue quitado de tus favoritos.")
    return redirect("favoritos")


# -------------------------------------------------------
# ✨ PÁGINA "PRÓXIMAMENTE"
# -------------------------------------------------------
def proximamente(request):
    return render(request, "proximamente.html")
