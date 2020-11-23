# region MENÚ PRINCIPAL
print("""
    ***************************************************
    *******************MENÚ PRINCIPAL****************
    ***************************************************\n
    SELECCIONAR OPERACIÓN A REALIZAR
    1 - CREAR PRODUCTO
    2 - MODIFICAR PRODUTO
    3 - ELIMINAR PRODUTO
    4 - VENDER PRODUTO
    5 - CALCULAR PERDIDAS O GANANCIAS
    6 - VER PRODUCTOS
    0 - SALIR

    A continuación debe digitar el numero de la operación a realizar...
    """)
# endregion

# region VARIABLES GLOBALES
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
    },
    {
        "codigo": "cam3",
        "nombre": "camara 3",
        "precioCompra": 60000,
        "precioVenta": 90000
    }
]

facturas = [
]
# endregion

# region CREAR PRODUCTO


def crearProducto():
    codigo = input('Ingresar código del producto: ')
    nombre = input('Ingresar nombre del producto: ')
    precioCompra = float(
        input('Ingresar precio de compra del producto: '))
    precioVenta = float(
        input('Ingresar precio de venta para el producto: '))
    nuevoProducto = {"codigo": codigo, "nombre": nombre,
                     "precioCompra": precioCompra, "precioVenta": precioVenta}

    return nuevoProducto
# endregion

# region MODIFICAR PRODUCTOS

def ModificarProducto(productos):
    while True:
        busqueda = 0
        codigoProducto = str(
            input("Ingresar código del producto a Modificar: "))
        for ibusqueda in productos:
            if ibusqueda['codigo'] == codigoProducto:
                print(ibusqueda)
                ibusqueda['nombre'] = str(
                    input("Ingrese nombre del producto : "))
                ibusqueda["precioCompra"] = float(
                    input('Ingresar precio de compra del producto: '))
                ibusqueda["precioVenta"] = float(
                    input('Ingresar precio de venta del producto: '))
                print("Cambio guardado", ibusqueda)
                busqueda = 1
        if busqueda == 0:
            print("producto con código ", codigoProducto, " no existe.")
        opcion = int(input("Deseas modificar otro producto: 1. Si , 2. No : "))
        if opcion == 2:
            break
    return productos
# endregion

# region ELIMINAR PRODUCTO


def eliminarProducto():
    while True:
        buscar = False
        codigoProductoEliminar = input(
            "Ingresar código del producto a Eliminar : ")
        for producto in productos:
            if producto['codigo'] == codigoProductoEliminar:
                productos.remove(producto)
                buscar = True
        if buscar == False:
            print("producto con código ", codigoProductoEliminar, " no existe.")
        opcion = int(input("Deseas eliminar otro producto: 1. Si , 2. No : "))
        if opcion == 2:
            break
# endregion

# region VENDER PRODUCTOS


def venderProducto(productos):
    factura = []
    vtiva = 0
    vsubfactura = 0
    while True:
        busqueda = 0
        codigoProducto = str(input("Ingresar código del producto : "))
        for iventa in productos:
            if iventa['codigo'] == codigoProducto:
                cantidad = int(input("Ingrese cantidad : "))
                iva = (iventa['precioVenta'] * 0.19) * cantidad
                vtiva = vtiva + iva
                valorTotal = (cantidad * iventa['precioVenta'])
                vsubfactura = valorTotal + vsubfactura
                factura.append(
                    {"codigo": codigoProducto, "cantidad": cantidad, "valorUnitario": iventa['precioVenta'], "valorUnitarioC": iventa['precioCompra'], "valorTotal": valorTotal})
                # print(factura)
                busqueda = 1
        if busqueda == 0:
            print("producto con código ", codigoProducto, " no existe.")
        opcion = int(input("Deseas ingresar otro producto: 1. Si , 2. No : "))
        if opcion == 2:
            vtfactura = vsubfactura + vtiva
            break
    print("Valor Sub Total     : ", vsubfactura)
    print("Valor IVA           : ", vtiva)
    print("Valor Total a Pagar : ", vtfactura)
    return factura
# endregion

# region CALCULA PERDIDAS O GANANCIAS DE LAS FACTURAS DEL DIA


def calculabalance(facturas):
    vbalance = 0
    cbalance = 0
    for nFactura in facturas:
        for detFact in nFactura:
            vbalance = vbalance + (detFact.get('cantidad')
                                   * detFact.get('valorUnitario'))
            cbalance = cbalance + (detFact.get('cantidad')
                                   * detFact.get('valorUnitarioC'))
    tbalance = vbalance - cbalance
    return tbalance
# endregion

# region VER PRODUCTO
def verProductos():
    cont = 1
    for producto in productos:
        print('\nproducto # ', cont, "\n")
        for llave, valor in producto.items():
            print(llave, " ", valor)  
        cont += 1        
# endregion 

# region SWITCH DE OPERACIONES
while True:
    opcion = int(input("\nIngresar número según operación a realizar : "))
    if(opcion == 1):
        productos.append(crearProducto())
    elif(opcion == 2):
        ProductoModif = ModificarProducto(productos)
        print("Productos Modificados ", ProductoModif)
    elif(opcion == 3):
        eliminarProducto()
    elif(opcion == 4):
        facturas.append(venderProducto(productos))
    elif(opcion == 5):
        Balance = calculabalance(facturas)
        print("Balance de Compras vs Ventas ", Balance)
    elif(opcion == 6):
        verProductos()
    elif(opcion == 0):
        print("Has Finalizado.. Gracias.")
        break
    else:
        print('Opción invalida')
# endregion
