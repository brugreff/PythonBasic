# Conceitos gerais de Orientação a Objeto - exemplo aula

# class: define uma classe(classe é um tipo)
# self(ponteiro de autoreferência): sempre presente nos métodos que pertencem à classe - ref do próprio objeto
# __init__: inicializa meu objeto - defino objeto que possui nome e idade como atributos(linha 8 e 9)
class Pessoa:
    def __init__(self, nome, idade): 
        self.nome = nome
        self.idade = idade 

    def imprimir(self):
        print(self.nome, " tem ", self.idade, " ano(s).")
    # get e set: métodos de encapsulamento(controlar o acesso a determinada propriedade)
    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade 

p = Pessoa("Ana", 25)   
p.imprimir()

# ----- Herança -----
class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade) # super(): utiliza o nome e idade def anteriores e acrescenta profissao
        self.profissao = profissao
    def imprimir(self):
        super().imprimir()
        print("\t e trabalha como ", self.profissao)

# ----- Polimorfismo ------
# Enquanto o 'pai' imprimia apenas o nome e a idade, o 'filho' imprime também a profissão
p = Profissional("Ana", 25, "balconista")
p.imprimir()