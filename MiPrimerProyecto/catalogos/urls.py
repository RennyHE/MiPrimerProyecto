from django.urls import path
from .views import *

urlpatterns = [
    path('paises/', PaisListView.as_view(), name='lista_paises'),
    path('paises/nuevo/', PaisCreateView.as_view(), name='agregar_pais'),
    path('paises/<int:pk>/', PaisUpdateView.as_view(), name='modificar_pais'),
    path('paises/<int:pk>/eliminar/', PaisDeleteView.as_view(), name='eliminar_pais'),
    path('departamentos/', DepartamentoListView.as_view(), name='lista_departamentos'),
    path('departamentos/nuevo/', DepartamentoCreateView.as_view(), name='agregar_departamento'),  # Agrega la URL para crear Departamento
    path('departamentos/<int:pk>/', DepartamentoUpdateView.as_view(), name='modificar_departamento'),  # Agrega la URL para actualizar Departamento
    path('departamentos/<int:pk>/eliminar/', DepartamentoDeleteView.as_view(), name='eliminar_departamento'),  # Agrega la URL para eliminar Departamento
    path('municipios/', MunicipioListView.as_view(), name='lista_municipios'),  # Agrega la URL para listar Municipios
    path('municipios/nuevo/', MunicipioCreateView.as_view(), name='agregar_municipio'),  # Agrega la URL para crear Municipio
    path('municipios/<int:pk>/', MunicipioUpdateView.as_view(), name='modificar_municipio'),  # Agrega la URL para actualizar Municipio
    path('municipios/<int:pk>/eliminar/', MunicipioDeleteView.as_view(), name='eliminar_municipio'),  # Agrega la URL para eliminar Municipio
]


