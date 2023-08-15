# Agregação - exemplo aula

# ---- Classe Salário ----
class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus 
    def salario_anual(self):
        return (self.base*12)+self.bonus
    
# ---- Classe Empregado ----
class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario # Agregação(gancho com classe Salario)
    def salario_total(self):
        return self.salario_agregado.salario_anual()
    
# Chamada para as classes (como elas irão interagir entre si)
salario = Salario(10000, 700) # instanciar objeto da classe Salario e seus atributos(def __init__: base, bonus)
emp = Empregado('Musashi', 46, salario) # instanciou objeto da classe Empregado e atributos(nome, idade, salario) - salário é obj da classe Salário - relacionou ambas classes
print(emp.salario_total())