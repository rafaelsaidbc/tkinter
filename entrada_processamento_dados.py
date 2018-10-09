from tkinter import *


def bt_click():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    soma = num1 + num2
    lb['text'] = soma


janela = Tk()

ed1 = Entry(janela)
ed1.place(x=100, y=100)

ed2 = Entry()
ed2.place(x=100, y=130)

bt = Button(janela, text='SOMA', width=20, command=bt_click)
bt.place(x=100, y=150)

lb = Label(janela, text='Label')
lb.place(x=100, y=200)

janela.geometry('300x300+200+200')
janela.mainloop()
