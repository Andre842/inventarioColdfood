from django.shortcuts import render, redirect, get_object_or_404
from .models import Entrada, Producto, Proveedor, Cliente
from .forms import FormularioEntrada
from .models import Salida, Producto, Proveedor, Cliente
from .forms import FormularioSalida
from .forms import FormularioProducto
from .forms import FormularioProveedor
from .forms import FormularioCliente
from django.urls import reverse
from django.db.models import Sum
from django.utils.timezone import now
from django.db.models import Count, F
from django.db.models import Prefetch
from django.db.models.functions import Coalesce

def crear_producto(request):
    if request.method == 'POST':
        form = FormularioProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = FormularioProducto()
    return render(request, 'producto/crear_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect(reverse('productos'))  
    else:
        form = FormularioProducto(instance=producto)
    return render(request, 'producto/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        producto.delete()
        return redirect(reverse('productos'))  
    return render(request, 'producto/eliminar_producto.html', {'producto': producto})

def productos(request):
    productos_list = Producto.objects.all()  
    return render(request, 'producto/productos.html', {'productos': productos_list})

def crear_proveedor(request):
    if request.method == 'POST':
        form = FormularioProveedor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = FormularioProveedor()
    return render(request, 'proveedor/crear_proveedor.html', {'form': form})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = FormularioProveedor(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect(reverse('proveedores'))  
    else:
        form = FormularioProveedor(instance=proveedor)
    return render(request, 'proveedor/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect(reverse('proveedores')) 
    return render(request, 'proveedor/eliminar_proveedor.html', {'proveedor': proveedor})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    
    return render(request, 'proveedor/detalle_proveedor.html', {
        'proveedor': proveedor
    })

def proveedores(request):
    proveedores_list = Proveedor.objects.all() 
    return render(request, 'proveedor/proveedores.html', {'proveedores': proveedores_list})

def crear_cliente(request):
    if request.method == 'POST':
        form = FormularioCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = FormularioCliente()
    return render(request, 'cliente/crear_cliente.html', {'form': form})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = FormularioCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect(reverse('clientes')) 
    else:
        form = FormularioCliente(instance=cliente)
    return render(request, 'cliente/editar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect(reverse('clientes')) 
    return render(request, 'cliente/eliminar_cliente.html', {'cliente': cliente})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    return render(request, 'cliente/detalle_cliente.html', {
        'cliente': cliente
    })

def clientes(request):
    clientes_list = Cliente.objects.all()
    return render(request, 'cliente/clientes.html', {'clientes': clientes_list})

def crear_entrada(request):
    if request.method == 'POST':
        form = FormularioEntrada(request.POST)
        if form.is_valid():
            entrada = form.save()
            # Actualizar el stock del producto
            producto = entrada.producto
            producto.stock += entrada.cantidad
            producto.save()
            return redirect('lista_entradas')
    else:
        form = FormularioEntrada()
    return render(request, 'entradas_salidas/crear_entrada.html', {'form': form})

def crear_salida(request):
    if request.method == 'POST':
        form = FormularioSalida(request.POST)
        if form.is_valid():
            salida = form.save(commit=False)
            producto = salida.producto
            if producto.stock >= salida.cantidad:
                producto.stock -= salida.cantidad
                producto.save()
                salida.save()
                return redirect('lista_salidas')
            else:
                form.add_error('cantidad', 'No hay suficiente stock para esta salida')
        else:
            print(form.errors)  # Esto mostrará los errores de validación en la consola
    else:
        form = FormularioSalida()
    return render(request, 'entradas_salidas/crear_salida.html', {'form': form})


def listar_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'entradas_salidas/lista_entradas.html', {'entradas': entradas})

def listar_salidas(request):
    salidas = Salida.objects.all()
    return render(request, 'entradas_salidas/lista_salidas.html', {'salidas': salidas})


def stock(request):
    productos_list = Producto.objects.all()  # Trae todos los productos
    return render(request, 'stock.html', {'productos': productos_list})

def index(request):
    productos = Producto.objects.all()    
    total_productos_en_stock = sum(producto.stock for producto in productos)
    productos_bajo_stock = productos.filter(stock__lt=100)
    entradas = Entrada.objects.all().order_by('-fecha')[:5]
    salidas = Salida.objects.all().order_by('-fecha')[:5]
    proveedores_destacados = Proveedor.objects.prefetch_related(
        Prefetch('producto_set', queryset=Producto.objects.all())
    )[:5]
    
    # Obtener los clientes con los productos más comprados
    clientes_destacados = Cliente.objects.all()

    # Para cada cliente, obtener el producto más comprado
    # Para cada cliente, obtener el producto más comprado
    for cliente in clientes_destacados:
    # Obtener los productos comprados por el cliente, ordenados por cantidad total comprada
        productos_comprados = cliente.salida_set.values('producto__nombre')\
            .annotate(total_comprado=Sum('cantidad'))\
            .order_by('-total_comprado')
        
        print(f"Cliente: {cliente.nombre}")
        print(f"Productos comprados: {productos_comprados}")
    
        if productos_comprados:
            cliente.producto_mas_comprado = productos_comprados[0]  # Producto más comprado
        else:
            cliente.producto_mas_comprado = None

    return render(request, 'index.html', {
        'total_productos_en_stock': total_productos_en_stock,
        'entradas': entradas,
        'salidas': salidas,
        'productos': productos,
        'productos_bajo_stock': productos_bajo_stock,
        'proveedores_destacados': proveedores_destacados,
        'clientes_destacados': clientes_destacados,
        'productos_comprados': productos_comprados,
    })
