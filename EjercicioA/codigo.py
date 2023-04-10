class empleados :
    def __init__(self, nombre):
        self.nombre = nombre



class edificio :
    def __init__(self, letra):
        self.letra = letra
    empleados = []

class empresa :
    def __init__(self, nombre):
        self.nombre = nombre
    empleados = []
    edificios = []

class ciudad: 
    def __init__(self, nombre):
        self.nombre = nombre
    empresas = []
    edificio = []
    empleados = []



SrMartin = empleados("Sr.Martin")
Srsalim = empleados("Sr.Salim")
SraXang = empleados("Sra.Xang")
edificio_A = edificio("A", SrMartin)
edificio_B = edificio("B", Srsalim)
edificio_C = edificio("C", SraXang)
NY = ciudad("New York", edificio_A, edificio_B, SrMartin, Srsalim)
LA = ciudad("Los Angeles", edificio_C, SraXang)
yohoo = empresa("Yohoo", edificio_A, edificio_B, edificio_C, SrMartin, Srsalim, SraXang, NY, LA)

print(yohoo.nombre)
