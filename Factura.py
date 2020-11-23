def Calcula_Valor_Factura (Precios_Productos):
  Total_Precios_Productos=0
  for Item in Precios_Productos:
    Total_Precios_Productos = Precios_Productos.get(Item) + Total_Precios_Productos
  return Total_Precios_Productos

Dic_factura = {}
Opcion=0
V_iva=0.19
print ('PRODUCTOS COMPRADOS')
while Opcion==0:
  Codigo_Producto = str(input("Codigo Producto : "))
  #llamar funcion consultar en directorio de productos , traer nomobre, valor
  #con eso valores ingresarlos al directorio Dic_factura
  Cantidad_Producto = int(input("Cantidad Producto : "))
  Nombre_Producto = str(input("Nombre Producto : "))
  Valor_Producto = int(input("Valor Producto : "))
  Valor_producto = Valor_Producto * Cantidad_Producto
  Dic_factura.setdefault('Nombre_Producto' : Valor_Producto, )
  Dic_factura.setdefault
  Opcion = int(input("Deseas ingresar otro valor: 1. Si , 2. No :" ))
  if Opcion == 1:
    Opcion=0
  else: 
    Sub_Valor_factura = Calcula_Valor_Factura(Dic_factura)
    print(Dic_factura)
    Vlr_Iva= round(Sub_Valor_factura * V_iva)
    Valor_Total_Factura = Sub_Valor_factura + Vlr_Iva
    print ('Valor Sub Total Productos {}'.format(Sub_Valor_factura)) 
    print ('Valor IVA Factura 19% {}'.format(Vlr_Iva)) 
    print ('Valor Total Factura {}'.format(Valor_Total_Factura))   
    Opcion = 1
def calculabalance(facturas):
    ValorVentas = 0
    ValorCompra = 0
    for key, values in facturas.items():
        print(key, values)
        ValorVentas = (vbalance['cantidad'] * vbalance['valorUnitario']) + ValorVentas
        ValorCompra = (vbalance['valorUnitarioC'] * vbalance['cantidad']) + ValorCompra                  
    ValorBalance = ValorVentas - ValorCompra 
    return ValorBalance