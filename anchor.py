from tkinter import *

janela = Tk()

lb1 = Label(janela, text='SIDE 1', bg='white')
lb2 = Label(janela, text='SIDE 2', bg='red')
lb3 = Label(janela, text='ANCHOR 1', bg='white')
lb4 = Label(janela, text='ANCHOR 2', bg='red')

# não omitir a propriedade LEFT, senão o Python assume que é TOP
lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(anchor=NW)
lb4.pack(anchor=SW)

janela['bg'] = 'black'
janela.geometry('400x300+200+200')
janela.mainloop()
