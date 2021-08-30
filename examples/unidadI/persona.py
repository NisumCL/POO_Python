class Persona:
    """Una clase persona simple"""
    def __init__(self):
        self.nombre = ""

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre


persona = Persona()
persona.set_nombre("Pedro")

print(persona.get_nombre())
