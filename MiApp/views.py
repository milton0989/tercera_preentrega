from django.shortcuts import render

# Create your views here.

def base (request):
    return render(request, "MiApp/base.html")

def index (request):
    return render(request, "MiApp/index.html")

def compras (request):
    return render(request, "MiApp/compras.html")

def proveedores (request):
    return render(request, "MiApp/proveedores.html")

def recursos (request):
    return render(request, "MiApp/recursos.html")
    
