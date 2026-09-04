class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def ver_info(self):
        return f"Número: {self.numero} | Saldo: ${self.saldo}"


class CuentaAhorro(Cuenta):
    def __init__(self, numero, saldo, interes):
        super().__init__(numero, saldo)
        self.interes = interes

    def aplicar_interes(self):
        self.saldo += self.saldo * (self.interes / 100)


class CuentaCorriente(Cuenta):
    def __init__(self, numero, saldo, descuento):
        super().__init__(numero, saldo)
        self.descuento = descuento

    def aplicar_descuento(self):
        self.saldo -= self.saldo * (self.descuento / 100)


class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.cuenta = None

    def agregar_cuenta(self, cuenta):
        self.cuenta = cuenta

    def ver_info(self):
        if self.cuenta is not None:
            return (
                f"Cédula: {self.cedula} | "
                f"Nombre: {self.nombre} | "
                f"Número de cuenta: {self.cuenta.numero} | "
                f"Saldo: ${self.cuenta.saldo}"
            )
        else:
            return (
                f"Cédula: {self.cedula} | "
                f"Nombre: {self.nombre} | "
                f"Sin cuenta"
            )


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
    print("4) Obtener el número de clientes de un Banco")
    print("5) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del Banco: ")
        banco = Banco(nombre)
        print("Banco creado correctamente")

    elif opcion == "2":
        if banco is None:
            print("Primero debe crear un Banco")
        else:
            cedula = input("Ingrese la cédula del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")

            numero = input("Ingrese el número de cuenta: ")
            saldo = float(input("Ingrese el saldo: "))

            print("1. Cuenta de Ahorro")
            print("2. Cuenta Corriente")

            tipo = input("Seleccione el tipo de cuenta: ")

            if tipo == "1":
                interes = float(input("Ingrese el interés: "))
                cuenta = CuentaAhorro(numero, saldo, interes)

            elif tipo == "2":
                descuento = float(input("Ingrese el descuento: "))
                cuenta = CuentaCorriente(numero, saldo, descuento)

            else:
                print("Tipo de cuenta inválido")
                continue

            cliente = Cliente(cedula, nombre)
            cliente.agregar_cuenta(cuenta)
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
            print(f"El Banco tiene {cantidad} cliente")

    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Opción inválida")