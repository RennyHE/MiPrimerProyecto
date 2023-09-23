from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais, Departamento, Municipio
from .forms import PaisForm, DepartamentoForm, MunicipioForm
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import PaisSerializer


class PaisListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Pais
    template_name = 'pais/lista_paises.html'
    context_object_name = 'paises'
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.view_pais'


class DepartamentoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Departamento
    template_name = 'departamento/lista_departamentos.html'
    context_object_name = 'departamentos'
    login_url = reverse_lazy('login')
    permission_required = 'catalogos_view_departamento'


class PaisCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/agregar_pais.html'
    success_url = reverse_lazy('lista_paises')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_pais'


class DepartamentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/agregar_departamento.html'
    success_url = reverse_lazy('lista_departamentos')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_departamento'

class DepartamentoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Departamento  # Define el modelo Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/modificar_departamento.html'
    success_url = reverse_lazy('lista_departamentos')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.change_departamento'
class DepartamentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Departamento  # Define el modelo Departamento
    template_name = 'departamento/eliminar_departamento.html'
    success_url = reverse_lazy('lista_departamentos')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.delete_departamento'


class PaisUpdateView(LoginRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/modificar_pais.html'
    success_url = reverse_lazy('lista_paises')
    login_url = reverse_lazy('login')


class PaisDeleteView(LoginRequiredMixin, DeleteView):
    model = Pais
    template_name = 'pais/eliminar_pais.html'
    success_url = reverse_lazy('lista_paises')
    login_url = reverse_lazy('login')

# viewset para pais


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class MunicipioListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Municipio
    template_name = 'municipio/lista_municipios.html'
    context_object_name = 'municipios'
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.view_municipio'

class MunicipioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/agregar_municipio.html'
    success_url = reverse_lazy('lista_municipios')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_municipio'

class MunicipioUpdateView(LoginRequiredMixin, UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/modificar_municipio.html'
    success_url = reverse_lazy('lista_municipios')
    login_url = reverse_lazy('login')

class MunicipioDeleteView(LoginRequiredMixin, DeleteView):
    model = Municipio
    template_name = 'municipio/eliminar_municipio.html'
    success_url = reverse_lazy('lista_municipios')
    login_url = reverse_lazy('login')
