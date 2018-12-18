nomes = ['xandy', 'alex', 'roberto', 'pedro', 'jao', 'eticia']
lplayer = ['MUSICA', 'MÚSICA', 'MÚSICA', 'PARAR', 'STOP', 'toddy', 'PARE', 'PAUSAR', 'PAUSE', 'VOLUME']
outra = ['carro', 'casa', 'animal', 'teste']
outra2 = ['aviao', 'telhado', 'carrinho', 'caminhao']
outras3 = ['iosfhsa', 'fhais']

listas = [nomes, lplayer, outra, outra2]

while True:
    frase = input('Frase: ')
    vbolean = True

    v1 = 0
    v2 = 0
    variavelencontrada = 0

    while vbolean:
        len1 = len(listas) - 1
        len2 = len(listas[v1]) - 1

        v = listas[v1][v2]

        if v in frase:
            print('Encontrado')
            vbolean = False
            variavelencontrada = v1

        elif v1 == len1 and v2 == len2:
            vbolean = False
            print('Não encontrado')

        elif v2 == len2:
            v1 += 1
            v2 = 0

        else:
            v2 += 1

    print(variavelencontrada)
