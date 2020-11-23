lista =[
    [{'codigo': 'cam1', 'cantidad': 2, 'valorUnitario': 80000, 'valorUnitarioC': 50000, 'valorTotal': 160000}, 
     {'codigo': 'cam2', 'cantidad': 1, 'valorUnitario': 85000, 'valorUnitarioC': 55000, 'valorTotal': 85000}], 
    [{'codigo': 'cam3', 'cantidad': 1, 'valorUnitario': 90000, 'valorUnitarioC': 60000, 'valorTotal': 90000}]
]

productos = [
    {
        "codigo": "cam1",
        "nombre": "camara 1",
        "precioCompra": 50000,
        "precioVenta": 80000
    },
    {
        "codigo": "cam2",
        "nombre": "camara 2",
        "precioCompra": 55000,
        "precioVenta": 85000
    }
]   

def ModificarProducto(productos):
    while True:
        busqueda=0
        codigoProducto = str(input("Ingresar código del producto : "))
        for ibusqueda in productos:
            if ibusqueda['codigo']  == codigoProducto:
               print (ibusqueda)
               ibusqueda['nombre'] = str(input("Ingrese nombre del producto : "))
               ibusqueda["precioCompra"] = float(input('Ingresar precio de compra del producto: '))
               ibusqueda["precioVenta"] = float(input('Ingresar precio de venta del producto: '))
               print("Cambio guardado", ibusqueda)   
               busqueda=1
        if  busqueda == 0:
            print("producto con código ", codigoProducto, " no existe.")     
        opcion = int(input("Deseas modificar otro producto: 1. Si , 2. No : "))
        if opcion == 2:
            break
    print (productos)
    return productos


def ModificarProducto(productos):
    while True:
        busqueda=0
        codigoProducto = str(input("Ingresar código del producto a borrar : "))
        for ibusqueda in productos:
            if ibusqueda['codigo']  == codigoProducto:
               print (ibusqueda)
               ibusqueda.pop()
               print("Cambio guardado", ibusqueda)   
               busqueda=1
        if  busqueda == 0:
            print("producto con código ", codigoProducto, " no existe.")     
        opcion = int(input("Deseas modificar otro producto: 1. Si , 2. No : "))
        if opcion == 2:
            break
    print (productos)
    return productos
# endregion


vbalance = 0
cbalance = 0
for elem in lista: 
    for k in elem:
       vbalance = vbalance + (k.get('cantidad') * k.get('valorUnitario'))
       cbalance = cbalance + (k.get('cantidad') * k.get('valorUnitarioC'))
tbalance = vbalance - cbalance
print (tbalance)

kt = ModificarProducto(productos)
print(kt)
