# exemplo com labels e botões funcionais
from tkinter import *


# define uma função para o botão
def bt_click():
    print('bt_click')

    # altera o atributo text da variável lb
    lb['text'] = 'Funciona'


janela = Tk()

# cria um botão, command define uma função a ser executada quando o botão for clicado
bt = Button(janela, width=20, text='OK', command=bt_click)
# define a localização do botão
bt.place(x=100, y=100)

# cria um label com a variável lb
lb = Label(janela, text='Teste')
# define a localização de lb
lb.place(x=100, y=150)

janela.geometry('300x300+200+200')
janela.mainloop()
