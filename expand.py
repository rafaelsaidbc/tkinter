from tkinter import *

janela = Tk()

lb1 = Label(janela, text='Linha 1', bg='red')
lb2 = Label(janela, text='Linha 2', bg='white')
lb3 = Label(janela, text='Linha 3', bg='black')

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry('500x200+600+200')

janela.mainloop()
