from django.contrib import admin
from .models import Flan

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'destacado', 'descuento_inscrito' )
    prepopulated_fields = {'slug': ('nombre',)}
    list_filter = ('destacado', 'descuento_inscrito', 'precio')
    search_fields = ('nombre', 'descripcion')