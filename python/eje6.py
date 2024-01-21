# Codigo para retirar dinero de una cuenta
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        while cantidad > self.saldo:   print("Saldo insuficiente. Espere a que haya suficientes fondos.")
        self.saldo -= cantidad

    def obtener_saldo(self):
        return self.saldo

mi_cuenta = CuentaBancaria(1000)

mi_cuenta.retirar(1500)

saldo_actual = mi_cuenta.obtener_saldo()
print(f'Saldo actual: ${saldo_actual}')
