class ContaBancaria:
    def __init__(self,titular,saldo_inicial):
        self.titular = titular # Atributo público
        self.__saldo=saldo_inicial #Atributo privado

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print(f"Saque de R${valor} realizado com sucesso!")
    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo-=valor
            print(f"Saque de R${valor} realizado com sucesso!")
        else:
            print(f"Saldo insuficiente oara saque.")
        
    def verificar_saldo(self):
        print(f"Saldo atual:{self.__saldo}")
#Testando a classe
conta = ContaBancaria("João",1000)
conta.verificar_saldo()#saldo atual: R$1000
conta.depositar(500)#Depósito de R$500 realizado
conta.verificar_saldo()#saldo atual: R$1500
conta.sacar(2000)#Saldo insuficiente
conta.sacar(300)#Saque de R$300 realizido
conta.verificar_saldo()#Saldo atual: R$1200