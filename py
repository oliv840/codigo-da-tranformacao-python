class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        """
        Método de inicialização para CarroEletrico.
        Chama o construtor da classe pai para herdar os atributos.
        """
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria
        
    def exibir_info(self):
        """
        Sobrescreve o método da classe pai para adicionar a autonomia.
        """
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Autonomia da Bateria: {self.autonomia_bateria} km")

    def __str__(self):
        """
        Método especial para representação em string.
        """
        return f"Carro Elétrico: {self.marca} {self.modelo} (Autonomia: {self.autonomia_bateria} km)"

# Exemplo de uso da classe CarroEletrico
meu_carro_eletrico = CarroEletrico("Tesla", "Model S", 650)
meu_carro_eletrico.exibir_info()
print(meu_carro_eletrico)
