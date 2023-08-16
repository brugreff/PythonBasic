# Associação entre objetos - Agregação
# Parte 1 - Criar classe Cliente

# --- Classe Cliente ---
class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome 
        self.endereco = endereco