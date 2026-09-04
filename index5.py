# pip install tabulate

from tabulate import tabulate


class Estudiante:
    __institucion = "Universidad Nacional"
    __cantidad_estudiantes = 0

    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = self.__validar_nota(nota1)
        self.__nota2 = self.__validar_nota(nota2)
        Estudiante.__cantidad_estudiantes += 1

    def __validar_nota(self, nota):
        if 0 <= nota <= 5:
            return nota
        else:
            raise ValueError("La nota debe estar entre 0 y 5.")

    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2

    def mostrar_informacion(self):
        print("Nombre:", self.__nombre)
        print("Nota 1:", self.__nota1)
        print("Nota 2:", self.__nota2)
        print("Nota promedio:", self.obtener_nota_promedio())
        print("Institucion:", Estudiante.__institucion)

    def __str__(self):
        return f"Nombre: {self.__nombre}, Nota promedio: {self.obtener_nota_promedio()}, Institucion: {Estudiante.__institucion}"

    @classmethod
    def cambiar_institucion(cls, nueva_institucion):
        cls.__institucion = nueva_institucion

    @classmethod
    def obtener_institucion(cls):
        return cls.__institucion

    @classmethod
    def obtener_cantidad_estudiantes(cls):
        return cls.__cantidad_estudiantes

    @classmethod
    def ver_escala(cls):
        datos = [
            ["0 a 2.9", "BAJA"],
            ["3 a 3.9", "MEDIA"],
            ["4 a 4.5", "ALTA"],
            ["4.6 a 5", "SOBRESALIENTE"]
        ]

        print(tabulate(datos, headers=["Nota", "Escala"], tablefmt="grid"))


estudiante1 = Estudiante("Juan Perez", 4.5, 3.8)
estudiante2 = Estudiante("Maria Lopez", 4.2, 4.8)
estudiante3 = Estudiante("Carlos Gomez", 3.5, 4.0)

print(estudiante1)
print(estudiante2)
print(estudiante3)

print("Cantidad de estudiantes:", Estudiante.obtener_cantidad_estudiantes())

Estudiante.cambiar_institucion("Universidad Industrial de Santander")

print(estudiante1)
print(estudiante2)
print(estudiante3)

Estudiante.ver_escala()