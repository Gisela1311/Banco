from banco import Banco
from cliente import Cliente

ING=Banco()

cliente1 = Cliente("Gisela", "41245102E", 33, 2)
cliente2 = Cliente("Roser", "26530256T", 63, 1)
cliente3 = Cliente("Josep", "36502984V", 26, 3)


ING.abrir_cuenta(cliente1, 60)
ING.abrir_cuenta(cliente2, 100)
ING.abrir_cuenta(cliente3, 80)

ING.listar_cuentas()

ING.retirar(cliente2, 200)

ING.ingresar(cliente3, 20)

ING.listar_cuentas()

ING.saldo_total()

#opción 1
saldo= ING.saldo_total()
print(saldo)
#opción 2
print(ING.saldo_total())

print(ING.edad_media())


