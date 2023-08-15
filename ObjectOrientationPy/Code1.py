# Aplicações da Orientação a Objetos em Py

# Implementando uma Classe
# --------- Classe Pessoa ----------
class Pessoa: # class: sintaxe específica
    def __init__(self, nome, ender): # construtor def # parâmetro self: autoreferência(poder acessar os atributos e métodos de dentro da própria classe)
        self.set_nome(nome) # parâmetro nome(dentro do construtor)
        self.set_ender(ender) # parâmetro endereço(dentro do construtor)


    def set_nome(self, nome): # set_nome: recebe um nome 
        self.nome=nome # atribuição do nome p/ um atributo da própria classe(pois até então era um parâmetro do método)

    def set_ender(self, ender): 
        self.ender=ender # mesmo anterior 

    # get_: retornar um atributo da classe p/ ser manipulado posteriormente 
    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender
    
# ------- Objeto pessoa ----------
# Instanciando a classe
pessoa1 = Pessoa("Maria", "Rua 01234")
pessoa2 = Pessoa("João", "Rua 56789")

# ------ Imprimir cada um dos Objetos --------
print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')