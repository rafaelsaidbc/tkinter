import tkinter as tk

janela = tk.Tk() #define a janela

janela.title('Janela principal') #define o título da janela
janela['bg'] = 'red' #toda janela é um dicionário, essa variável define o background da janela
janela.geometry('300x300+100+100') #define as dimensões da janela, LarguraxAltura+DistanciaDaEsquerda+DistanciaDoTopo, dimensões em pixels


janela.mainloop() #chama a janela criada, enquanto a janela estiver sendo exibida, executa o mainloop

print('teste')