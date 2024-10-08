from cuenta import Cuenta

class Cliente:
  def __init__(self, n:str, i:str, e:int, r=0):
    self.nombre = n
    self.identificacion= i
    self.edad = e
    self.riesgo_credito = r

#   def ingresar(self, cuenta:Cuenta, cantidad:int):
#     cuenta.ingresar(cantidad)

#   def retirar(self, cuenta:Cuenta, cantidad:int):
#     cuenta.retirar(cantidad)

  def __str__(self):
    return f"{self.nombre}, {self.identificacion}, {self.edad}, {self.riesgo_credito}"