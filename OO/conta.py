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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = (self.__saldo + self.__cheque_especial)
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor de {}, é superior ao seu limite.".format(valor))

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular.title()
    @property
    def numero(self):
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo
    @property
    def cheque_especial(self):
        return self.__cheque_especial
    @cheque_especial.setter
    def cheque_especial(self,novo_limite):
        self.__cheque_especial = novo_limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001','Caixa':'104','Bradesco':'237'}

#executando testes no console.        

conta = Conta(1234,"Fulano",1000.0)

conta_origem = Conta(4444,"Beutrano",2000.0)
conta_destino = Conta(5555,"Siclano",400.0)

#conta_origem.transfere(1000,conta_destino)
#conta_origem.extrato()
#conta_destino.extrato()

print(conta.cheque_especial)
conta.cheque_especial = 10000.0
print(conta.cheque_especial)
print(Conta.codigo_banco())
print(Conta.codigos_bancos())
codigos = Conta.codigos_bancos()
print(codigos["Bradesco"])