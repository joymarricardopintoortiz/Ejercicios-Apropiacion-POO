class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Nombre: {self.nombre} | Precio: ${self.precio} | Cantidad: {self.cantidad}"

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def aumentar_precio(self, monto):
        self.precio += monto

    def pedir(self, cantidad):
        self.cantidad += cantidad

    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        return False

class Tienda:
    def __init__(self, productos_iniciales=None):
        if productos_iniciales is None:
            productos_iniciales = []

        self.productos = productos_iniciales

    def comprar_productos(self, productos):
        for nombre, cantidad in productos.items():
            if self.esta_producto(nombre):
                for producto in self.productos:
                    if producto.get_nombre() == nombre:
                        producto.pedir(cantidad)
            else:
                producto = Producto(nombre, 0, cantidad)
                self.productos.append(producto)

    def vender_productos(self, productos):
        for nombre, cantidad in productos.items():
            if self.esta_producto(nombre):
                for producto in self.productos:
                    if producto.get_nombre() == nombre:
                        producto.vender(cantidad)

    def ver_inventario(self):
        for producto in self.productos:
            print(producto)

    def aumentar_precio(self, producto, monto):
        for p in self.productos:
            if p.get_nombre() == producto:
                p.aumentar_precio(monto)

    def esta_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.get_nombre() == nombre_producto:
                return True
        return False

    def total_dinero_inventario(self):
        total = 0
        for producto in self.productos:
            total += producto.get_precio() * producto.cantidad
        return total

producto1 = Producto("Arroz", 4000, 10)
producto2 = Producto("Leche", 3500, 8)
producto3 = Producto("Huevos", 12000, 5)

tienda = Tienda([producto1, producto2, producto3])

print("Inventario Inicial")
tienda.ver_inventario()

print("Comprar 20 unidades de arroz")
tienda.comprar_productos({
    "Arroz": 20
})

print("Comprar 12 unidades de pan")
tienda.comprar_productos({
    "Pan": 12
})

tienda.productos[-1].set_precio(2500)

print("Inventario despues de las compras")
tienda.ver_inventario()

print("Vender 2 unidades de leche")
tienda.vender_productos({
    "Leche": 2
})

print("Inventar vender 1 unidad de gaseosa")

if tienda.esta_producto("Gaseosa"):
    tienda.vender_productos({
        "Gaseosa": 1
    })
else:
    print("El producto Gaseosa no existe en la tienda")

print("Inventario despues de las ventas")
tienda.ver_inventario()

print("Aumentar el precio del arroz en un 10%")

precio_actual = producto1.get_precio()
aumento = precio_actual * 0.10

tienda.aumentar_precio("Arroz", aumento)

print("Inventario despues del Aumento")
tienda.ver_inventario()

print("Total de Inventario del Dinero")

total = tienda.total_dinero_inventario()

print(f"${total}")