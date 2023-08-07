# MÓDULO TKINTER

# Exemplo 2
# Elemento Label - exibir textos
# Criação do elemento e seu posicionamento
# Tam padrão da janela: 200 x 200 pixels

from tkinter import*

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Hello World")
texto.place(x = 50, y = 100) 
janelaPrincipal.mainloop()