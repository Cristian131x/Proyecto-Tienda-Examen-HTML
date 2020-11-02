from django.contrib import messages
from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required






def index(request):
    print("Estamos en la vista")
    context={}
    return render(request,'productos/index.html',context)

def listar(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/listar.html',context)
def administrar(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/administrar.html',context)
def Snack(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/Snack.html',context)

def Cabritas(request):
    print("Estamos en la vista listar")
    data = {
        'productos': Producto.objects.filter(tipo='Bebida')
    }
    return render(request,'productos/Cabritas.html',data)

def listar_productos(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/listar_productos.html',context)


def Bebidas(request):
    print("Estamos en la vista Bebidas")
    data = {
        'productos' :Producto.objects.filter(tipo='Bebida')
    }
    return render(request,'productos/Bebidas.html' , data)

def mostrar_productos(request):
    print("Estamos en la vista mostrar productos")
    lista = Producto.objects.all()
    #lista = Producto.objects.filter(activo=1, genero= 'femenino')
    context={'listado':lista}
    return render(request,'productos/listar_productos.html',context)

def boton_buscar(request):
    print("Estamos en la vista boton buscar")
    context={}
    return render(request,'productos/boton_buscar.html',context)

def buscar_por_id(request):
    print("hola  estoy en buscar_por_id...")
    if request.method == 'POST':
       mi_nu = request.POST['numero']

       if mi_nu != "":
           try:
               producto = Producto()
               producto= Producto.objects.get(numero=mi_nu)
               if producto is not None:
                   print("Producto=", producto)
                   context={'producto':producto}
                   return render(request, 'productos/mostrar_datos.html', context)
               else:
                   return render(request, 'productos/error/error_202.html',{})
           except producto.DoesNotExist:
               return render(request, 'productos/error/error_202.html', {})
       else:
           return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def agregar(request):
    print("Estamos en la vista agregar")
    context = {}
    return render(request, 'productos/formulario_agregar.html', context)

def eliminar(request):
    print("Estamos en la vista eliminar")
    context={}
    return render(request,'productos/boton_eliminar.html',context)

def eliminar_por_id(request):
    print("Hola estoy en eliminar_por_rut")
    if request.method == 'POST':
       mi_numero = request.POST['numero']

       if mi_numero != "":
           try:
               producto = Producto()
               producto= Producto.objects.get(numero = mi_numero)
               if producto is not None:
                   print("Producto=", producto)
                   producto.delete()
                   context={}
                   return render(request, 'productos/mensaje_producto_eliminado.html', context)
               else:
                   return render(request, 'productos/error/error_202.html',{})
           except producto.DoesNotExist:
               return render(request, 'productos/error/error_202.html', {})
       else:
           return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def editar(request):
    print("Ok estamos en la vista editar")
    context={}
    return render(request,'productos/boton_editar.html',context)

def buscar_para_editar(request):

    print("hola  estoy en buscar_para_editar...")
    if request.method == 'POST':
        mi_numero = request.POST['numero']

        if mi_numero != "":
            try:
                producto = Producto()
                producto = Producto.objects.get(numero=mi_numero)
                if producto is not None:
                    print("Producto=", producto)
                    context = {'producto': producto}
                    return render(request, 'productos/formulario_editar.html', context)
                else:
                    return render(request, 'productos/error/error_202.html', {})
            except producto.DoesNotExist:
                return render(request, 'productos/error/error_202.html', {})
        else:
            return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})


def actualizar_producto(request):
        print("hola  estoy en actualizar_alumno...")
        if request.method == 'POST':
            mi_id = request.POST['id_producto']
            mi_numero = request.POST['numero']
            mi_precio = request.POST['precio']
            mi_nombre = request.POST['nombre']
            mi_foto = request.FILES.get('foto')
            mi_stock = request.POST['stock']
            mi_tipo = request.POST['tipo']

            if mi_numero != "":
                try:
                    producto = Producto()
                    producto.id_producto = mi_id
                    producto.numero = mi_numero
                    producto.precio = mi_precio
                    producto.nombre = mi_nombre
                    producto.foto = mi_foto
                    producto.stock = mi_stock
                    producto.tipo = mi_tipo

                    producto.save()

                    return render(request, 'productos/mensaje_datos_grabados.html', {})

                except producto.DoesNotExist:
                    return render(request, 'productos/error/error_204.html', {})
            else:
                return render(request, 'productos/error/error_201.html', {})
        else:
            return render(request, 'productos/error/error_203.html', {})

def agregar_producto(request):
    print("hola  estoy en actualizar_alumno...")
    if request.method == 'POST':
        mi_numero = request.POST['numero']
        mi_nombre = request.POST['nombre']
        mi_precio = request.POST['precio']
        mi_stock = request.POST['stock']
        mi_foto = request.FILES['foto']
        mi_tipo = request.POST['tipo']

        if mi_numero != "":
            try:
                producto = Producto()
                producto.numero = mi_numero
                producto.nombre = mi_nombre
                producto.precio = mi_precio
                producto.foto = mi_foto
                producto.stock = mi_stock
                producto.activo = 1
                producto.tipo = mi_tipo

                producto.save()

                return render(request, 'productos/mensaje_datos_grabados.html', {})

            except producto.DoesNotExist:
                return render(request, 'productos/error/error_204.html', {})
        else:
            return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def menu(request):
    print("ok, estamos en la vista menu alumnos")
    productos = Producto.objects.all()
    context={'Producto':productos}
    return render(request,'productos/menu_producto.html',context)

def Inicio(request):
    print("ok, estamos en la vista menu alumnos")
    productos = Producto.objects.all()
    context={'Producto':productos}
    return render(request,'productos/Inicio.html',context)


