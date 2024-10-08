class Cuenta:
  def __init__(self, num, saldo=0):
    self.numero = num
    self.saldo = saldo

  def ingresar(self, cantidad):
    self.saldo = self.saldo + cantidad

  def retirar(self, cantidad):
    self.saldo = self.saldo - cantidad