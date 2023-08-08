# MÓDULO TKINTER

# Acrescentando uma imagem e botão
# OBS: Imagem precisa estar na mesma pasta do arquivo.py

from tkinter import * # módulo principal
from tkinter import messagebox # submódulo 

# Função funcClicar() - funcionamento correto do botão
# Serve apenas para imprimir na tela a string "Purr"
def funcClicar():
    messagebox.showinfo("Sofia:", "Purr")
    #print("Purr")
   

janelaPrincipal = Tk()
janelaPrincipal.title("Sofia")
texto = Label(master = janelaPrincipal, text = "Hi, I'm Sofia")
texto.pack()

# Criação do objeto Label p/ conter a imagem e seu posicionamento
# Método pack(): centraliza o elemento, posiciona o mais próx possível do topo, depois dos elem. já posicionados
pic = PhotoImage(file = "StructuredPython/Tkinter/testcat.png") # Caminho a partir da raiz do meu projeto(VS Code)
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

# Criação do elemento botão, com atributos text e command
# Texto exibido no corpo do botão e função a ser executada ao clicar
botao = Button(master = janelaPrincipal, text = 'Pet me', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()