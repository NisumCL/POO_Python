class Vehiculo():
    def acelerar(self):
        print("Acelerar generico")

class Moto(Vehiculo):
    def acelerar(self):
        print("Acelerar girando el puño derecho")

class Coche(Vehiculo):
    def acelerar(self):
        print("Acelerar apretando el acelerador")

class MotoAgua(Vehiculo):
    pass


auto = Coche()
print(auto.acelerar())

moto = Moto()
print(moto.acelerar())

motoAgua = MotoAgua()
print(motoAgua.acelerar())