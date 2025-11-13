class Carro: 
    def __init__(self,marca,modelo,cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False

        def ligar(self): 
            if not self.ligado:
                self.ligado = True
                print(f"O {self.marca} {self.modelo} ligou.")
            else:
                print(f"{self.modelo} ja esta ligado.")
        def status (self):
            estado = "ligado" if self.ligado else "desligado"
            print(f"Status do {self.modelo} : {estado}")

        meu_carro = Carro("Toyota", "Corolla", "Prata")

        meu_carro = Carro("Honda", "Civic", "Preto")

        print(f"Marca do meu carro: {meu.carro.marca}")
        meu_carro.status()
        meu_carro.ligar()
        meu_carro.status()

        print(f"Cor do carro do amigo: 88{carro_amigo.cor}")
