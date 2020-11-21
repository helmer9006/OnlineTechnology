Dic_Productos = {}
print ('Ingresas datos')
NombreProducto = str(input("Nombre del producto : "))
ValorProducto = int(input("Valor del producto : "))
Dic_Productos.setdefault(NombreProducto,ValorProducto)
print(Dic_Productos)