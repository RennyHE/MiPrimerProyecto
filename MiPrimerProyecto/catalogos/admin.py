from django.contrib import admin

# Register your models here.
from .models import Pais, Departamento, Municipio

class PaisAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo']
    list_filter = ['codigo']
    search_fields = ['nombre', 'codigo']

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais', 'active']
    list_filter = ['pais__nombre', 'active']
    search_fields = ['nombre', 'pais__nombre']

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo', 'departamento', 'active']
    list_filter = ['departamento__nombre', 'active']
    search_fields = ['nombre', 'codigo', 'departamento__nombre']

admin.site.register(Pais, PaisAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)