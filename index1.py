class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def obtener_nota_promedio(self):
        return (self.nota1 + self.nota2) / 2

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Nota 1:", self.nota1)
        print("Nota 2:", self.nota2)
        print("Nota promedio:", self.obtener_nota_promedio())

estudiante1 = Estudiante("Juan Perez", 4.5, 3.8)

estudiante1.mostrar_informacion()