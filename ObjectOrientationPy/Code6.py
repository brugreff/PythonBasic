# Métodos 

# Ex - depositar dinheiro na conta para aumentar o valor da conta corrente
# Conta tinha um saldo de R$300 após o 1º depósito
# Após chamar sacar(100) o saldo será R$200
# Ao executar o método gerarextrato(), o valor será R$200

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    # Definindo método depositar - recebe a instância do obj por meio do self e de um parâmetro valor
    # O nº passado pelo parâmetro será adicionado ao saldo da conta do cliente
    def depositar(self, valor):
        self.saldo += valor

    # Definindo método sacar - subtração do valor passado como parâmetro, do saldo do cliente.
    def sacar(self, valor):
        self.saldo -= valor

    # Definindo método extrato - avaliar os valores atuais(estado atual do objeto)
    def gerar_extrato(self):
        print(f"numero: {self.numero}\ncpf: {self.cpf}\nsaldo: {self.saldo}")


def main():
    c1 = Conta(1, 1, "Joao", 0)
    c1.depositar(300)
    c1.sacar(100)
    c1.gerar_extrato()

if __name__ == "__main__":
    main()