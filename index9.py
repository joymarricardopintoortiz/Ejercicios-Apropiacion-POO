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

    def set_precio(self):
        return self.precio

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
    def __init__(self, productos_iniciales=[]):
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

    def vender_prodcutos(self, productos):
        for nombre, cantidad in productos.items():
            if self.esta_producto(nombre):
                for producto in self.productos:
                    if producto.get_nombre() == nombre:
                        producto.vender(cantidad)

    def ver_inventario(self):
        if len(self.productos) == 0:
            print("El inventario esta vacio")
        else:
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
producto2 = Producto("Leche", 3500, 5)

tienda = Tienda([producto1, producto2])

print("Inventario Inicial")
tienda.ver_inventario()

print("Comprando Productos")
tienda.comprar_productos({
    "Arroz": 5,
    "Leche": 3,
    "Pan": 10
})

tienda.ver_inventario()

print("Vendiendo Productos")
tienda.vender_prodcutos({
    "Arroz": 3,
    "Leche": 2,
    "Pan": 4,
    "Gaseosa": 2
})

tienda.ver_inventario()

print("Aumentando Precio")
tienda.aumentar_precio("Arroz", 500)

tienda.ver_inventario()

print("¿Esta el producto?")
print(tienda.esta_producto("Arroz"))
print(tienda.esta_producto("Gaseosa"))

print("Total Dinero del Inventario")
print(f"${tienda.total_dinero_inventario()}")