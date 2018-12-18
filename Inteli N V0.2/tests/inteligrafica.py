from tkinter import *
import time
from functools import partial
from threading import Timer

janela = Tk()

def mudalabel(janela):
    lb['text'] = 'clicou'


bt = Button(janela, width = 17, text = 'Iniciar')
bt.place(x = 320, y = 190)
bt['command'] = partial(mudalabel, janela)

lb = Label(janela, text='label1')
lb.place(x=100,y=200)


janela.title('Inteli N')
janela.geometry('800x600+260+40')
janela['bg'] = 'blue'

janela.mainloop()
