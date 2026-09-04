class Cuenta:
    def __init__(self, numero, tipo, saldo):
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo

    def ver_info(self):
        return f"Cuenta: {self.numero} | Tipo: {self.tipo} | Saldo: ${self.saldo}"

class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.cuenta = None

    def agregar_cuenta(self, numero, tipo, saldo):
        self.cuenta = Cuenta(numero, tipo, saldo)

    def ver_info(self):
        if self.cuenta is not None:
            return (
                f"Cedula: {self.cedula} | "
                f"Nombre: {self.nombre} | "
                f"Numero de cuentas: {self.cuenta.numero} | "
                f"Tipo: {self.cuenta.tipo} | "
                f"Saldo: ${self.cuenta.saldo}"
            )
        else:
            return (
                f"Cedula: {self.cedula} | "
                f"Nombre: {self.nombre} | "
                f"Sin cuenta"
            )

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def cambiar_nombre(self, nombre):
        self.nombre = nombre

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.clientes)

    def obtener_clientes(self):
        return self.clientes

    def ver_clientes(self):
        if len(self.clientes) == 0:
            print("No hay clientes registrados")
        else:
            print(f"Banco: {self.nombre}")
            print(f"Total de clientes: {self.obtener_numero_clientes()}")

            for cliente in self.clientes:
                print(cliente.ver_info())

    def total_saldos_ahorros(self):
        total = 0

        for cliente in self.clientes:
            if cliente.cuenta is not None:
                if cliente.cuenta.tipo.lower() == "ahorros":
                    total += cliente.cuenta.saldo

        return total

    def total_saldos_corriente(self):
        total = 0

        for cliente in self.clientes:
            if cliente.cuenta is not None:
                if cliente.cuenta.tipo.lower() == "corriente":
                    total += cliente.cuenta.saldo

        return total

banco = None

while True:
    print("1) Crear/cambiar nombre Banco")
    print("2) Agregar Cliente a un Banco")
    print("3) Ver informacion clientes")
    print("4) Ver saldos totales cuentas de ahorros")
    print("5) Ver saldos totales cuentas corrientes")
    print("6) Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del banco: ")

        if banco is None:
            banco = Banco(nombre)
            print("Banco creado correctamente")
        else:
            banco.cambiar_nombre(nombre)
            print("Nombre del banco actualizado")

    elif opcion == "2":
        if banco is None:
            print("Primero debe crear el banco")
        else:
            cedula = input("Ingrese la cedula: ")
            nombre = input("Ingrese el nombre del cliente: ")
            numero = input("Ingrese el numero de cuenta: ")
            tipo = input("Ingrese el tipo de cuenta (ahorros/corriente): ")
            saldo = float(input("Ingrese el saldo: "))

            cliente = Cliente(cedula, nombre)
            cliente.agregar_cuenta(numero, tipo, saldo)

            banco.adicionar_cliente(cliente)

            print("Cliente agregado correctamente")

    elif opcion == "3":
        if banco is None:
            print("Primero debe crear el banco")
        else:
            banco.ver_clientes()

    elif opcion == "4":
        if banco is None:
            print("Primero debe crear el banco")
        else:
            total = banco.total_saldos_ahorros()
            print(f"Total saldos cuentas de ahorros: ${total}")

    elif opcion == "5":
        if banco is None:
            print("Primero debe crear el banco")
        else:
            total = banco.total_saldos_corriente()
            print(f"Total saldos cuentas corrientes: ${total}")

    elif opcion == "6":
        print("Programa finalizado")
        break

    else:
        print("Opcion invalida")