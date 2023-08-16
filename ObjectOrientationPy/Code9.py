# Encapsulamento 
# ---- Decorator @property ----
# mantém-se os atributos protegidos(acessados apenas por meio dos métodos "decorados" com property)

class Retangulo:
    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento 
        self.__largura = largura 

    @property
    def area(self):
        return self.__comprimento * self.__largura
        
    @property
    def comprimento(self):
        return self.__comprimento
        
    @property
    def largura(self):
        return self.__largura
        
    @comprimento.setter
    def comprimento(self, novo_comprimento):
        if novo_comprimento > 0:
            self.__comprimento = novo_comprimento

    @largura.setter
    def largura(self, nova_largura):
        if nova_largura > 0:
            self.__largura = nova_largura

# Criando um obj da classe Retangulo
retangulo = Retangulo(5, 3)

# Acessando a área usando a propriedade 'área'
print(f"Área do retângulo: {retangulo.area}")

# Acessando o comprimento e largura usando as propriedades
print(f"Comprimento: {retangulo.comprimento}")
print(f"Largura: {retangulo.largura}")

# Tentando alterar o valor da área diretamente(não é possível)
# retangulo.area = 20

# Alterando o comprimento e a largura usando as propriedades
retangulo.comprimento = 8
retangulo.largura = 4

# Verificando os novos valores do comprimento e largura
print(f"Novo comprimento: {retangulo.comprimento}")
print(f"Nova largura: {retangulo.largura}")
print(f"Nova área do retângulo: {retangulo.area}")