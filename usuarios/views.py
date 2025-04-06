from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.

class LoginUsuario(LoginView):
    """
    Vista para manejar el inicio de sesión de usuarios.
    
    Attributes:
        template_name (str): Plantilla HTML para el formulario de login
        success_url (str): URL a la que se redirige después del login exitoso
    """
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        """
        Retorna la URL a la cual el usuario debe ser redirigido después de
        un inicio de sesión exitoso.
        
        Returns:
            str: URL de redirección
        """
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
            
        # Si el usuario es administrador, redirigir a la tabla
        if self.request.user.is_staff:
            return reverse_lazy('personal:personal_list')
            
        return reverse_lazy('personal:listado')
