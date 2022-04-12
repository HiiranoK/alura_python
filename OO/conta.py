class Conta:
    def __init__(self,numero,titular,saldo,cheque_especial = 500.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__cheque_especial = cheque_especial
        print("construindo uma conta com o nº {}, do titular {}, com {} de saldo e {} de cheque especial disponível".format(numero,titular,saldo,cheque_especial))

    def extrato(self):
        print("O saldo da conta de {} é {}".format(self.__titular,self.__saldo))
    
    def deposita(self,valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

conta = Conta(1234,"Fulano",1000.0)
print(conta)
print(conta._Conta__saldo)