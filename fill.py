from tkinter import *

janela = Tk()

lb1 = Label(janela, text='horizontal', bg='red')
lb2 = Label(janela, text='FLA', bg='black')
lb3 = Label(janela, text='FLA', bg='black')

lb1.pack(side=TOP, fill=X)  # x = horizontal, y = vertical
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)

janela.geometry('500x200+600+200')

janela.mainloop()
