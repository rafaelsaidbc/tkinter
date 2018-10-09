from tkinter import *

janela = Tk()

# atribui uma instância label a uma variável, nesse caso lb
lb = Label(janela, text='Fala galera!!')
# define a localização de lb
lb.place(x=100, y=100)

# largura x altura x distanciaEsquerda x distanciaTopo
janela.geometry('300x300+200+200')

janela.mainloop()
