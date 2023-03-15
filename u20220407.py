from abc import ABC,abstractmethod

class Pablo(ABC):

    def __init__(self,nombre,comprension):
        self.nombre = nombre
        self.comprension = comprension

    @abstractmethod
    def estudiar():
        pass

class estudiarDia(Pablo):
    pass
    def estudiar(self):
        return "El Estudiante {} tiene una comprension {} a la hora de estudiar de dia".format(self.nombre,self.comprension)

class estudiarTarde(Pablo):
    pass
    def estudiar(self):
        return "El Estudiante {} tiene una comprension {} a la hora de estudiar de tarde".format(self.nombre,self.comprension)

class estudiarNoche(Pablo):
    pass
    def estudiar(self):
        return "El Estudiante {} tiene una comprension {} a la hora de estudiar de noche".format(self.nombre,self.comprension)




estudiar1 = estudiarDia("Pablo","Rapida")
estudiar2 = estudiarTarde("Pablo","Media")
estudiar3 = estudiarNoche("Pablo", "Lenta")
print(estudiar1.estudiar())
print(estudiar2.estudiar())
print(estudiar3.estudiar())
