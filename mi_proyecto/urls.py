"""mi_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiApp.views import index, base, compras, proveedores, recursos, agregar_compra, agregar_proveedor, agregar_recurso, buscar_proveedor

urlpatterns = [
    path('', index, name="index"),
    path('compras', compras, name="compras"),
    path('proveedores', proveedores, name="proveedores"),
    path('recursos', recursos, name="recursos"),
    path('compras/agregar', agregar_compra, name="agregar_compras"),
    path('proveedores/agregar', agregar_proveedor, name="agregar_proveedor"),
    path('recursos/agregar', agregar_recurso, name="agregar_recurso"),
    path('proveedores/buscar', buscar_proveedor, name="buscar_proveedor"),
    path('admin/', admin.site.urls),
]
