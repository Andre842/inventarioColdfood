from django import forms
from .models import Entrada
from .models import Salida
from .models import Producto
from .models import Proveedor
from .models import Cliente
from django.utils import timezone

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'stock', 'proveedor'] 
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),  
        }


class FormularioProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class FormularioEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['producto', 'cantidad', 'proveedor', 'placa', 'fecha']

    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    cantidad = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    placa = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput(attrs={'class': 'form-control'}))

class FormularioSalida(forms.ModelForm):
    class Meta:
        model = Salida
        fields = ['producto', 'cantidad', 'cliente', 'placa', 'fecha']

    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    cantidad = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    placa = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateTimeField(initial=timezone.now, widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
