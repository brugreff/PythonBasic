# Funções puras e dados imutáveis

# Funções puras - dependem apenas dos parâmetros de entrada p/ gerar uma saída
# Sempre retornam um valor, um objeto ou outra função

# Exemplo 1 - função não pura

#script funcao1.py

valor = 20

# Def função multiplica
# Multipl. a var. global valor por um fator passado como parâmetro
# O valor do resultado é atribuído à var. valor novamente e impresso em seguida
def multiplica(fator):
    global valor
    valor = valor * fator
    print("Resultado", valor)

def main():
    numero = int(input())
    multiplica(numero)
    multiplica(numero)

# Ao executar um script python, a variável reservada NAME referente à ele tem valor igual à "__main__" 
# Nesse caso a cond. IF a seguir será TRUE, então será executado

if __name__ == "__main__":
    main()

# Função não depende apenas dos parâmetros - função multiplica não pura
# Função não retorna valor algum