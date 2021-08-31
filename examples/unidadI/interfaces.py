import abc

class Alarma(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def setAlarma(self):
        pass

class Despertador(Alarma):
    def color(self):
        print("Rojo")

    def setAlarma(self):
        print("Colocamos la alarma moviendo perillas")
    def mostrarHora(self):
        print("Son las 11:00")

class Celular(Alarma):
    def setAlarma(self):
        print("Colocamos la alarma llendo al menu del reloj")
    def llamar(self):
        print("Llamar a contacto")

class Alexa(Alarma):
    def setAlarma(self):
        print("Alexa, establece alarma 5.00 am")

desp = Despertador()
print(desp.color())