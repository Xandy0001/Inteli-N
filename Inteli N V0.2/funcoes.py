#Funções Inteli N V0.1
#Imports
#______________________________________________________________________________________________
import pygame
import random
import speech_recognition as sr
import pyttsx3
import datetime
import os
import json
import requests
#______________________________________________________________________________________________

#Listas
#______________________________________________________________________________________________
# Listas fixas para funções
laguarde = ['Só um segundo...', 'Aguarde um pouco...', 'Processando...']
lescultando = ['Na esculta, senhor!', 'Estou te ouvindo...', 'As suas ordens!', 'Estou te escultando!', 'Esperando comando']
lqualmusica = ['Qual música devo tocar?', 'Qual música o senhor deseja?', 'Qual música senhor?']
ldespedidas = ['Tudo bem, até mais', 'Até mais!', 'Ok!', 'Como o senhor quiser!']
lnaoentendi = ['Não entendi...', 'Ainda não tenho esse comando :(', 'Haam?', 'Não entendo...']

#Identificadores:
lpesquisa = ['PESQUISAR', 'FAÇA UMA PESQSUISA', 'PESQUSA', 'PESQUIAA', 'PESQUISA', 'PESQUISE', 'TRADUZA', 'TRADUZIR']
lxingamentosi = ['BOBO', 'BURRO', 'ANIMAL', 'VOCÊ É UM LIXO', 'TE ODEIO', 'VAI TE FERRAR', 'BESTA', 'CALA A BOCA']
lencerra = ['ENCERRAR', 'TCHAU', 'DESLIGAR', 'VAI EMBORA', 'VAZA', 'SAIR', 'SAI']
lcontar = ['FUNCAO CONTA', 'CONTAR', 'CONTE', 'CONTA']
lhorario = ['QUAL É A HORA', 'FALA A HORA', 'QUANTAS HORAS', 'HORÁRIO', 'QUANTAS HORAS SAO', 'HORA', 'DIA É HOJE', 'QUE DIA ESTAMOS', 'DATA', 'DIA', 'TEMPO', 'CLIMA', 'TEMPERATURA', 'INFORMAÇÕES GERAIS', 'INFORMAÇÕES']
lplayer = ['MUSICA', 'MÚSICA', 'MÚSICA', 'PARAR', 'STOP', 'PARE', 'PAUSAR', 'PAUSE', 'VOLUME']
lelogiosi = ['VOCÊ É INCRÍVEL', 'EU TE AMO', 'VOCÊ É DEMAIS', 'VOCÊ É DEMAIS CARA', 'EU TE ADORO', 'TE AMO', 'LINDO']
lfuncaorepetei = ['FUNCAO REPETE', 'FUNÇÃO REPETE', 'REPITA', 'REPETE']
lobrigado = ['OBRIGADO', 'VALEU']
laprende = ['APRENDA', 'APRENDE', 'APRENDER', 'QUERO TE ENSINAR']
lfuncoes = ['O QUE VOCÊ PODE FAZER', 'FUNÇÕES', 'LISTA DE FUNÇÕES', 'VOCÊ PODE FAZER O QUÊ']
#______________________________________________________________________________________________

listas = [lpesquisa, lplayer, lhorario, lfuncaorepetei, lcontar, lelogiosi, lxingamentosi, lobrigado,
          lencerra, laprende, lfuncoes]

#Variaveis para funções
vtimer = 0
vq = 0
vbolean = True
r = sr.Recognizer()
speak = pyttsx3.init('sapi5')
frases = {}
memoria = open('memoria.txt', 'r')
frases = json.load(memoria)
memoria.close()

#Parametros para iniciar:
#______________________________________________________________________________________________________

#______________________________________________________________________________________________________

def funcaopesquisa(v1):

    if len(v1) >= 23 and not 'FAÇA' in v1 and not 'FAZER' in v1:
        if 'PESQUISE' in v1:
            v1 = v1[9:]
        elif 'PESQUISA' in v1:
            v1 = v1[9:]
        elif 'PESQUISAR' in v1:
            v1 = v1[10:]

        if 'NO GOOGLE' in v1:
            v1 = v1[:-10].capitalize()
            v2 = v1
            v1 = f'https://www.google.com/search?q={v1}&oq=explora&aqs=chrome.0.35i39j69i60j69i57j0l3.5124j1j7&sourceid=chrome&ie=UTF-8'
            os.startfile(v1)
            fala(f'Claro, aqui está a pesquisa no Google sobre {v2}')

        elif 'NO YOUTUBE' in v1:
            v1 = v1[:-11].capitalize()
            v2 = v1
            v1 = f'https://www.youtube.com/results?search_query={v1}&page=&utm_source=opensearch'
            os.startfile(v1)
            fala(f'Segue videos relacionados a {v2} no Youtube, senhor"')

        elif 'NO CIFRA CLUB' in v1:
            v1 = v1[:-13].capitalize()
            v2 = v1
            v1 = f'https://www.cifraclub.com.br/?q={v1}'
            os.startfile(v1)
            fala(f'Claro, essas são as cifras relacionadas a {v2} no cifra club!')


    elif 'NO GOOGLE' in v1:
        v1 = funcaoreconhecefacil('O que devo pesquisar no Google senhor?').capitalize()
        if v1 == 'Cancelar' or v1 == 'Sair':
            fala('Tudo bem!')

        else:
            v2 = v1
            v1 = f'https://www.google.com/search?q={v1}&oq=explora&aqs=chrome.0.35i39j69i60j69i57j0l3.5124j1j7&sourceid=chrome&ie=UTF-8'
            os.startfile(v1)
            fala(f'Aqui está a pesquisa no Google sobre {v2}!')

    elif 'YOUTUBE' in v1:
        v1 = funcaoreconhecefacil('O que devo pesquisar no Youtube?').capitalize()
        if v1 == 'Cancelar' or v1 == 'Sair':
            fala('Tudo bem, como quiser!')

        else:
            v2 = v1
            v1 = f'https://www.youtube.com/results?search_query={v1}&page=&utm_source=opensearch'
            os.startfile(v1)
            fala(f'Segue videos relacionados a "{v2} no Youtube, senhor"')

    elif 'CIFRA CLUB' in v1:
        v1 = funcaoreconhecefacil('Tudo bem, qual pesquisa devo fazer no cifra club senhor?').capitalize()
        if v1 == 'Cancelar' or v1 == 'Sair':
            fala('Tudo bem, como quiser!')
        else:
            v2 = v1
            v1 = f'https://www.cifraclub.com.br/?q={v1}'
            os.startfile(v1)
            fala(f'Claro, segue cifras relacionadas a "{v2}" no Cifra Club, senhor.')

    elif 'TRADUZA' in v1 or 'TRADUZIR' in v1:
        if 'TRADUZIR' in v1:
            v1 = v1[8:]
        elif 'TRADUZA' in v1:
            v1 = v1[7:].capitalize()

        os.startfile(f'https://translate.google.com.br/?source=osdd#view=home&op=translate&sl=auto&tl=pt&text={v1}')
        fala(f'Claro, aqui está a tradução para o português de {v1} no Google Tradutor!')

    else:
        v1 = funcaoreconhecefacil('Claro, o que devo pesquisar senhor?').capitalize()
        if v1 == 'Cancelar' or v1 == 'Sair':
            fala('Tudo bem!')

        else:
            v2 = v1
            v1 = f'https://www.google.com/search?q={v1}&oq=explora&aqs=chrome.0.35i39j69i60j69i57j0l3.5124j1j7&sourceid=chrome&ie=UTF-8'
            os.startfile(v1)
            fala(f'Aqui está a pesquisa sobre {v2}, senhor')


def funcaoconta(v1):
    global vtimer
    vtimer = 0
    vbolean = True

    while vbolean == True:
        if 'ATÉ' in v1:
            v1 = v1[10:].strip()

        else:
            v1 = funcaoreconhecefacil('\nAté quanto devo contar?')

        if 'ate' in v1.lower() or 'até' in v1.lower():
            v1 = v1[4:]

        if v1.isnumeric():
            v1 = int(v1)
            while vtimer < v1:
                vtimer = vtimer + 1
                print(vtimer)
                fala(vtimer)

                if vtimer == v1:
                    print('\033[32m\nTerminei, senhor!\033[m')
                    fala('Terminei, senhor!')
                    vbolean = False

        elif v1 == 'sair' or v1 == 'cancelar' or v1 == 'sai' or v1 == 'voltar':
            print('Tudo bem senhor, voltando!')
            fala('Tudo bem senhor, voltando!')
            vbolean = False

        else:
            print('\033[31mDiga um número inteiro!\033[m')
            fala('Diga um número inteiro!')


def player(v1):
    global vbolean
    vbolean = True

    while vbolean == True:
        global vq
        global musicanapasta
        vq = True
        v1 = v1.lower()
        vbolean = True
        if 'volume' in v1:

            while vbolean == True:
                v1 = funcaoreconhecefacil('Qual volume voçê deseja senhor?')

                if 'auto' in v1 or 'alto' in v1:
                    v1 = 5.0
                    vbolean = False

                elif 'baixo' in v1:
                    v1 = 0.1
                    vbolean = False

                elif 'médio' in v1 or 'medio' in v1:
                    v1 = 0.4
                    vbolean = False

                elif v1.upper() == 'SAIR' or v1.upper() == 'NENHUM' or v1.upper() == 'SAÍR' or v1.upper() == 'CANCELAR':
                    vbolean = False
                    print('\033[32mTudo bem\033[m')
                    fala('Tudo bem')

                else:
                    print('\033[33m\nDiga "alto" "médio" ou "baixo"!\033[m')
                    fala('Diga "alto", "médio", ou "baixo"!')

            if vq:
                pygame.mixer.music.set_volume(v1)
                vq = False
                vbolean = False
                print('\033[33mVolume redefinido!\033[m')
                fala('Volume redefinido')

        elif 'parar' in v1 or 'stop' in v1:
            pygame.mixer.music.stop()
            vbolean = False
            print('\033[33mParando música...\033[m')
            fala('Parando música...')

        elif 'pausar' in v1 or 'pause' in v1:
            pygame.mixer.music.pause()
            vbolean = False
            print('\033[33mPausando música...\033[m')
            fala('Pausando música...')

        elif 'voltar' in v1 or 'continuar' in v1:
            pygame.mixer.music.unpause()
            vbolean = False
            print('\033[32mVoltando música...\033[m')
            fala('Voltando música...')

        elif v1 == 'recomecar' or v1 == 'de novo' or 'recomeçar' in v1:
            pygame.mixer.music.play()
            vbolean = False
            print('\033[33mRecomeçando música...\033[m')
            fala('Recomeçando música...')

        elif 'qualquer' in v1 or 'aleatória' in v1:
            lmusicas = loadmusics()
            if musicanapasta == True:
                v1 = random.choice(lmusicas)
                pygame.mixer.init()
                pygame.mixer.music.load('musicas\{}' .format(v1))
                pygame.mixer.music.play()
                vbolean = False
                v1 = v1[0:-4]
                print(f'Claro, tocando {v1}!')
                fala(f'Claro, tocando {v1}!')

            else:
                print('Aparentemente o diretorio de música está vazio!')
                fala('Aparentemente o diretorio de música está vazio!')
                vbolean = False

        else:
            lmusicas = loadmusics()
            v1 = random.choice(lqualmusica)
            if musicanapasta:
                v1 = funcaoreconhecefacil(v1)

                if v1 == 'aleatoria' or v1 == 'aleatório' or v1 == 'qualquer uma' or v1 == 'aleatória':
                    v1 = random.choice(lmusicas)
                    pygame.mixer.init()
                    pygame.mixer.music.load('musicas\{}'.format(v1))
                    pygame.mixer.music.play()
                    vbolean = False
                    v1 = v1[0:-4]
                    print(f'Claro, tocando {v1}!')
                    fala(f'Claro, tocando {v1}!')

                elif v1 in lmusicas:
                    pygame.mixer.init()
                    pygame.mixer.music.load('musicas\{}'.format(v1))
                    pygame.mixer.music.play()
                    vbolean = False
                    print('\033[1;32mTocando...\033[m')
                    fala('Tocando')

                elif v1.upper() == 'SAIR' or v1.upper() == 'NENHUMA' or v1.upper() == 'NADA' or v1.upper() == 'SAÍR' or v1.upper() == 'CANCELAR':
                    vbolean = False
                    print('\033[32mTudo bem\033[m')
                    fala('Tudo bem')

                else:
                    print('\n\033[31mNão identifiquei essa música, tente outra!\033[m')
                    fala('Não identifiquei essa música, tente outra!')

            else:
                print('Aparentemente o diretorio de música está vazio!')
                fala('Aparentemente o diretorio de música está vazio!')
                vbolean = False


def funcaoreconhecimentodevoz():
    vbolean = True

    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)

        print('\033[1;32m\nEsperando me chamar...\033[m')
        while vbolean:

            audio = r.listen(s)
            try:
                v1 = r.recognize_google(audio, language='pt-BR')
                print(random.choice(laguarde))
                vbolean = False
            except sr.UnknownValueError:
                print('\033[31mNão entendo seu audio...\033[m')
                print('\033[1;32m\nEsperando me chamar...\033[m')
            except sr.RequestError as e:
                print('\033[7;31mErro ao conectar a nuvem...; {}\033[m'.format(e))
                print('\033[1;32m\nEsperando me chamar...\033[m')

        return v1.upper()


def funcaoreconhecefacil(v1):
    global r
    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)
        vbolean = True

        while vbolean == True:
            print(f'\033[33m\n{v1}\033[m')
            fala(v1)
            audio = r.listen(s)
            print(random.choice(laguarde))
            try:
                v1 = r.recognize_google(audio, language='pt-BR')
                vbolean = False

            except sr.UnknownValueError:
                print('\033[31mNão entendo seu audio...\033[m')
            except sr.RequestError as e:
                print('\033[7;31mErro ao conectar a nuvem...; {}\033[m'.format(e))

    return(v1)


def funcaohorario(v1):
    v1 = v1.lower()

    cidade = 'contagem'

    tempo = json.loads(requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=49b5fba2a15189d1bcd687f6d055106e').text)

    med = tempo['main']['temp'] - 273.15
    min = tempo['main']['temp_min'] - 273.15
    max = tempo['main']['temp_max'] - 273.15
    nuvens = tempo['weather'][0]['description']

    chuva = False

    # Traduzindo:
    if nuvens == 'clear sky':
        nuvens = 'céu limpo'
    elif nuvens == 'broken clouds':
        nuvens = 'nuvens quebradas'
    elif nuvens == 'overcast clouds':
        nuvens = 'nuvens nubladas'
    elif nuvens == 'few clouds':
        nuvens = 'poucas nuvens'
    elif nuvens == 'scattered clouds':
        nuvens = 'nuvens dispersas'
    elif nuvens == 'smoke':
        nuvens = 'nuvens baixas'
    elif nuvens == 'light rain':
        nuvens = 'chuva leve'
    elif nuvens == 'shower rain':
        nuvens = 'leves pancadas de chuva'
    elif nuvens == 'heavy intensity rain':
        nuvens = 'chuva pesada'
    elif nuvens == 'light snow':
        nuvens = 'pouca neve'

    if 'tempo' in v1 or 'temperatura' in v1 or 'clima' in v1:

        print(f'Atualmente em {cidade} estamos com {nuvens}\
, e a temperatura média é de {med:.0f} graus, \ncom mínima de {min:.0f}, e máxima de {max:.0f}!')
        fala(f'Atualmente em {cidade} estamos com {nuvens}\
, e a temperatura média é de {med:.0f} graus, \ncom mínima de {min:.0f}, e máxima de {max:.0f}!')

    elif 'dia' in v1 or 'data' in v1:
        print(f'\nEstamos no dia \033[32m{datetime.datetime.now().day}\033[m do \033[32m{datetime.datetime.now().month}\033[m do ano de \033[32m{datetime.datetime.now().year}\033[m!')
        fala(f'\nEstamos no dia {datetime.datetime.now().day} do {datetime.datetime.now().month} do ano de {datetime.datetime.now().year}!')

    elif 'horas' in v1 or 'horário' in v1:
        print(f'\nSão \033[33m{datetime.datetime.now().hour}\033[m horas e \033[33m{datetime.datetime.now().minute}\033[m minutos.')
        fala(f'\nSão {datetime.datetime.now().hour} horas e {datetime.datetime.now().minute} minutos.')

    elif 'informações' in v1:
        print(f'Claro, são {datetime.datetime.now().hour} horas e {datetime.datetime.now().minute} minutos do dia {datetime.datetime.now().day} do {datetime.datetime.now().month} do ano de {datetime.datetime.now().year}!')
        fala(f'Claro, são {datetime.datetime.now().hour} horas e {datetime.datetime.now().minute} minutos do dia {datetime.datetime.now().day} do {datetime.datetime.now().month} do ano de {datetime.datetime.now().year}!')

        print(f'Atualmente em {cidade} estamos com {nuvens}\
, e a temperatura média é de {med:.0f} graus, \ncom mínima de {min:.0f}, e máxima de {max:.0f}!')
        fala(f'Atualmente em {cidade} estamos com {nuvens}\
, e a temperatura média é de {med:.0f} graus, \ncom mínima de {min:.0f}, e máxima de {max:.0f}!')


def funcaorepete():
    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s)
        vbolean = True
        print('\033[32m\nÉ só dizer que eu repito senhor!\033[m')
        fala('É só dizer que eu repito, senhor!')

        while vbolean == True:
            print('\nOuvindo')
            audio = r.listen(s)
            print(random.choice(laguarde))
            try:
                v1 = r.recognize_google(audio, language='pt-BR')

                if v1.upper() == 'CANCELAR' in v1.upper() or 'SAÍR' in v1.upper() or 'SAIR' in v1.upper() or 'PARAR' in v1.upper() or 'PARE' in v1.upper() or 'PARA' in v1.upper():
                    print('\nTudo bem, saíndo senhor!')
                    fala('Tudo bem, saindo senhor!')
                    vbolean = False

                else:
                    print(v1)
                    fala(v1)

            except sr.UnknownValueError:
                print('\033[31mNão entendo seu audio...\033[m')
            except sr.RequestError as e:
                print('\033[7;31mErro ao conectar a nuvem...; {}\033[m'.format(e))


def loadmusics():
    vbolean = True
    v = 0
    global musicanapasta
    lmusicas = []
    for lmusicas in os.walk('musicas'):
        print('Carregando lista de músicas...')
    lmusicas = lmusicas[2]

    while vbolean:
        v1 = lmusicas[v]
        if not '.mp3' in v1:
            del lmusicas[v]
            v = 0
        if v == len(lmusicas) - 1:
            vbolean = False
        if v < len(lmusicas) - 1:
            v = v + 1
        musicanapasta = True

    if len(lmusicas) <= 4:
        print('Nenhuma música encontrada')
        musicanapasta = False

    return lmusicas


def reconhececomando(v1):
    frase = v1
    vbolean = True
    v1 = 0
    v2 = 0
    variavelencontrada = 0

    while vbolean:
        len1 = len(listas) -1
        len2 = len(listas[v1]) -1
        v = listas[v1][v2]

        if v in frase:
            vbolean = False
            variavelencontrada = v1

        elif v1 == len1 and v2 == len2:
            vbolean = False
            variavelencontrada = 'nd'

        elif v2 == len2:
            v1 += 1
            v2 = 0

        else:
            v2 += 1

    return variavelencontrada


def encerra(v1, janela):
    encerra = False
    if v1 == 'ENCERRAR AGORA':
        encerra = True
        v1 = random.choice(ldespedidas)
        print(v1)
        fala(v1)
        janela.quit()

    else:
        v1 = funcaoreconhecefacil('Devo mesmo encerrar?').upper()

        if v1 == 'SIM' or v1 == 'SS' or v1 == 'S' or v1 == 'DEVE':
            encerra = True
            v1 = random.choice(ldespedidas)
            print(v1)
            fala(v1)

        else:
            fala(v1)

    return encerra


def aprende():
    vbolean = True

    while vbolean:
        pergunta = funcaoreconhecefacil('Claro, o que devo aprender senhor?').upper()

        if pergunta == 'CANCELAR' or pergunta == 'SAIR':
            vbolean = False
            fala('Está bem...')

        else:
            resposta = funcaoreconhecefacil('Como devo responder a isso senhor? ').upper()

            if resposta == 'CANCELAR' or resposta == 'SAIR':
                vbolean = False
                fala('Tudo bem, saindo...')

            else:
                vbolean = False
                frases[pergunta] = resposta
                memoria = open('memoria.txt', 'w')
                json.dump(frases, memoria)
                memoria.close()
                fala('Está bem, quando me perguntar responderei!')


def fala(frase):
    speak.say(frase)
    speak.runAndWait()


def funcaoelse(v1, frases):
    if v1 in frases:

        v1 = frases[v1]

        if 'EXECUTAR' in v1 or 'ABRIR' in v1:
            if 'EXECUTAR' in v1:
                v1 = v1[9:].lower()
                os.startfile(v1)
                fala(f'Claro, abrindo {v1[:-4]}')

            elif 'ABRIR' in v1:
                v1 = v1[6:].lower()
                os.startfile(v1)
                fala(f'Claro, abrindo {v1[4:]}')

        else:
            fala(v1)

    else:
        v1 = random.choice(lnaoentendi)
        print(f'\033[31m{v1}\033[m')
        fala(v1)
