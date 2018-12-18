import os
import pygame
import random
import time

for lmusicas in os.walk('musicas'):
    print('Carregando lista de músicas...')
lmusicas = lmusicas[2]

vbolean = True
v = 0
v1 = 0

while vbolean:
    print(v)
    v1 = lmusicas[v]
    if not '.mp3' in v1:
        del lmusicas[v]
        v = 0
    if v == len(lmusicas) - 1:
        vbolean = False
    if v < len(lmusicas) - 1:
        v = v +1
    print(v1)
    print(lmusicas)

print(lmusicas)


'''pygame.mixer.init()
pygame.mixer.music.load('musicas\{}' .format(v1))
pygame.mixer.music.play()

time.sleep(10)'''
