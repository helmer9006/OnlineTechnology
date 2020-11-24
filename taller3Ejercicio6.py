# region MENÚ PRINCIPAL
print("""
    ***************************************************
    *******************MENÚ PRINCIPAL****************
    ***************************************************\n
    SELECCIONAR OPERACIÓN A REALIZAR
    1 - CREAR PRODUCTO
    2 - MODIFICAR PRODUCTO
    3 - ELIMINAR PRODUCTO
    4 - VENDER PRODUCTO
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
    """Permite la creación de un producto.
    Se solicita al usuario los valores para los campos: codigo, nombre, valor compra y valor venta y                
    y se devuelven los valores en un diccionario para ser ingresados al arreglo productos.

    Parametros: Ninguno
    Ejemplo diccionario devuelto:

    { "codigo": "cam1", "nombre": "camara 1", "precioCompra": 50000, "precioVenta": 80000} 

    Atributos:
    codigo: string, nombre: string, precioCompra: Float, precioVenta: Float

    """
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


def modificarProducto(productos):
    """Permite modificar un producto, pidiendo por consola al usuario el codigo de producto a modificar 
    y posteriormente los nuevos valores para actualizar el producto.

    Se devuelve arreglo con los productos actualizados
    parametros: Array de productos.

    Ejemplo parametro productos: 

    productos[{ "codigo": "cam1", "nombre": "camara 1", "precioCompra": 50000, "precioVenta": 80000} ,
              { "codigo": "cam1", "nombre": "camara 1", "precioCompra": 50000, "precioVenta": 80000}] 
    Atributos:
    codigo: string, nombre: string, precioCompra: Float, precioVenta: Float
    """
    while True:
        busqueda = 0
        codigoProducto = str(
            input("Ingresar código del producto a Modificar: "))
        for ibusqueda in productos:
            if ibusqueda['codigo'] == codigoProducto:
                print(ibusqueda)
                productos.remove(ibusqueda)
                codigo = codigoProducto
                nombre = input('Ingresar nombre del producto: ')
                precioCompra = float(input('Ingresar precio de compra del producto: '))
                precioVenta = float(input('Ingresar precio de venta para el producto: '))
                nuevoProducto = {"codigo": codigo, "nombre": nombre,
                                 "precioCompra": precioCompra, "precioVenta": precioVenta}
                productos.append(nuevoProducto)
                busqueda = 1
        if busqueda == 0:
            print("producto con código ", codigoProducto, " no existe.")
        opcion = int(input("Deseas modificar otro producto: 1. Si , 2. No : "))
        if opcion == 2:
            break
    return productos
# endregion


# region ELIMINAR PRODUCTO
"""
 Permite eliminar producto a partir del codigo de producto a eliminar solicitado al usuario. 
 Elimina producto del array productos. 

 Parametros: No recibe. 
 
"""


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
    """Permite realizar venta de productos, pidiendo por consola al usuario el codigo de producto a vender y la cantidad.

    parametros: Array de productos.

    Ejemplo array retornado: 

    {"codigo": 'cam1', "cantidad": 2, "valorUnitario": 50000, "valorUnitarioC": 19000, "valorTotal": 119000})
    
    """


def venderProducto(productos):
    factura = []
    vsubfactura = 0
    valorTotalIva =0
    while True:
        busqueda = 0
        codigoProducto = str(input("Ingresar código del producto : "))
        for iventa in productos:
            if iventa['codigo'] == codigoProducto:
                cantidad = int(input("Ingrese cantidad : "))
                iva = (iventa['precioVenta'] * 0.19) * cantidad
                valorTotalIva = valorTotalIva + iva
                valorTotal = (cantidad * iventa['precioVenta'])
                vsubfactura = valorTotal + vsubfactura
                factura.append(
                    {
                      "codigo": codigoProducto, 
                      "cantidad": cantidad, 
                      "valorUnitario": iventa['precioVenta'], 
                      "valorUnitarioC": iventa['precioCompra'], 
                      "valorTotal": valorTotal
                     }
                )
                # print(factura)
                busqueda = 1
        if busqueda == 0:
            print("producto con código ", codigoProducto, " no existe.")
        opcion = int(input("Deseas ingresar otro producto: 1. Si , 2. No : "))
        if opcion == 2:
            vtfactura = vsubfactura + valorTotalIva
            break
    print("Valor Sub Total     : ", vsubfactura)
    print("Valor IVA           : ", valorTotalIva)
    print("Valor Total a Pagar : ", vtfactura)
    return factura
# endregion


# region CALCULA PERDIDAS O GANANCIAS DE LAS FACTURAS DEL DIA
"""Funcion que nos permite calcular el balance indicativo para validar si nuestras ventas
    generan ganancia o perdidas. 
    Parametros: Array Facturas.

    Ejemplo Array: una factura con un item:
    facturas =[[{'codigo': 'cam1', 'cantidad': 3, 'valorUnitario': 80000, 'valorUnitarioC': 50000, 'valorTotal': 240000}]]
    
    Devuelve el valor del balance. 
    se calcula restando  restando los valores de venta - valores de compra

"""


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
    """Funcion que me permite listar los productos creados
    Devuelve diccionarios de productos, donde se identifican las llaves y sus valores. 
    nombre producto, valor compra, valor venta y codigo.

    Parametros: No recibe.

    Ejemplo de impresión de productos. 

    producto #  3

    codigo   cam3
    nombre   camara 3
    precioCompra   60000
    precioVenta   90000


    """

def verProductos():
    cont = 1
    for producto in productos:
        print('\nproducto # ', cont, "\n")
        for llave, valor in producto.items():
            print(llave, " ", valor)
        cont += 1
# endregion


# region SWITCH DE OPERACIONES
"""Condicional que permite gestionar el menu principal.

    Se inicializa con un while en true, captura la opcion deseada por el usuario según
    descripción detallada en las opciones del menu. 
    Según el numero ingresado por el usuario se ejectuca una de las opciones del condicional.
    Finaliza con la opcion  0.    
"""
while True:
    opcion = int(input("\nIngresar número según operación a realizar : "))
    if(opcion == 1):
        productos.append(crearProducto())
    elif(opcion == 2):
        productoModif = modificarProducto(productos)
        print("Productos Modificados ", productoModif)
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

