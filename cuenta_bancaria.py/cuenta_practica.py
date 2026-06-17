class cuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, cantidad):
        if (cantidad >0):
            self.__saldo += cantidad

            print(f"Su saldo es:{self.__saldo}")
        else:
            print("Cantidad invaida")


    def retirar(self, cantidad):
        if 0<cantidad<=self.__saldo:
            self.__saldo-=cantidad
            print(f"Su saldo es de: {self.__saldo}")
        else: 
            print("Recuerda recargar su cuenta")

    def ver_saldo(self):
        print(f"El saldo total de {self.titular} es de {self.__saldo}")

#probar 
cuenta1 = cuentaBancaria("Laura castillo", 100000)
cuenta1.retirar(8000)
cuenta1.ver_saldo()
cuenta1.depositar(300000)
cuenta1.retirar(1000)
cuenta1.ver_saldo()

print(f"el saldo de: {cuenta1._cuentaBancaria__saldo}")






        