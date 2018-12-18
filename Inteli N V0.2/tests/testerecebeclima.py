import requests
import json

cidade = 'contagem'

tempo = json.loads(requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid=49b5fba2a15189d1bcd687f6d055106e').text)

med = tempo['main']['temp']-273.15
min = tempo['main']['temp_min']-273.15
max = tempo['main']['temp_max']-273.15
nuvens = tempo['weather'][0]['description']

chuva = False

#Traduzindo:
if nuvens == 'clear sky':
    nuvens = 'céu limpo'
    chuva = False
elif nuvens == 'broken clouds':
    nuvens = 'nuvens quebradas'
    chuva = False
elif nuvens == 'overcast clouds':
    nuvens = 'nuvens nubladas'
    chuva = False
elif nuvens == 'few clouds':
    nuvens = 'minimas'
    chuva = False
elif nuvens == 'scattered clouds':
    nuvens = 'nuvens dispersas'
    chuva = False
elif nuvens == 'smoke':
    nuvens = 'nuvens baixas'
    chuva = False
elif nuvens == 'light rain':
    nuvens = 'chuva leve'
    chuva = True
elif nuvens == 'shower rain':
    nuvens = 'leves pancadas de chuva'
    chuva = True
elif nuvens == 'heavy intensity rain':
    nuvens = 'chuva pesada'
    chuva = True
elif nuvens == 'light snow':
    nuvens = 'pouca neve'
    chuva = True


if chuva == True:
    print(f'Atualmente estamos com {nuvens}\
, e a temperatura média é de {med:.0f} graus, \ncom minima de {min:.0f}, e maxima de {max:.0f}!')

else:
    print(f'Atualmente estamos com {nuvens}\
, e a temperatura média é de {med:.0f} graus, \ncom minima de {min:.0f}, e maxima de {max:.0f}!')
