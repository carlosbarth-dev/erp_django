from django import forms
from django.core.exceptions import ValidationError
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

    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        tipo_pessoa = self.cleaned_data.get('tipo_pessoa')

        if not documento:
            return documento

        if not documento.isdigit():
            raise ValidationError('Informe somente numeros.')

        if tipo_pessoa == Cliente.TipoPessoa.FISICA and len(documento) != 11:
            raise ValidationError('CPF deve ter 11 numeros.')

        if tipo_pessoa == Cliente.TipoPessoa.JURIDICA and len(documento) != 14:
            raise ValidationError('CNPJ deve ter 14 numeros.')

        return documento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = ('nome', 'tipo_pessoa', 'documento', 'telefone', 'ativo')
    list_filter = ('tipo_pessoa', 'ativo')
    search_fields = ('nome', 'documento', 'email')
