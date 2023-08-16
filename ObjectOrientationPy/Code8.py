# Encapsulamento: convenção e não restrição rígida
# reunir dados e funções em uma única entidade
# proibir a alteração indevida dos atributos

# ATRIBUTOS PÚBLICOS E PRIVADOS
# ('__atributo'): convenção em Py p/ indicar que o atributo é privado(não deve ser acessado diretamente fora da classe)
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome       # Atributo público
        self.__idade = idade   # Atributo privado
    # get_idade(): método público que permite acessar o atributo privado '__idade'
    def get_idade(self):
        return self.__idade
    # set_idade(): método público que permite atualizar o valor do atributo privado '__idade'
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade

# Criando um objeto da classe Pessoa
pessoa = Pessoa("João", 30)

# Acessando atributos públicos diretamente
print(f"Nome: {pessoa.nome}")

# Acessando atributo privado por meio de método público
print(f"Idade: {pessoa.get_idade()}")

# Tentando acessar o atributo privado diretamente (gerará um erro)
# print(pessoa.__idade)

# Atualizando a idade por meio de método público
pessoa.set_idade(35)
print(f"Nova idade: {pessoa.get_idade()}")