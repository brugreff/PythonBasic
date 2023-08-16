# Método de Classe x Método Estático

# importar date dentro do pacote datetime 
from datetime import date
class Pessoa:
    def __init__(self, nome, idade): # construtor init
        self.nome = nome
        self.idade = idade
    # Um método de classe para criar 
    # Um objeto Pessoa através do ano de nascimento
    @classmethod
    def apartirAnoNascimento(cls, nome, ano): #cls: fábrica de classes 
        return cls(nome, date.today().year - ano)
    # Método Estático: verificar se é maior de idade 
    @staticmethod
    def ehMaiorIdade(idade): # não recebe cls nem self(não depende do estado da classe) - é geral(não tem relação com um obj específico)
        return idade >= 18 # recebeu parâmetro idade e retorna um resultado V ou F
pessoa1 = Pessoa('Maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('Ana', 2006)
print(pessoa1.idade)
print(pessoa2.idade)
# Imprimir o resultado 
print(Pessoa.ehMaiorIdade(17)) # chamando a partir da classe pessoa(não são os objetos)