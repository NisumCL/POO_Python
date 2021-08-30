""" Clase circulo """


class Circulo:

    """
        Constructor de la clase

        Este es llamado cuando alguien crea un nuevo círculo.
        Acá se le asignan parámetros por defecto en el proceso
        de creación del objeto
    """
    def __init__(self, center, radio):
        self.__center = center
        self.__radio = radio

    """ Método que usamos para dibujar un círculo """
    def draw(self, canvas):
        rad = self.__radio
        (x1, y1) = (self.__center[0] - rad, self.__center[1] - rad)
        (x2, y2) = (self.__center[0] + rad, self.__center[1] + rad)
        canvas.create_oval(x1, y1, x2, y2, fill='green')

    """ Método que usamos para mover un circulo """
    def move(self, x, y):
        self.__center = [x, y]
        self.__process(10)

    def __process(self, rad):
        self.__center = [rad, rad]


