# Construtores e self 

# __init__(): inicialização de classes(construtor da classe)
# self: parâmetro do construtor 
# método __init__ recebe uma ref. do objeto instanciado como self
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero # indica que o numero é um atributo do objeto
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

def main():
    c1 = Conta(1, 1, "Joao", 1000) # Objeto sendo instanciado ]
    print(f"Nome do titular da conta: {c1.nomeTitular}")
    print(f"Número da conta: {c1.numero}")
    print(f"CPF do titular da conta: {c1.cpf}")
    print(f"Saldo da conta: {c1.saldo}")

# Ao executar um script em Py, a variável reservada NAME ref. a ele tem valor = "__main__"
# Nesse caso, a condição do IF a seguir será TRUE.
# Logo, o que está no corpo do IF será executado(é um chamado ao método main do script)
if __name__ == "__main__":
    main()