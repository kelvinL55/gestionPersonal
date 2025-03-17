from django.urls import path
from . import views

urlpatterns = [
    path('', views.personal_list, name='personal_list'),
    path('nuevo/', views.personal_create, name='personal_create'),
    path('editar/<int:pk>/', views.personal_update, name='personal_update'),
    path('eliminar/<int:pk>/', views.personal_delete, name='personal_delete'),
    path('import-excel/', views.import_excel, name='import_excel'),
]