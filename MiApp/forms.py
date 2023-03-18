from django import forms
from MiApp.models import Compra, Proveedor, Recurso

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = '__all__'