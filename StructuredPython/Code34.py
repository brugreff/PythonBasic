# Tratamento completo das exceções

try:
    Bloco 1
except Exception1:
    Bloco tratador para Exception1
except Exception2:
    Bloco tratador para Exception2
...
else:
    Bloco 2 - executado caso nenhuma exceção seja levantada
finally:
    Bloco 3 - executado independente do que ocorrer
Instrução fora do try/except