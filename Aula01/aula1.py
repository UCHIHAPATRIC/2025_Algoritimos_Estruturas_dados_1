#contrua uma classe chamada Carro que possui os atributos modelo, ano e quilometragem
#esta classe também deve conter uma método para imprimir os dados de todos atributos


class Carro:
    def __init__(self, modelo = none, ano =2025):
        self.modelo = modelo
        self.ano = ano
        self.__kilometragem = 0

    def incrementar(self, km):
        if km > 0:
            self.__kilometragem += km

    def setKM(sekf, km):
        if km > self.__kilometragem:
            self.__kilometragem = km    

    def imprimir_dados(self):
        print(f"modelo: {self.modelo}")
        print(f"ano: {self.ano}")
        print(f"Quilometragem: {self.quilometragem} km")
    
carro1 = Carro("Gol", 2000, 500000)
carro1.imprimir_dados()