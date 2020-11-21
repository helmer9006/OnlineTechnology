

# region CREAR PRODUCTO
productos = [] # nombre, precioCompra, precioventa
def crearProducto():
    nombre = input('Por favor, ingresar nombre del producto: ')
    precioCompra = float(input('Por favor, ingresar precio de compra del producto: '))
    precioVenta = float(input('Por favor, ingresarprecio de venta para el producto: '))
    nuevoProducto = {"nombre":nombre, "precioCompra": precioCompra, "precioVenta":precioVenta} 
    productos.append(nuevoProducto)
