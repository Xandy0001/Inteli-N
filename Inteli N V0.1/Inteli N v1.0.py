# Informações
versaointeliN = '0.1 N'
sobre = f'\nInteli N versão {versaointeliN}; \nO Inteli N tem base na versão "1.3 Beta" do Inteli! \nVarias funcões adicionadas. \nBugs corrigidos \nFução "aprende"/Memória adicionada \nPasta para músicas \nMain simplificado \nFuncão pesquisa reformulada \nInicio de desenvolvimento de interface gráfica. \n\n~A.Rubens'

# Imports
import random
import funcoes
import pyttsx3
import time
import tkinter as tk
import json
import os

print(f'\033[4;34m\nInteli V{versaointeliN}\033[m\n\n')

# Variaveis
encerra = False
v = True
speak = pyttsx3.init('sapi5')
frases = {}

# Listas fixas:
#_____________________________________________________________________________________________________________________
# Prints:
lsaudacoes = ['Ao seu comando, senhor! ', 'Olá, senhor! ', 'Ao seu comando, senhor!', 'Iniciando', 'Olá senhor, estou pronta!']
lxingamentos = ['Que isso...', 'Pô cara, nunca te fiz nada...', 'Jesus te ama!', 'Isso você tem que falar para o meu desenvolvedor!']
lelogios = ['Aaahhhh... Eu te adoro muitooo!', 'Você é demais!', 'Senhor, você é incrível!']
ldenada = ['Por nada, senhor!', 'De nada, senhor', 'Não há de que, senhor!', 'Por nada, apenas cumpro minha função...', 'Por nada!']
#_____________________________________________________________________________________________________________________

def inteliN():

    #Parâmetros de inicialização:
    #___________________________________________________________________________________________________________
    janela.update_idletasks()
    janela.update()

    frase = random.choice(lsaudacoes)
    print(f'\033[1;36m{frase}\033[m')
    #speak.setProperty('voice',b'brazil')
    funcoes.fala(frase)
    #___________________________________________________________________________________________________________

    encerra = False
    while encerra != True:
        lb['text'] = 'Esperando me chamar...'
        lb.place(x=300, y=270)
        janela.update()

        v1 = funcoes.funcaoreconhecimentodevoz().upper().strip()
        comando = funcoes.reconhececomando(v1)

        if comando == 0:
            lb['text'] = 'Pesquisa'
            lb.place(x=330, y=270)
            janela.update()
            funcoes.funcaopesquisa(v1)

        elif comando == 1:
            lb['text'] = 'Música'
            lb.place(x=340, y=270)
            janela.update()
            funcoes.player(v1)

        elif comando == 2:
            lb['text'] = 'Hora/Data'
            lb.place(x=330, y=270)
            janela.update()
            funcoes.funcaohorario(v1)

        elif comando == 3:
            lb['text'] = 'Repete'
            lb.place(x=330, y=270)
            janela.update()
            funcoes.funcaorepete()

        elif comando == 4:
            lb['text'] = 'Contar'
            lb.place(x=330, y=270)
            janela.update()
            funcoes.funcaoconta(v1)

        elif comando == 5:
            lb['text'] = ':)'
            lb.place(x=350, y=270)
            janela.update()
            v1 = random.choice(lelogios)
            print(v1)
            funcoes.fala(v1)

        elif comando == 6:
            lb['text'] = ': |'
            lb.place(x=350, y=270)
            janela.update()
            v1 = random.choice(lxingamentos)
            print(v1)
            funcoes.fala(v1)

        elif comando == 7:
            lb['text'] = ';)'
            lb.place(x=350, y=270)
            janela.update()
            funcoes.fala(random.choice(ldenada))

        elif comando == 8:
            lb['text'] = 'Encerrar'
            lb.place(x=330, y=270)
            janela.update()
            encerra = funcoes.encerra(v1, janela)

        elif v1 == 'SOBRE' or v1 == 'VERSAO' or v1 == 'VERSÃO':
            print(f'\033[4m{sobre}\033[m')
            time.sleep(3)

        elif comando == 9:
            lb['text'] = 'Aprendendo...'
            lb.place(x=320, y=270)
            janela.update()
            funcoes.aprende()

        elif comando == 10:
            lb['text'] = 'Minhas funções'
            lb.place(x=330, y=270)
            os.startfile('minhasfuncoes.txt')
            funcoes.fala('Bem, aqui está uma lista das minhas funções!')

        else:
            memoria = open('memoria.txt', 'r')
            frases = json.load(memoria)
            memoria.close()
            lb['text'] = '...'
            lb.place(x=350, y=270)
            janela.update()
            funcoes.funcaoelse(v1, frases)


janela = tk.Tk()
janela.title('Inteli N')
janela['bg'] = 'black'
janela.geometry('720x480+420+100')

imagem = tk.PhotoImage(file='images.png')
w = tk.Label(janela, image=imagem)
w.place(x=0,y=0,relwidth = 1.0, relheight = 1.0)

lb = tk.Label(janela, text = 'Inteli N')
lb.place(x = 340, y = 270)

inteliN()
