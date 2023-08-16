# Associação entre objetos - Composição
# Criação da classe Extrato 
# armazenar todas as transações realizadas na conta
# conseguir imprimir um extrato com a lista dessas transações 
# foi adicionado um atributo transacoes: inicializado p/ receber um array de valores - transações da conta
class Extrato:
    def __init__(self):
        self.transacoes = []

    def imprimir_extrato(self, numeroconta):
        print(f"Extrato: {numeroconta} \n")
        for p in self.transacoes:
            print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")