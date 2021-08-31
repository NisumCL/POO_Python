class Estudiante():
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def __str__(self):
        return "Nombre es: " + self.__nombre

student = Estudiante("Pedro", "Riquelme")
print(student)

