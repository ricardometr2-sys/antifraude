from collections import namedtuple

#Definiciónde registro
Producto = namedtuple ("Producto",["id","nombre","precio","stock","activo"])

def  mostrarInventario(lista):
    if not lista:
        print ("Inventario vacio")
        return

    for p in lista:
        print("__________________________________________________")
        print(f"ID: {p.id}")
        print(f"Nombre: {p.nombre}")
        print(f"Precio: {p.precio}")
        print(f"Stock: {p.stock}")
        print(f"Activo: {p.activo}")
    print("***************************************************************")

def actualizarPrecio(lista,idBuscar,nuevoPrecio):
    if nuevoPrecio<=0:
        print("Precio invalido")
        return
    
    for i,p in enumerate(lista):
        if p.id==idBuscar:
            lista[id]=p._replace(precio=nuevoPrecio)
            print("Precio cambiado de froma correcta")
            return

#prueba del sistema

inventario=[
    Producto(1,"Laptop",15000.00,5,True),
    Producto(2,"Mouse",300.00,20,True),
    Producto(3,"Teclado",800.00,10,True)
]

mostrarInventario(inventario)

actualizarPrecio(inventario,2,350.0)


















































#Tuplas