class ContaCorrente:
    def __init__(self,saldo):
        self.__saldo=saldo

    def depositar(self,valor):
        self.__saldo += valor
        
    def ver_saldo(self):
        print(f"Saldo atual:{self.__saldo}")

conta1 = ContaCorrente(1000)
conta1.depositar(200)
conta1.ver_saldo()