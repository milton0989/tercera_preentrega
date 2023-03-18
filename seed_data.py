from MiApp.models import Compra, Proveedor, Recurso


Compra(fecha_compra="15/03/2023",
       proveedor = "Ferreteria",
       importe_compra = "10.23").save()
Compra(fecha_compra="23/03/2023",
       proveedor = "Corralon",
       importe_compra = "3000.00").save()

Proveedor(nombre = "Ferreteria",
          domicilio = "Rawson",
          contacto ="2804525333" ).save()
Proveedor(nombre = "Corralon",
          domicilio = "Trelew",
          contacto ="281346846154" ).save()

Recurso(nombre_recurso = "cemento",
        unidad ="bolsa", 
        agrupamiento = "Aglomerantes").save()
Recurso(nombre_recurso = "Acero 6mm",
        unidad ="barra",
        agrupamiento = "Aceros").save()

