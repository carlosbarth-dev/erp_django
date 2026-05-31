from django import forms
from django.contrib import admin

from .models import Cliente

class ClienteAdminForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'documento': 'CPF/CNPJ',
        }
        widgets = {
            'documento': forms.TextInput(attrs={
                'placeholder': 'Somente numeros',
            }),
        }


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = ('nome', 'tipo_pessoa', 'documento', 'telefone', 'ativo')
    list_filter = ('tipo_pessoa', 'ativo')
    search_fields = ('nome', 'documento', 'email')
