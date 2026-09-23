class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = self.__validar_nota(nota1)
        self.__nota2 = self.__validar_nota(nota2)

    def __validar_nota(self, nota):
        if 0 <= nota <= 5:
            return nota
        else:
            raise ValueError("La nota debe estar entre 0 y 5.")

    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2

    def mostrar_informacion(self):
        print("Nombre: ", self.__nombre)
        print("Nota 1: ", self.__nota1)
        print("Nota 2: ", self.__nota2)
        print("Nota promedio: ", self.obtener_nota_promedio())

    def __str__(self):
        return f"Nombre: {self.__nombre}, Nota promedio: {self.obtener_nota_promedio()}"

estudiante1 = Estudiante("Juan Perez", 4.5, 3.8)

print(estudiante1)
