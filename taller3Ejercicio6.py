# region MENú PRINCIPAL
print("""
    ***************************************************
    *******************MENÚ PRINCIPAL****************
    ***************************************************\n
    SELECCIONAR OPERACIÓN A REALIZAR
    1 - CREAR PRODUCTO
    2 - VENDER PRODUTO
    3 - CALCULAR PERDIDAS O GANANCIAS
    4 - SALIR

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

# region VENDER PRODUCTOS
def venderProducto(productos):
    factura = []
    vtiva = 0
    vsubfactura = 0
    while True:
        busqueda=0
        codigoProducto = str(input("Ingresar código del producto : "))
        for iventa in productos:
            if iventa['codigo']  == codigoProducto:
                cantidad = int(input("Ingrese cantidad : "))
                iva = (iventa['precioVenta'] * 0.19) * cantidad
                vtiva = vtiva + iva 
                valorTotal = (cantidad * iventa['precioVenta'])
                vsubfactura = valorTotal + vsubfactura
                factura.append(
                    {"codigo": codigoProducto, "cantidad": cantidad, "valorUnitario": iventa['precioVenta'], "valorUnitarioC": iventa['precioCompra'], "valorTotal": valorTotal})
                print(factura)   
                busqueda=1
        if  busqueda == 0:
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

# region CALCULA PERDIDAS O GANANCIAS
def calculabalance(facturas):
    vbalance = 0 
    cbalance = 0
    for nFactura in facturas: 
       for detFact in nFactura:
          vbalance = vbalance + (detFact.get('cantidad') * detFact.get('valorUnitario'))
          cbalance = cbalance + (detFact.get('cantidad') * detFact.get('valorUnitarioC'))
    tbalance = vbalance - cbalance
    return tbalance
# endregion

# region SWITCH DE OPERACIONES
while True:
    opcion = int(input("\nIngresar número según operación a realizar : "))
    if(opcion == 1):
        productos.append(crearProducto())
    elif(opcion == 2):
        facturas.append(venderProducto(productos))
    elif(opcion == 3):
        Balance=calculabalance(facturas)
        print("Balance de Compras vs Ventas ", Balance)
    elif(opcion == 4):
        print("Has Finalizado.. Gracias.")
        break
    else:
        print('Opción invalida')
print(productos)
print(facturas)
# endregion
