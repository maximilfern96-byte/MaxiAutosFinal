
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class LoginUsuarioView(FormView):
    template_name = 'usuarios/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


def logout_usuario(request):
    logout(request)
    return redirect('inicio')


class RegistroUsuarioView(FormView):
    template_name = 'usuarios/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil.html')
