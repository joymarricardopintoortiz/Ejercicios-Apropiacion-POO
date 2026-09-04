class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    def ver_info(self):
        return f"Cedula: {self.cedula} | Nombre: {self.nombre}"

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.clientes)

    def obtener_clientes(self):
        return self.clientes

banco = None

while True:
    print("1) Crear Banco")
    print("2) Agregar Cliente a un Banco")
    print("3) Ver los clientes de un Banco")
    print("4) Obtener el numero de clientes de un Banco")
    print("5) Salir")

    opcion = input("Selecciones una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del Banco: ")
        banco = Banco(nombre)
        print("Banco creado correctamente")

    elif opcion == "2":
        if banco is None:
            print("Primero debe crear un Banco")
        else:
            cedula = input("Ingrese la cedula del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")

            cliente = Cliente(cedula, nombre)
            banco.adicionar_cliente(cliente)

            print("Cliente agregado correctamente")

    elif opcion == "3":
        if banco is None:
            print("Primero debe crear un Banco")
        else:
            clientes = banco.obtener_clientes()

            if len(clientes) == 0:
                print("El Banco no tiene clientes")
            else:
                print(f"Clientes del Banco {banco.nombre}:")

                for cliente in clientes:
                    print(cliente.ver_info())

    elif opcion == "4":
        if banco is None:
            print("Primero debe crear un Banco")
        else:
            cantidad = banco.obtener_numero_clientes()
            print(f"El banco tiene {cantidad} cliente")

    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Opcion invalida")