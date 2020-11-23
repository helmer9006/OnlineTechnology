# region MENú PRINCIPAL
print("""
    ***************************************************
    *******************MENÚ PRINCIPAL****************
    ***************************************************\n
    SELECCIONAR OPERACIÓN A REALIZAR
    1 - CREAR PRODUCTO
    2 - VENDER PRODUTO
    3 - CALCULAR PERDIDAS O GANANCIAS
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
    }
]
facturas = [

]
# endregion

# region CREAR PRODUCTO


def crearProducto():
    codigo = input('Por favor, ingresar código del producto: ')
    nombre = input('Por favor, ingresar nombre del producto: ')
    precioCompra = float(
        input('Por favor, ingresar precio de compra del producto: '))
    precioVenta = float(
        input('Por favor, ingresarprecio de venta para el producto: '))
    nuevoProducto = {"codigo": codigo, "nombre": nombre,
                     "precioCompra": precioCompra, "precioVenta": precioVenta}
    return nuevoProducto
# endregion

# region VENDER PRODUCTOS


def venderProducto(productos):
    factura = []
    while True:
        codigoProducto = input("Ingresar código del producto : ")

        for i in productos:
            if i['codigo'] == codigoProducto:
                cantidad = int(input("Ingresas la cantidad a vender : "))
                iva = i['precioVenta'] * 0.19
                valorTotal = (cantidad * i['precioVenta'])+iva
                factura.append(
                    {"codigo": codigoProducto, "cantidad": cantidad, "valorUnitario": i['precioVenta'], "valorTotal": valorTotal})
            else:
                print("producto con código ", codigoProducto, " no existe.")
        opcion = int(input("Deseas ingresar otro producto: 1. Si , 2. No : "))
        if opcion == 2:
            break
    return factura
# endregion

# region SWITCH DE OPERACIONES
while True:
    opcion = int(input("\nIngresar número según operación a realizar : "))
    if(opcion == 1):
        productos.append(crearProducto())
    elif(opcion == 2):
        facturas.append(venderProducto(productos))
    elif(opcion == 3):
        print("opcion validar perdida")
    elif(opcion == 4):
        print("Has Finalizado.. Gracias.")
        break
    else:
        print('Opción invalida')
print(productos)
print(facturas)

# endregion
