from tkinter import *

janela = Tk()

lb1 = Label(janela, text='Label 1')
bl2 = Label(janela, text='Label 2')

# não importa a linha e coluna definidas se não tiverem outros objetos entre eles. Estarão sempre alinhados à partir do topo e à esquerda
lb1.grid(row=1, column=1)
bl2.grid(row=4, column=3)

janela.geometry('300x300+400+400')

janela.mainloop()
