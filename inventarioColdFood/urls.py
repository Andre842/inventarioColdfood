from django.contrib import admin
from django.urls import path
from inventario import views

app_name = 'inventario'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('entrada/', views.crear_entrada, name='crear_entrada'),
    path('salida/', views.crear_salida, name='crear_salida'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('crear-proveedor/', views.crear_proveedor, name='crear_proveedor'),
    path('crear-cliente/', views.crear_cliente, name='crear_cliente'),
    path('entradas/', views.listar_entradas, name='lista_entradas'),
    path('salidas/', views.listar_salidas, name='lista_salidas'),
    path('productos/', views.productos, name='productos'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('clientes/', views.clientes, name='clientes'),
    path('stock/', views.stock, name='stock'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('proveedores/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedor/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
]
