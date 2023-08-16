# Associação entre objetos - Agregação 
# Parte 3 - Criação de um programa p/ ser usado na instanciação dos objetos das duas classes(Cliente e Contas)
# Gerar as transações realizadas nas contas dos clientes(conta conjunta)

from conta import Conta
from cliente import Cliente 
cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria", "Rua 2")
conta1 = Conta([cliente1, cliente2], 1, 0)
conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()