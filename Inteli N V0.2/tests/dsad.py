import speech_recognition as sr
import pyaudio
import pyttsx3
import json

vbolean = True
frases = {}
memoria = open('memoria.txt', 'r')
frases = json.load(memoria)
memoria.close()

while vbolean:

    v1 = input('Comando: ')
    
    if v1.upper() == 'APRENDA':
        pergunta = input('Qual é a pergunta? ')
        resposta = input('Qual é a resposta? ')
        frases[pergunta] = resposta
        memoria = open('memoria.txt', 'w')
        json.dump(frases,memoria)
        memoria.close()

    elif v1 in frases:
        print(frases[a])

    else:
        print('Não tenho esse comando')