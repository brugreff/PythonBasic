#  Associação entre objetos - Composição
# Criação da classe Conta(conta.py modificado)
# a composição Conta->Extrato precisa ser inicializada no construtor da classe Conta
# --- Modificações ---
# linha 17: criação de um atributo extrato, fazendo ref. a um objeto Extrato.
# linhas 22, 29 e 38: adição de linhas ao array de transações do obj Extrato por meio do atributo extrato


import datetime
from extrato import Extrato 

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes 
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPÓSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True    

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contadestino.depositar(valor)
            self.saldo -= valor 
            self.extrato.transacoes.append(["TRANSFERÊNCIA", valor, "Data", datetime.datetime.today()])
            return "Transferência Realizada"
    
    def gerarsaldo(self):
        print(f"numero: {self.numero}\n saldo: {self.saldo}")
        self.extrato.imprimir_extrato(self.numero)