from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='personal:home'), name='logout'),
    # ... otras rutas de autenticación ...
] 