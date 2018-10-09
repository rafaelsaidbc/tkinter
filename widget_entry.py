from tkinter import *


# função define evento do botão, que troca o text do label para o que for digitado pelo usuário
def bt_onclick():
    print(ed.get())
    lb['text'] = ed.get()

janela = Tk()

ed = Entry(janela)
ed.place(x=100, y=100)

bt = Button(janela, width=20, text='OK', command=bt_onclick)
bt.place(x=100, y=150)

lb = Label(janela, text='Label')
lb.place(x=100, y=200)

janela.geometry('300x300+200+200')
janela.mainloop()
