from cuenta import Cuenta
from cliente import Cliente

class Banco:
  cuentas_abiertas=0
  def __init__(self):
    self.clientes = []
    self.cuentas = []

  def abrir_cuenta(self, nuevocliente:Cliente, saldo_inicial:int):
    Banco.cuentas_abiertas +=1
    cuenta=Cuenta(f"ING000{Banco.cuentas_abiertas}", saldo_inicial)
    riesgo=self.cambiar_riesgo(nuevocliente)
    nuevocliente.riesgo_credito=riesgo
    self.clientes.append(nuevocliente)
    self.cuentas.append(cuenta)

  def listar_cuentas(self):
    for cuenta, cliente in zip(self.cuentas, self.clientes):
      print(f"cuenta={cuenta.numero}, cliente={cliente.nombre}, saldo={cuenta.saldo}")


  def saldo_total(self):
    saldo_total=0
    for cuenta in self.cuentas:
      saldo_total += cuenta.saldo
    return saldo_total


  def ingresar(self, cliente:Cliente, cantidad:int):
    for posicio, clienteexistente in enumerate(self.clientes):
      if clienteexistente.identificacion == cliente.identificacion:
        self.cuentas[posicio].ingresar(cantidad)
        return
    return (f"El {cliente.nombre} no es cliente de este banco")
    

  def retirar(self, cliente:Cliente, cantidad:int):
    for posicio, clienteexistente in enumerate(self.clientes):
      if clienteexistente.identificacion == cliente.identificacion :
        if self.cuentas[posicio].saldo < cantidad:
          if self.cuentas[posicio].saldo + clienteexistente.riesgo_credito > cantidad:
            self.cuentas[posicio].retirar(cantidad)
            print("Saldo insuficiente. Le hemos dado crédito")
          else: 
            print("No hay saldo")
        else:
          self.cuentas[posicio].retirar(cantidad)
        return
    return (f"El {cliente.nombre} no es cliente de este banco")
    

  @staticmethod
  def cambiar_riesgo(cliente:Cliente):
    if cliente.edad >= 50:
      return 200
    elif cliente.edad >= 30 and cliente.edad <50:
      return 100
    else:
      return 0
  
  def edad_media (self):
    suma=0   
    for cliente in self.clientes:
        suma = suma+cliente.edad
    return suma/len(self.clientes)
     
