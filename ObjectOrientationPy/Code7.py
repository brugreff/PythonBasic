# Métodos com retorno - retorna um valor a partir da análise do estado do objeto
# Comum na orientação a objetos 

# Saque maior do que o saldo atual do cliente não é permitido
# Resposta: FALSE para o objeto que está executando o saque 

class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
            
    def gerar_extrato(self):
        print(f"numero: {self.numero}\ncpf: {self.cpf}\nsaldo: {self.saldo}")     
        
def main():
    c1 = Conta(1,1,"Joao",0)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerar_extrato()
    print(f"O saque foi realizado? {saque}")
    

if __name__ == "__main__": 
    main()