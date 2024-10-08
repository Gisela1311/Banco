class Cuenta:
  '''
  En esta cuenta encontramos el método init. además hemos creado los métodos ingresar y retirar para poder realizar entradas y salidas de dinero en la cuenta
  '''
  def __init__(self, num, saldo=0):
    self.numero = num
    self.saldo = saldo

  def ingresar(self, cantidad):
    self.saldo = self.saldo + cantidad

  def retirar(self, cantidad):
    self.saldo = self.saldo - cantidad