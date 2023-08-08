# Exceções de múltiplos tipos
# Py permite diversos tratamentos p/ diferentes tipos possíveis de execução
# Mais de uma cláusula except para a mesma cláusula try

try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")