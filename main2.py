from os import system
import time
import random  # Importamos random para numeros al azar
import platform
import operator
from operator import itemgetter

# COMPATIBILIDAD DE SISTEMA OPERATIVO ========================================

sistema = platform.system()
SO=sistema  

usuario = ''
puntaje = 0


def limpiar():
    if SO == 'Windows':
        system('cls')
    elif SO == 'Darwin' or SO == 'Linux':
        system('clear')

def pausa():
    if SO == 'Windows':
        system('pause')
    elif SO == 'Darwin' or SO == 'Linux':
        input('Presione enter para continuar...')

def colores(color):
    if color == 'rojo':
        if SO == 'Windows':
            system('color 4')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 1')
    elif color == 'verde':
        if SO == 'Windows':
            system('color 2')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 2')
    elif color == 'amarillo':
        if SO == 'Windows':
            system('color 6')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 3')
    elif color == 'celeste':
        if SO == 'Windows':
            system('color 3')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 6')
    elif color == 'azul':
        if SO == 'Windows':
            system('color 1')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 4')
    elif color == 'morado':
        if SO == 'Windows':
            system('color 5')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 5')
    elif color == 'blanco':
        if SO == 'Windows':
            system('color 7')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 7')
    elif color == 'gris':
        if SO == 'Windows':
            system('color 8')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 8')

def inf_colores():
    if SO == 'Windows':
        print('''0 = Negro       
1 = Azul        
2 = Verde
3 = Celeste
4 = Rojo
5 = Púrpura
6 = Amarillo
7 = Blanco
8 = Gris''')

    elif SO == 'Darwin' or SO == 'Linux':
        print('''1. Rojo
2. Verde
3. Amarillo
4. Azul
5. Morado
6. Celeste
7. Blanco
8. Gris''')

h1 = ['  __   ','  __   ','  ___  ','  __   ',' _  _ ','  ___  ','  ___  ','  ___  ','   ___  ','  ___  '] 
h2 = [' /  \\  ',' /  |  ',' (_  | ',' |__`. ','| || |',' | __| ',' / __| ',' |_  | ','  / _ \\ ',' / _ \\  ']
h3 = ['| // | ',' `7 |  ','  / /  ','  |_ | ','`._  _|',' `._`. ','| ,_ \\ ','  / /  ',' ) _ ( ',' \__ / ']
h4 = [' \__/  ','  |_|  ',' |___| ',' |__.\' ','   |_| ',' !__.\' ',' \___/ ',' |_/   ',' \___/ ','  /_/  ']


def numero(numero):
  if len(str(numero))==1:
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = numero
  elif len(str(numero))==2:
    n1 = 0
    n2 = 0
    n3 = int(str(numero)[0])
    n4 = int(str(numero)[1])
  elif len(str(numero))==3:
    n1 = 0
    n2 = int(str(numero)[0])
    n3 = int(str(numero)[1])
    n4 = int(str(numero)[2])

  elif len(str(numero))==4:
    n1 = int(str(numero)[0])
    n2 = int(str(numero)[1])
    n3 = int(str(numero)[2])
    n4 = int(str(numero)[3])
  print('\t\t\t\t\t\t\t'+"\033[1;101;93m"+'           PUNTUACION            '+"\033[0m")
  print('\t\t\t\t\t\t\t'+"\033[1;101;93m",h1[n1],h1[n2],h1[n3],h1[n4],"\033[0m")
  print('\t\t\t\t\t\t\t'+"\033[1;101;93m",h2[n1],h2[n2],h2[n3],h2[n4],"\033[0m")
  print('\t\t\t\t\t\t\t'+"\033[1;101;93m",h3[n1],h3[n2],h3[n3],h3[n4],"\033[0m")
  print('\t\t\t\t\t\t\t'+"\033[1;101;93m",h4[n1],h4[n2],h4[n3],h4[n4],"\033[0m")

def lee_entero(txt):
   while True:
       entrada = input(txt)
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:   
           print("La entrada es incorrecta: escribe un numero entero")

def lee_float(txt):
   while True:
       entrada = input(txt)
       try:
           entrada = float(entrada)
           return entrada
       except ValueError:
           print("La entrada es incorrecta: escribe un numero")
# ============================================================================

system('color 2')
limpiar()
# LETRAS ASCII
# http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=VICTORIA!!!%0A
from pygame import mixer
mixer.init()
#mixer.music.load('\music\init.mp3')
limpiar()
def rint(txt,error):
    while True:
        try:
            str = int(input(txt))
            return str
        except ValueError:
            print(error)
#mixer.music.play()
mixer.music.set_volume(0.25)
limpiar()
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  

''')
time.sleep(1)
limpiar()
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  ██ 

''')
time.sleep(1)
limpiar()
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  ██ ██ 

''')
time.sleep(1)
limpiar()
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  ██ ██ ██ 

''')
time.sleep(2)
import random
for i in range(100):
    for j in range(150):
        r=random.randint(0,1)
        print(r,end='')
    print()
limpiar()
mixer.music.stop()

# ****************************************************************
# ***********************  AHORCADO  *****************************
# ****************************************************************
# Tablero de Juego
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

# Preguntas
pregCiencia = []

# Respuestas
resCiencia = []

errores = 0  # Numero de veces que se equivoco el usuario

linea = []  # Lista donde estaran _ _ _ _ _ _ ...

# *****************************************************************


limpiar()

continuar = True

while continuar == True:
    limpiar()
    mixer.music.load('music/main.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.4)
    colores('celeste')
    print('''

______██████████████
-____██▓▓▓▓▓▓▓▓▓ M ▓████
-__██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
-__██████░░░░██░░██████
██░░░░████░░░██░░░░░░░░██
██░░░░████░░░░██░░░░░░░██
-__████░░░░░░██████████         ██████╗ ██╗███████╗ █████╗      ██████╗  █████╗ ███╗   ███╗███████╗███████╗
-__██░░░░░░░░░░░░░██            ██╔══██╗██║██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝
_____██░░░░░░░░░██              ██████╔╝██║███████╗███████║    ██║  ███╗███████║██╔████╔██║█████╗  ███████╗
-______██░░░░░░██               ██╔═══╝ ██║╚════██║██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║
-____██▓▓████▓▓▓█               ██║     ██║███████║██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║
-_██▓▓▓▓▓▓████▓▓█               ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
██▓▓▓▓▓▓███░░███░
-__██░░░░░░███████
-____██░░░░███████
-______██████████
-_____██▓▓▓▓▓▓▓▓▓██
-_____█████████████
                                                                
            \n''')
    print('1) Iniciar Juego')
    print('2) Opciones del Juego')
    print('3) Salón de la Fama')
    print('4) Creditos del Juego')
    print('5) SALIR\n')
    opcion = rint('Escribe el número de la opción que quieras: ','Error: Opcion Incorrecta')
    if opcion == 1:
        limpiar()
        colores('verde')
        print('''
                    _____
                 ,-"     "-.
                / o       o \\
               /   \     /   \\                 
              /     )-"-(     \\                
             /     ( 6 6 )     \\                _____   ______________  ____________________________
            /       \ " /       \\               ___  | / /_  __ \__   |/  /__  __ )__  __ \__  ____/
           /         )=(         \\              __   |/ /_  / / /_  /|_/ /__  __  |_  /_/ /_  __/  
          /   o   .--"-"--.   o   \\             _  /|  / / /_/ /_  /  / / _  /_/ /_  _, _/_  /___  
         /    I  /  -   -  \  I    \\            /_/ |_/  \____/ /_/  /_/  /_____/ /_/ |_| /_____/  
     .--(    (_}y/\       /\y{_)    )--.         
    (    ".___l\/__\_____/__\/l___,"    )        
     \                                 /         
      "-._      o O o O o O o      _,-"         
          `--Y--.___________.--Y--'
             |==.___________.==| 
             `==.___________.==' 

        ''')

        usuario = input('\t\t\t\t\t')
        while usuario=='':
            usuario = input('\t\t\t\t\t')
        pausa()
        continuar_juego = True
        while continuar_juego == True:
            limpiar()
            colores('blanco')
            print('''

            
                            ___________________________________|      |____________________________________________
                                                  ,--.    ,--.          ,--.   ,--.
                                                 |oo  | _  \  `.       | oo | |  oo|
                              o  o  o  o  o  o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o  o  o  o  o  o
                                                 |/\/\|   '._,'        |/\/\| |/\/\|
                            ___________________________________        ____________________________________________
                                         JUEGOS                |      |               DISPONIBLES

            ''')
            print('1) Matemática')
            print('2) Historia')
            print('3) Ciencia')
            print('4) Terminar Partida\n')
            opc_juego = lee_entero('OPCION: ')
            if opc_juego == 1:
                mixer.music.stop()
                mixer.music.load('music/mate.mp3')
                mixer.music.play()
                limpiar()
                cont = True
                while cont == True:
                    limpiar()
                    print('''

                    __              ___  ___      _                       _   _                     
                 U /"/_ u           |  \/  |     | |                     | | (_)                      ____    
                 \| '_ \/           | .  . | __ _| |_ ___ _ __ ___   __ _| |_ _  ___ __ _            |___"\   
                  | (_) |           | |\/| |/ _` | __/ _ \ '_ ` _ \ / _` | __| |/ __/ _` |           U __) |  
                   \___/            | |  | | (_| | ||  __/ | | | | | (_| | |_| | (_| (_| |           \/ __/ \ 
                  _// \\\\            \_|  |_/\__,_|\__\___|_| |_| |_|\__,_|\__|_|\___\__,_|           |_____|u 
                 (__) (__)                                                                           <<  //   
                                                                                                    (__)(__)  
                    \n''')
                    print('Elige un nivel:\n')
                    print('1) Principiante ')
                    print('2) Intermedio ')
                    print('3) Avanzado')
                    print('4) Regresar\n')
                    op = rint('Escribe el número de la opción que quieras: ','Error: Opcion Incorrecta')
                    if op == 1:
                        limpiar()
                        # PRINCIPIANTE

                        pregunta = []
                        respuesta = []
                        correccion = []

                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])

                        leer_tipo('pregunta',1,5,pregunta)
                        leer_tipo('respuesta',1,5,respuesta)
                        leer_tipo('correccion',1,5,correccion)


                        def buscar(lista,valor):
                            if len(lista)==0:
                                return False
                            else:
                                encontrado=False
                                for i in range(len(lista)):
                                    if valor==lista[i]:
                                        encontrado=True
                                        return True
                                        break
                                    elif i == len(lista)-1 and encontrado==False:
                                        return False

                        repetidas=[]
                        correcto=True
                        while correcto==True:
                            limpiar()
                            print('PRINCIPIANTE\n')
                            print('Escribe las respuestas de las prguntas de la forma más simplificada y en fracción\n')
                            if len(repetidas)==len(pregunta):
                                print('¡Juego completado!')
                                correcto=False
                            else:
                                validado=False
                                while validado==False:
                                    aleatorio = random.randint(0,len(pregunta)-1)
                                    if buscar(repetidas,aleatorio) == False:
                                        validado=True
                                        repetidas.append(aleatorio)
                                print(pregunta[aleatorio])
                                res = input('\nRESPUESTA: ')
                                if res == respuesta[aleatorio]:
                                    print('¡CORRECTO!')
                                    puntaje += 50
                                    pausa()
                                else:
                                    print(correccion[aleatorio])
                                    pausa()
                                    correcto=False
                        limpiar()
                        numero(puntaje)
                        pausa()
                    elif op == 2:
                        limpiar()
                        # INTERMEDIO

                        pregunta = []
                        respuesta = []
                        correccion = []

                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])

                        leer_tipo('pregunta',8,12,pregunta)
                        leer_tipo('respuesta',8,12,respuesta)
                        leer_tipo('correccion',8,12,correccion)


                        def buscar(lista,valor):
                            if len(lista)==0:
                                return False
                            else:
                                encontrado=False
                                for i in range(len(lista)):
                                    if valor==lista[i]:
                                        encontrado=True
                                        return True
                                        break
                                    elif i == len(lista)-1 and encontrado==False:
                                        return False

                        repetidas=[]
                        correcto=True
                        while correcto==True:
                            limpiar()
                            print('INTERMEDIO\n')
                            print('Escribe las respuestas de las prguntas de la forma más simplificada\n')
                            if len(repetidas)==len(pregunta):
                                print('¡Juego completado!')
                                correcto=False
                            else:
                                validado=False
                                while validado==False:
                                    aleatorio = random.randint(0,len(pregunta)-1)
                                    if buscar(repetidas,aleatorio) == False:
                                        validado=True
                                        repetidas.append(aleatorio)
                                print(pregunta[aleatorio])
                                res = input('\nRESPUESTA: ')
                                if res == respuesta[aleatorio]:
                                    print('¡CORRECTO!')
                                    puntaje += 50
                                    pausa()
                                else:
                                    print(correccion[aleatorio])
                                    pausa()
                                    correcto=False
                        limpiar()
                        numero(puntaje)
                        pausa()
                    elif op == 3:
                        limpiar()
                        # AVANZADO

                        pregunta = []
                        respuesta = []
                        correccion = []

                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])

                        leer_tipo('pregunta',15,19,pregunta)
                        leer_tipo('respuesta',15,19,respuesta)
                        leer_tipo('correccion',15,19,correccion)


                        def buscar(lista,valor):
                            if len(lista)==0:
                                return False
                            else:
                                encontrado=False
                                for i in range(len(lista)):
                                    if valor==lista[i]:
                                        encontrado=True
                                        return True
                                        break
                                    elif i == len(lista)-1 and encontrado==False:
                                        return False

                        repetidas=[]
                        correcto=True
                        while correcto==True:
                            limpiar()
                            print('AVANZADO\n')
                            if len(repetidas)==len(pregunta):
                                print('¡Juego completado!')
                                correcto=False
                            else:
                                validado=False
                                while validado==False:
                                    aleatorio = random.randint(0,len(pregunta)-1)
                                    if buscar(repetidas,aleatorio) == False:
                                        validado=True
                                        repetidas.append(aleatorio)
                                print(pregunta[aleatorio])
                                res = input('\nRESPUESTA: ')
                                if res == respuesta[aleatorio]:
                                    print('¡CORRECTO!')
                                    puntaje += 50
                                    pausa()
                                else:
                                    print(correccion[aleatorio])
                                    pausa()
                                    correcto=False
                        limpiar()
                        numero(puntaje)
                        pausa()
                    elif op == 4:
                        cont = False
                        pausa()
            elif opc_juego == 2:
                limpiar()
                mixer.music.stop()
                mixer.init()
                mixer.music.load('music/historia.mp3')
                mixer.music.play()
                limpiar()

                seguir = True
                while seguir == True:
                    limpiar()
                    print('''

                                      /^\\
                   L L               /   \               L L
                __/|/|_             /  .  \             _|\|\__
               /_| [_[_\           /     .-\           /_]_] |_\\
              /__\  __`-\_____    /    .    \    _____/-`__  /__\\          _   _ _     _             _       
             /___] /=@>  _   {>  /-.         \  <}   _  <@=\ [___\\        | | | (_)   | |           (_)      
            /____/     /` `--/  /      .      \  \--` `\     \____\\       | |_| |_ ___| |_ ___  _ __ _  __ _ 
           /____/  \____/`-._> /               \ <_.-`\____/  \____\\      |  _  | / __| __/ _ \| '__| |/ _` |
          /____/    /__/      /-._     .   _.-  \      \__\    \____\\     | | | | \__ \ || (_) | |  | | (_| |
         /____/    /__/      /         .         \      \__\    \____\\    \_| |_/_|___/\__\___/|_|  |_|\__,_|
        |____/_  _/__/      /          .          \      \__\_  _\____|
         \__/_ ``_|_/      /      -._  .        _.-\      \_|_`` _\___/
           /__`-`__\      <_         `-;           _>      /__`-`__\\
              `-`           `-._       ;       _.-`           `-`
                                `-._   ;   _.-`
                                    `-._.-`

                    \n''')
                    print('Elige un nivel:\n')
                    print('1) Principiante ')
                    print('2) Intermedio ')
                    print('3) Avanzado')
                    print('4) Regresar\n')
                    opc = rint('Escribe el número de la opción que quieras: ','Error: Opcion Incorrecta')
                    if opc == 1:
                        limpiar()
                        preguntas =[]
                        respuestas = []
                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])
                        # Facil -> 1,6
                        # Medio -> 11,15
                        # Dificil -> 19,24
                        leer_tipo('pregsopa',1,6,preguntas)
                        leer_tipo('respsopa',1,6,respuestas)
                        
                        
                        #sopita(preguntas,respuestas,puntaje)

                        tablero = [
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

                        # Intentar llenar

                        for p in range(len(respuestas)):
                            # Tipo de llenado
                            '''
                            1. Derecha
                            2. Izquierda
                            3. Arriba
                            4. Abajo
                            '''
                            r_llenar = random.randint(1, 4)
                            l = len(respuestas[p])
                            #print('Llenado: ' + str(r_llenar))
                            if r_llenar == 1:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)

                                    disponibles = 12 - r_pos_j
                                    while disponibles < l:
                                        r_pos_j = random.randint(0, 11)
                                        disponibles = 12 - r_pos_j
                                    vacio = False
                                    cont = 0
                                    for j in range(r_pos_j, r_pos_j+l):
                                        if tablero[r_pos_i][j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for j in range(r_pos_j, r_pos_j+l):
                                            tablero[r_pos_i][j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True

                            elif r_llenar == 2:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = r_pos_j + 1
                                    while disponibles < l:
                                        r_pos_j = random.randint(0, 11)
                                        disponibles = r_pos_j + 1
                                    vacio = False
                                    cont = 0
                                    for j in range(r_pos_j, r_pos_j-l, -1):
                                        if tablero[r_pos_i][j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for j in range(r_pos_j, r_pos_j-l, -1):
                                            tablero[r_pos_i][j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
                            elif r_llenar == 3:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = r_pos_i+1
                                    while disponibles < l:
                                        r_pos_i = random.randint(0, 11)
                                        disponibles = r_pos_i+1
                                    vacio = False
                                    cont = 0
                                    for i in range(r_pos_i,r_pos_i-l,-1):
                                        if tablero[i][r_pos_j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for i in range(r_pos_i,r_pos_i-l,-1):
                                            tablero[i][r_pos_j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
                            elif r_llenar == 4:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = 12- r_pos_i
                                    while disponibles < l:
                                        r_pos_i = random.randint(0, 11)
                                        disponibles = 12- r_pos_i
                                    vacio = False
                                    cont = 0
                                    for i in range(r_pos_i,r_pos_i+l):
                                        if tablero[i][r_pos_j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for i in range(r_pos_i,r_pos_i+l):
                                            tablero[i][r_pos_j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True

                        def printTablero(matriz):
                            print('    a b c d e f g h i j k l')
                            print('')
                            for i in range(len(matriz)):
                                if i < 10:
                                    cor = ' '+str(i)
                                else:
                                    cor = str(i)
                                print(cor, end='  ')
                                for j in range(len(matriz[i])):
                                    if matriz[i][j] == '*':
                                        print("\033[43;44m"+str(matriz[i][j])+"\033[0m", end=' ')
                                    else:
                                        print(matriz[i][j], end=' ')
                                print('')


                        def llenarAleatorio(matriz):
                            for i in range(len(matriz)):
                                for j in range(len(matriz[i])):
                                    if matriz[i][j] == ' ':
                                        letra = chr(random.randint(65, 90))
                                        matriz[i][j] = letra

                        def buscar(lista,palabra):
                            try:
                                return lista.index(palabra)
                            except ValueError:
                                return -1

                        def seleccionar(matriz):
                            print('\nCoordenadas de inicio:')
                            ini = input('fila,columna : ').strip().split(',')
                            print('\nCoordenadas de fin:')
                            fin = input('fila,columna : ').strip().split(',')
                            print(ini)
                            print(fin) 
                            valido=False
                            while valido == False:
                                try:
                                    test = int(ini[0])
                                    test = int(fin[0])
                                    if ini[0]==fin[0] and conver_Letra(ini[1])<conver_Letra(fin[1]):
                                        # Izquierda a Derecha
                                        palabra = ''
                                        for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])+1):
                                            #0 1 2 3
                                            palabra += matriz[int(ini[0])][j]
                                        if buscar(respuestas,palabra) != -1:
                                            for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])+1):
                                                matriz[int(ini[0])][j] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif ini[0]==fin[0] and conver_Letra(ini[1])>conver_Letra(fin[1]):
                                        # Derecha a izquierda
                                        palabra = ''
                                        for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])-1,-1):
                                            palabra += matriz[int(ini[0])][j]
                                        if buscar(respuestas,palabra) != -1:
                                            for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])-1,-1):
                                                matriz[int(ini[0])][j] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif conver_Letra(ini[1])==conver_Letra(fin[1]) and ini[0]>fin[0]:
                                        # Abajo hacia arriba
                                        palabra = ''
                                        for i in range(int(ini[0]),int(fin[0])-1,-1):
                                            palabra += matriz[i][conver_Letra(ini[1])]
                                        if buscar(respuestas,palabra) != -1:
                                            for i in range(int(ini[0]),int(fin[0])-1,-1):
                                                matriz[i][conver_Letra(ini[1])] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif conver_Letra(ini[1])==conver_Letra(fin[1]) and ini[0]<fin[0]:
                                        # Arriba hacia abajo
                                        palabra = ''
                                        for i in range(int(ini[0]),int(fin[0])+1):
                                            palabra += matriz[i][conver_Letra(ini[1])]
                                        if buscar(respuestas,palabra) != -1:
                                            for i in range(int(ini[0]),int(fin[0])+1):
                                                matriz[i][conver_Letra(ini[1])] = '*'
                                            return True
                                        else:
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                except IndexError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')
                                except TypeError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')
                                except ValueError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')

                        def conver_Letra(letra):
                            if letra == 'a':
                                return 0
                            elif letra == 'b':
                                return 1
                            elif letra == 'c':
                                return 2
                            elif letra == 'd':
                                return 3
                            elif letra == 'e':
                                return 4
                            elif letra == 'f':
                                return 5
                            elif letra == 'g':
                                return 6
                            elif letra == 'h':
                                return 7
                            elif letra == 'i':
                                return 8
                            elif letra == 'j':
                                return 9
                            elif letra == 'k':
                                return 10
                            elif letra == 'l':
                                return 11

                        llenarAleatorio(tablero)
                        ganador = False
                        while ganador == False:
                            for i in range(len(preguntas)):
                                limpiar()
                                print('Completa la siguiente frase: \n')
                                print(preguntas[i],'\n')
                                printTablero(tablero)
                                while seleccionar(tablero) == False:
                                    pass
                                puntaje += 50
                                if i==len(preguntas)-1:
                                    limpiar()
                                    printTablero(tablero)
                                    pausa()
                                    limpiar()
                                    print('''

                                    ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗██╗██╗
                                    ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║██║██║
                                    ██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║██║██║██║
                                    ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║╚═╝╚═╝╚═╝
                                     ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║██╗██╗██╗
                                      ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝

                                    ''')
                                    numero(puntaje)
                                    pausa()
                                    ganador=True


                    elif opc == 2:
                        limpiar()
                        preguntas =[]
                        respuestas = []
                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])
                        # Facil -> 1,6
                        # Medio -> 10,15
                        # Dificil -> 19,24
                        leer_tipo('respsopa',10,15,respuestas)
                        leer_tipo('pregsopa',10,15,preguntas)
                        
                        #sopita(preguntas,respuestas,puntaje)

                        tablero = [
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
                        # Intentar llenar
    
                        for p in range(len(respuestas)):
                            # Tipo de llenado
                            '''
                            1. Derecha
                            2. Izquierda
                            3. Arriba
                            4. Abajo
                            '''
                            r_llenar = random.randint(1, 4)
                            l = len(respuestas[p])
                            #print('Llenado: ' + str(r_llenar))
                            if r_llenar == 1:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
    
                                    disponibles = 12 - r_pos_j
                                    while disponibles < l:
                                        r_pos_j = random.randint(0, 11)
                                        disponibles = 12 - r_pos_j
                                    vacio = False
                                    cont = 0
                                    for j in range(r_pos_j, r_pos_j+l):
                                        if tablero[r_pos_i][j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for j in range(r_pos_j, r_pos_j+l):
                                            tablero[r_pos_i][j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
    
                            elif r_llenar == 2:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = r_pos_j + 1
                                    while disponibles < l:
                                        r_pos_j = random.randint(0, 11)
                                        disponibles = r_pos_j + 1
                                    vacio = False
                                    cont = 0
                                    for j in range(r_pos_j, r_pos_j-l, -1):
                                        if tablero[r_pos_i][j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for j in range(r_pos_j, r_pos_j-l, -1):
                                            tablero[r_pos_i][j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
                            elif r_llenar == 3:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = r_pos_i+1
                                    while disponibles < l:
                                        r_pos_i = random.randint(0, 11)
                                        disponibles = r_pos_i+1
                                    vacio = False
                                    cont = 0
                                    for i in range(r_pos_i,r_pos_i-l,-1):
                                        if tablero[i][r_pos_j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for i in range(r_pos_i,r_pos_i-l,-1):
                                            tablero[i][r_pos_j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
                            elif r_llenar == 4:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = 12- r_pos_i
                                    while disponibles < l:
                                        r_pos_i = random.randint(0, 11)
                                        disponibles = 12- r_pos_i
                                    vacio = False
                                    cont = 0
                                    for i in range(r_pos_i,r_pos_i+l):
                                        if tablero[i][r_pos_j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for i in range(r_pos_i,r_pos_i+l):
                                            tablero[i][r_pos_j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
    
                        def printTablero(matriz):
                            print('    a b c d e f g h i j k l')
                            print('')
                            for i in range(len(matriz)):
                                if i < 10:
                                    cor = ' '+str(i)
                                else:
                                    cor = str(i)
                                print(cor, end='  ')
                                for j in range(len(matriz[i])):
                                    if matriz[i][j] == '*':
                                        print("\033[43;44m"+str(matriz[i][j])+"\033[0m", end=' ')
                                    else:
                                        print(matriz[i][j], end=' ')
                                print('')
    
    
                        def llenarAleatorio(matriz):
                            for i in range(len(matriz)):
                                for j in range(len(matriz[i])):
                                    if matriz[i][j] == ' ':
                                        letra = chr(random.randint(65, 90))
                                        matriz[i][j] = letra
    
                        def buscar(lista,palabra):
                            try:
                                return lista.index(palabra)
                            except ValueError:
                                return -1
    
                        def seleccionar(matriz):
                            print('\nCoordenadas de inicio:')
                            ini = input('fila,columna : ').strip().split(',')
                            print('\nCoordenadas de fin:')
                            fin = input('fila,columna : ').strip().split(',')
                            print(ini)
                            print(fin) 
                            valido=False
                            while valido == False:
                                try:
                                    test = int(ini[0])
                                    test = int(fin[0])
                                    if ini[0]==fin[0] and conver_Letra(ini[1])<conver_Letra(fin[1]):
                                        # Izquierda a Derecha
                                        palabra = ''
                                        for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])+1):
                                            #0 1 2 3
                                            palabra += matriz[int(ini[0])][j]
                                        if buscar(respuestas,palabra) != -1:
                                            for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])+1):
                                                matriz[int(ini[0])][j] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif ini[0]==fin[0] and conver_Letra(ini[1])>conver_Letra(fin[1]):
                                        # Derecha a izquierda
                                        palabra = ''
                                        for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])-1,-1):
                                            palabra += matriz[int(ini[0])][j]
                                        if buscar(respuestas,palabra) != -1:
                                            for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])-1,-1):
                                                matriz[int(ini[0])][j] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif conver_Letra(ini[1])==conver_Letra(fin[1]) and ini[0]>fin[0]:
                                        # Abajo hacia arriba
                                        palabra = ''
                                        for i in range(int(ini[0]),int(fin[0])-1,-1):
                                            palabra += matriz[i][conver_Letra(ini[1])]
                                        if buscar(respuestas,palabra) != -1:
                                            for i in range(int(ini[0]),int(fin[0])-1,-1):
                                                matriz[i][conver_Letra(ini[1])] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif conver_Letra(ini[1])==conver_Letra(fin[1]) and ini[0]<fin[0]:
                                        # Arriba hacia abajo
                                        palabra = ''
                                        for i in range(int(ini[0]),int(fin[0])+1):
                                            palabra += matriz[i][conver_Letra(ini[1])]
                                        if buscar(respuestas,palabra) != -1:
                                            for i in range(int(ini[0]),int(fin[0])+1):
                                                matriz[i][conver_Letra(ini[1])] = '*'
                                            return True
                                        else:
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                except IndexError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')
                                except TypeError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')
                                except ValueError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')
    
                        def conver_Letra(letra):
                            if letra == 'a':
                                return 0
                            elif letra == 'b':
                                return 1
                            elif letra == 'c':
                                return 2
                            elif letra == 'd':
                                return 3
                            elif letra == 'e':
                                return 4
                            elif letra == 'f':
                                return 5
                            elif letra == 'g':
                                return 6
                            elif letra == 'h':
                                return 7
                            elif letra == 'i':
                                return 8
                            elif letra == 'j':
                                return 9
                            elif letra == 'k':
                                return 10
                            elif letra == 'l':
                                return 11
                        
                        llenarAleatorio(tablero)
                        ganador = False
                        while ganador == False:
                            for i in range(len(preguntas)):
                                limpiar()
                                print('Completa la siguiente frase: \n')
                                print(preguntas[i],'\n')
                                printTablero(tablero)
                                while seleccionar(tablero) == False:
                                    pass
                                puntaje += 50
                                if i==len(preguntas)-1:
                                    limpiar()
                                    printTablero(tablero)
                                    pausa()
                                    limpiar()
                                    print('''
    
                                            ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗██╗██╗
                                            ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║██║██║
                                            ██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║██║██║██║
                                            ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║╚═╝╚═╝╚═╝
                                              ╚███╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║██╗██╗██╗
                                              ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝
    
                                    ''')
                                    numero(puntaje)
                                    pausa()
                                    ganador=True

                        
                    elif opc == 3:
                        limpiar()
                        preguntas =[]
                        respuestas = []
                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])
                        # Facil -> 1,6
                        # Medio -> 10,15
                        # Dificil -> 19,24
                        print(preguntas)
                        print(respuestas)
                        leer_tipo('respsopa',19,24,respuestas)
                        leer_tipo('pregsopa',19,24,preguntas)
                        
                        #sopita(preguntas,respuestas,puntaje)

                        tablero = [
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
                        # Intentar llenar
    
                        for p in range(len(respuestas)):
                            # Tipo de llenado
                            '''
                            1. Derecha
                            2. Izquierda
                            3. Arriba
                            4. Abajo
                            '''
                            r_llenar = random.randint(1, 4)
                            l = len(respuestas[p])
                            #print('Llenado: ' + str(r_llenar))
                            if r_llenar == 1:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
    
                                    disponibles = 12 - r_pos_j
                                    while disponibles < l:
                                        r_pos_j = random.randint(0, 11)
                                        disponibles = 12 - r_pos_j
                                    vacio = False
                                    cont = 0
                                    for j in range(r_pos_j, r_pos_j+l):
                                        if tablero[r_pos_i][j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for j in range(r_pos_j, r_pos_j+l):
                                            tablero[r_pos_i][j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
    
                            elif r_llenar == 2:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = r_pos_j + 1
                                    while disponibles < l:
                                        r_pos_j = random.randint(0, 11)
                                        disponibles = r_pos_j + 1
                                    vacio = False
                                    cont = 0
                                    for j in range(r_pos_j, r_pos_j-l, -1):
                                        if tablero[r_pos_i][j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for j in range(r_pos_j, r_pos_j-l, -1):
                                            tablero[r_pos_i][j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
                            elif r_llenar == 3:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = r_pos_i+1
                                    while disponibles < l:
                                        r_pos_i = random.randint(0, 11)
                                        disponibles = r_pos_i+1
                                    vacio = False
                                    cont = 0
                                    for i in range(r_pos_i,r_pos_i-l,-1):
                                        if tablero[i][r_pos_j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for i in range(r_pos_i,r_pos_i-l,-1):
                                            tablero[i][r_pos_j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
                            elif r_llenar == 4:
                                posible = False
                                while not posible:
                                    # Posicion inicial de Intento de llenado
                                    r_pos_i = random.randint(0, 11)
                                    r_pos_j = random.randint(0, 11)
                                    disponibles = 12- r_pos_i
                                    while disponibles < l:
                                        r_pos_i = random.randint(0, 11)
                                        disponibles = 12- r_pos_i
                                    vacio = False
                                    cont = 0
                                    for i in range(r_pos_i,r_pos_i+l):
                                        if tablero[i][r_pos_j] == ' ':
                                            cont += 1
                                    if cont == l:
                                        vacio = True
                                    if vacio:
                                        letra = 0
                                        for i in range(r_pos_i,r_pos_i+l):
                                            tablero[i][r_pos_j] = respuestas[p][letra]
                                            letra += 1
                                        posible = True
    
                        def printTablero(matriz):
                            print('    a b c d e f g h i j k l')
                            print('')
                            for i in range(len(matriz)):
                                if i < 10:
                                    cor = ' '+str(i)
                                else:
                                    cor = str(i)
                                print(cor, end='  ')
                                for j in range(len(matriz[i])):
                                    if matriz[i][j] == '*':
                                        print("\033[43;44m"+str(matriz[i][j])+"\033[0m", end=' ')
                                    else:
                                        print(matriz[i][j], end=' ')
                                print('')
    
    
                        def llenarAleatorio(matriz):
                            for i in range(len(matriz)):
                                for j in range(len(matriz[i])):
                                    if matriz[i][j] == ' ':
                                        letra = chr(random.randint(65, 90))
                                        matriz[i][j] = letra
    
                        def buscar(lista,palabra):
                            try:
                                return lista.index(palabra)
                            except ValueError:
                                return -1
    
                        def seleccionar(matriz):
                            print('\nCoordenadas de inicio:')
                            ini = input('fila,columna : ').strip().split(',')
                            print('\nCoordenadas de fin:')
                            fin = input('fila,columna : ').strip().split(',')
                            print(ini)
                            print(fin) 
                            valido=False
                            while valido == False:
                                try:
                                    test = int(ini[0])
                                    test = int(fin[0])
                                    if ini[0]==fin[0] and conver_Letra(ini[1])<conver_Letra(fin[1]):
                                        # Izquierda a Derecha
                                        palabra = ''
                                        for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])+1):
                                            #0 1 2 3
                                            palabra += matriz[int(ini[0])][j]
                                        if buscar(respuestas,palabra) != -1:
                                            for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])+1):
                                                matriz[int(ini[0])][j] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif ini[0]==fin[0] and conver_Letra(ini[1])>conver_Letra(fin[1]):
                                        # Derecha a izquierda
                                        palabra = ''
                                        for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])-1,-1):
                                            palabra += matriz[int(ini[0])][j]
                                        if buscar(respuestas,palabra) != -1:
                                            for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])-1,-1):
                                                matriz[int(ini[0])][j] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif conver_Letra(ini[1])==conver_Letra(fin[1]) and ini[0]>fin[0]:
                                        # Abajo hacia arriba
                                        palabra = ''
                                        for i in range(int(ini[0]),int(fin[0])-1,-1):
                                            palabra += matriz[i][conver_Letra(ini[1])]
                                        if buscar(respuestas,palabra) != -1:
                                            for i in range(int(ini[0]),int(fin[0])-1,-1):
                                                matriz[i][conver_Letra(ini[1])] = '*'
                                            return True
                                        else: 
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                    elif conver_Letra(ini[1])==conver_Letra(fin[1]) and ini[0]<fin[0]:
                                        # Arriba hacia abajo
                                        palabra = ''
                                        for i in range(int(ini[0]),int(fin[0])+1):
                                            palabra += matriz[i][conver_Letra(ini[1])]
                                        if buscar(respuestas,palabra) != -1:
                                            for i in range(int(ini[0]),int(fin[0])+1):
                                                matriz[i][conver_Letra(ini[1])] = '*'
                                            return True
                                        else:
                                            print('Respuesta Incorrecta',palabra)
                                            pausa()
                                            return False
                                        valido=True
                                except IndexError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')
                                except TypeError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')
                                except ValueError:
                                    print('Valores Incorrectos - Intente de nuevo\n')
                                    print('Coordenadas de inicio:')
                                    ini = input('fila,columna : ').strip().split(',')
                                    print('\nCoordenadas de fin:')
                                    fin = input('fila,columna : ').strip().split(',')
    
                        def conver_Letra(letra):
                            if letra == 'a':
                                return 0
                            elif letra == 'b':
                                return 1
                            elif letra == 'c':
                                return 2
                            elif letra == 'd':
                                return 3
                            elif letra == 'e':
                                return 4
                            elif letra == 'f':
                                return 5
                            elif letra == 'g':
                                return 6
                            elif letra == 'h':
                                return 7
                            elif letra == 'i':
                                return 8
                            elif letra == 'j':
                                return 9
                            elif letra == 'k':
                                return 10
                            elif letra == 'l':
                                return 11
                        
                        llenarAleatorio(tablero)
                        ganador = False
                        while ganador == False:
                            for i in range(len(preguntas)):
                                limpiar()
                                print('Completa la siguiente frase: \n')
                                print(preguntas[i],'\n')
                                printTablero(tablero)
                                while seleccionar(tablero) == False:
                                    pass
                                puntaje += 50
                                if i==len(preguntas)-1:
                                    limpiar()
                                    printTablero(tablero)
                                    pausa()
                                    limpiar()
                                    print('''
    
                                            ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗██╗██╗
                                            ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║██║██║
                                            ██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║██║██║██║
                                            ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║╚═╝╚═╝╚═╝
                                             ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║██╗██╗██╗
                                              ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝
    
                                    ''')
                                    numero(puntaje)
                                    pausa()
                                    ganador=True
               
                    elif opc == 4:
                        seguir = False
                        pausa()
            elif opc_juego == 3:
                mixer.music.stop()
                mixer.init()
                mixer.music.load('music/cien.mp3')
                mixer.music.play()
                limpiar()
                seg = True
                while seg == True:
                    limpiar()
                    print('''

                                 (``',
                                / `''/
                               /    /
                            O\/    /
                            \,    /
                            (    /                    _____ _                 _       
                           /x`''7/                   /  __ (_)               (_) 
                          (x   //`\\                 | /  \/_  ___ _ __   ___ _  __ _ 
                         / `''7'`\ \\                | |   | |/ _ \ '_ \ / __| |/ _` |
                        /    /   /()\\               | \__/\ |  __/ | | | (__| | (_| |
                       (    /   `|~~|`               \____/_|\___|_| |_|\___|_|\__,_|
                        `\'\'\'     |  |
                                 |  |
                                 |  |
                                 |  |
                                 |  |
                               /`    `\\
                     ,-------'`        `'-------,
                    `~~~~~~~~~~~~~~~~~~~~~~~~~~~~`            

                    \n''')
                    print('Elige un nivel:\n')
                    print('1) Principiante ')
                    print('2) Intermedio ')
                    print('3) Avanzado')
                    print('4) Regresar\n')
                    opc = rint('Escribe el número de la opción que quieras: ','Error: Opcion Incorrecta')
                    

                    if opc == 1:
                        limpiar()
                        # *****************************************************************************
                        # Creamos un Juego nuevo

                        # Preguntas
                        pregCiencia = []
                        # Respuestas
                        resCiencia = []

                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])
                        
                        leer_tipo('pregahorcado',1,10,pregCiencia)
                        leer_tipo('respahorcado',1,10,resCiencia)

                        for i in range(2):

                            errores = 0  # Numero de veces que se equivoco el usuario

                            hayganador = False  # ¿Hay ganador?

                            # Crear Juego

                            # Escogemos una pregunta al azar
                            pregunta = random.randint(0, len(pregCiencia)-1)

                            linea = []  # Lista donde estaran _ _ _ _ _ _ ...

                            # Cuántas letras tiene nuestra respuesta
                            letras = len(resCiencia[pregunta])

                            # For que se repite para la cantidad de letras de la respuesta
                            for i in range(letras):
                                # Agregamos una '_' para cada letra de la respuesta
                                linea.append('_')

                            # *****************************************************************************

                            # El juego se repite hasta que haya un ganador
                            while hayganador == False:  # Mientras no haya ganador hacer:

                                # TABLERO

                                limpiar()  # Limpiar pantalla
                                print('\tCiencia\n')
                                # Imprime la tabla de acuerdo a cuantos errores tenga el usuario
                                print(AHORCADO[errores]+'\n')
                                # Muestra una pregunta al azar
                                print(pregCiencia[pregunta]+'\n')

                                # LINEAS

                                # For que se repite para la cantidad de letras de la respuesta
                                for i in range(letras):
                                    # Imprime lo que tengamos en la lista 'linea' sin salto de linea
                                    print(linea[i], end=' ')
                                print('\n')  # Hacemos un salto de linea

                                # --------------------------------------------------------------------------------------

                                # COMPROBAMOS SI HAY GANADOR

                                contador = 0  # Contador
                                # For que se repite para la cantidad de letras de la respuesta
                                for i in range(letras):
                                    # Comprobamos si la posicion actual de 'linea' NO tiene un '_'
                                    if linea[i] != '_':
                                        contador = contador+1  # Si es que no tiene un '_' sumamos 1 al contador

                                if contador == letras:  # Si 'linea' tiene letras en vez de '_' significa que adivino todo
                                    limpiar()  # Limpiar pantalla
                                    print('''


                                            ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗██╗██╗
                                            ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║██║██║
                                            ██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║██║██║██║
                                            ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║╚═╝╚═╝╚═╝
                                             ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║██╗██╗██╗
                                              ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝


                                    ''')
                                    print('\n\t\tFELICIDADES')
                                    print('\nHas conseguido acertar todas las letras')
                                    puntaje += 50
                                    numero(puntaje)

                                    pausa()
                                    hayganador = True  # Indicamos que hay ganador
                                    break  # Salimos del while - Termina el juego

                                # COMPROBAMOS SI PERDIO

                                # Si los errores son igaules a la cantidad de oportunidades hacer:
                                if errores == len(AHORCADO)-1:
                                    limpiar()  # Limpiar pantalla
                                    print('''


                                            ██████╗   █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                                            ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                                            ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                                            ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                                            ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                                             ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝


                                    ''')
                                    print('\nLo sentimos no conseguido acertar todas las letras\n')
                                    numero(puntaje)
                                    pausa()
                                    break  # Salimos del while - Termina el juego

                                # ----------------------------------------------------------------------------------------

                                # LOGICA

                                # Pide una letra al usuario y la convierte a Mayus
                                letra = input('Introduce una letra: ').upper()
                                encontrado = False  # Creamos una variable para saber si encontramos lo que buscamos

                                # BUSCAMOS LA LETRA EN LA RESPUESTA

                                # For que se repite para la cantidad de letras de la respuesta
                                for x in range(letras):
                                    # Si 'letra' es igual a respuesta[letra actual]
                                    if letra == resCiencia[pregunta][x]:
                                        linea[x] = letra  # Reemplazamos '_' por la 'letra'
                                        encontrado = True  # Indicamos que encotramos la 'letra' en la respuesta
                                    elif x == letras-1 and encontrado == False:
                                        # Si estamos en la ultima vuelta y no se ha encontrado:
                                        # Indicamos que no esta
                                        print(":'( "+letra+' no esta')
                                        errores = errores+1  # Agregamos un error al usuario
                                        # Nos pide una tecla para continuar
                                        pausa()

                    elif opc == 2:
                        limpiar()
                        # *****************************************************************************
                        # Creamos un Juego nuevo

                        # Preguntas
                        pregCiencia = []

                        # Respuestas
                        resCiencia = []

                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])
                        
                        leer_tipo('pregahorcado',14,23,pregCiencia)
                        leer_tipo('respahorcado',14,23,resCiencia)

                        for i in range(2):
                            
                            errores = 0  # Numero de veces que se equivoco el usuario
    
                            hayganador = False  # ¿Hay ganador?
    
                            # Crear Juego
    
                            # Escogemos una pregunta al azar
                            pregunta = random.randint(0, len(pregCiencia)-1)
    
                            linea = []  # Lista donde estaran _ _ _ _ _ _ ...
    
                            # Cuántas letras tiene nuestra respuesta
                            letras = len(resCiencia[pregunta])
    
                            # For que se repite para la cantidad de letras de la respuesta
                            for i in range(letras):
                                # Agregamos una '_' para cada letra de la respuesta
                                linea.append('_')
    
                            # *****************************************************************************
    
                            # El juego se repite hasta que haya un ganador
                            while hayganador == False:  # Mientras no haya ganador hacer:
                            
                                # TALBERO
    
                                limpiar()  # Limpiar pantalla
                                print('\tCiencia\n')
                                # Imprime la tabla de acuerdo a cuantos errores tenga el usuario
                                print(AHORCADO[errores]+'\n')
                                # Muestra una pregunta al azar
                                print(pregCiencia[pregunta]+'\n')
    
                                # LINEAS
    
                                # For que se repite para la cantidad de letras de la respuesta
                                for i in range(letras):
                                    # Imprime lo que tengamos en la lista 'linea' sin salto de linea
                                    print(linea[i], end=' ')
                                print('\n')  # Hacemos un salto de linea
    
                                # --------------------------------------------------------------------------------------
    
                                # COMPROBAMOS SI HAY GANADOR
    
                                contador = 0  # Contador
                                # For que se repite para la cantidad de letras de la respuesta
                                for i in range(letras):
                                    # Comprobamos si la posicion actual de 'linea' NO tiene un '_'
                                    if linea[i] != '_':
                                        contador = contador+1  # Si es que no tiene un '_' sumamos 1 al contador
    
                                if contador == letras:  # Si 'linea' tiene letras en vez de '_' significa que adivino todo
                                    limpiar()  # Limpiar pantalla
                                    print('''
    
    
                                            ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗██╗██╗
                                            ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║██║██║
                                            ██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║██║██║██║
                                            ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║╚═╝╚═╝╚═╝
                                             ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║██╗██╗██╗
                                              ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝
    
    
                                    ''')
                                    print('\n\t\tFELICIDADES')
                                    print('\nHas conseguido acertar todas las letras')
                                    puntaje += 50
                                    numero(puntaje)
                                    
                                    pausa()
                                    hayganador = True  # Indicamos que hay ganador
                                    break  # Salimos del while - Termina el juego
                                
                                # COMPROBAMOS SI PERDIO
    
                                # Si los errores son igaules a la cantidad de oportunidades hacer:
                                if errores == len(AHORCADO)-1:
                                    limpiar()  # Limpiar pantalla
                                    print('''
    
    
                                            ██████╗   █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                                            ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                                            ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                                            ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                                            ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                                             ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
    
    
                                    ''')
                                    print('\nLo sentimos no conseguido acertar todas las letras\n')
                                    numero(puntaje)
                                    pausa()
                                    break  # Salimos del while - Termina el juego
                                
                                # ----------------------------------------------------------------------------------------
    
                                # LOGICA
    
                                # Pide una letra al usuario y la convierte a Mayus
                                letra = input('Introduce una letra: ').upper()
                                encontrado = False  # Creamos una variable para saber si encontramos lo que buscamos
    
                                # BUSCAMOS LA LETRA EN LA RESPUESTA
    
                                # For que se repite para la cantidad de letras de la respuesta
                                for x in range(letras):
                                    # Si 'letra' es igual a respuesta[letra actual]
                                    if letra == resCiencia[pregunta][x]:
                                        linea[x] = letra  # Reemplazamos '_' por la 'letra'
                                        encontrado = True  # Indicamos que encotramos la 'letra' en la respuesta
                                    elif x == letras-1 and encontrado == False:
                                        # Si estamos en la ultima vuelta y no se ha encontrado:
                                        # Indicamos que no esta
                                        print(":'( "+letra+' no esta')
                                        errores = errores+1  # Agregamos un error al usuario
                                        # Nos pide una tecla para continuar
                                        pausa()
                    elif opc == 3:
                        limpiar()
                        # *****************************************************************************
                        # Creamos un Juego nuevo

                        # Preguntas
                        pregCiencia = []

                        # Respuestas
                        resCiencia = []

                        def leer_tipo(nombre_archivo,inicio,fin,salida):
                            txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                            lispreg = txtpreg.readlines()
                            for i in range(inicio,fin+1):
                                lispreg[i]=lispreg[i].replace('\n','')
                                salida.append(lispreg[i])
                        
                        leer_tipo('pregahorcado',27,36,pregCiencia)
                        leer_tipo('respahorcado',27,36,resCiencia)

                        for i in range(2):
                            
                            errores = 0  # Numero de veces que se equivoco el usuario
    
                            hayganador = False  # ¿Hay ganador?
    
                            # Crear Juego
    
                            # Escogemos una pregunta al azar
                            pregunta = random.randint(0, len(pregCiencia)-1)
    
                            linea = []  # Lista donde estaran _ _ _ _ _ _ ...
    
                            # Cuántas letras tiene nuestra respuesta
                            letras = len(resCiencia[pregunta])
    
                            # For que se repite para la cantidad de letras de la respuesta
                            for i in range(letras):
                                # Agregamos una '_' para cada letra de la respuesta
                                linea.append('_')
    
                            # *****************************************************************************
    
                            # El juego se repite hasta que haya un ganador
                            while hayganador == False:  # Mientras no haya ganador hacer:
                            
                                # TALBERO
    
                                limpiar()  # Limpiar pantalla
                                print('\tCiencia\n')
                                # Imprime la tabla de acuerdo a cuantos errores tenga el usuario
                                print(AHORCADO[errores]+'\n')
                                # Muestra una pregunta al azar
                                print(pregCiencia[pregunta]+'\n')
    
                                # LINEAS
    
                                # For que se repite para la cantidad de letras de la respuesta
                                for i in range(letras):
                                    # Imprime lo que tengamos en la lista 'linea' sin salto de linea
                                    print(linea[i], end=' ')
                                print('\n')  # Hacemos un salto de linea
    
                                # --------------------------------------------------------------------------------------
    
                                # COMPROBAMOS SI HAY GANADOR
    
                                contador = 0  # Contador
                                # For que se repite para la cantidad de letras de la respuesta
                                for i in range(letras):
                                    # Comprobamos si la posicion actual de 'linea' NO tiene un '_'
                                    if linea[i] != '_':
                                        contador = contador+1  # Si es que no tiene un '_' sumamos 1 al contador
    
                                if contador == letras:  # Si 'linea' tiene letras en vez de '_' significa que adivino todo
                                    limpiar()  # Limpiar pantalla
                                    print('''
    
    
                                            ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗██╗██╗
                                            ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║██║██║
                                            ██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║██║██║██║
                                            ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║╚═╝╚═╝╚═╝
                                             ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║██╗██╗██╗
                                              ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝
    
    
                                    ''')
                                    print('\n\t\tFELICIDADES')
                                    print('\nHas conseguido acertar todas las letras')
                                    puntaje += 50
                                    numero(puntaje)
                                    
                                    pausa()
                                    hayganador = True  # Indicamos que hay ganador
                                    break  # Salimos del while - Termina el juego
                                
                                # COMPROBAMOS SI PERDIO
    
                                # Si los errores son igaules a la cantidad de oportunidades hacer:
                                if errores == len(AHORCADO)-1:
                                    limpiar()  # Limpiar pantalla
                                    print('''
    
    
                                            ██████╗   █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                                            ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                                            ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                                            ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                                            ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                                             ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
    
    
                                    ''')
                                    print('\nLo sentimos no conseguido acertar todas las letras\n')
                                    numero(puntaje)
                                    pausa()
                                    break  # Salimos del while - Termina el juego
                                
                                # ----------------------------------------------------------------------------------------
    
                                # LOGICA
    
                                # Pide una letra al usuario y la convierte a Mayus
                                letra = input('Introduce una letra: ').upper()
                                encontrado = False  # Creamos una variable para saber si encontramos lo que buscamos
    
                                # BUSCAMOS LA LETRA EN LA RESPUESTA
    
                                # For que se repite para la cantidad de letras de la respuesta
                                for x in range(letras):
                                    # Si 'letra' es igual a respuesta[letra actual]
                                    if letra == resCiencia[pregunta][x]:
                                        linea[x] = letra  # Reemplazamos '_' por la 'letra'
                                        encontrado = True  # Indicamos que encotramos la 'letra' en la respuesta
                                    elif x == letras-1 and encontrado == False:
                                        # Si estamos en la ultima vuelta y no se ha encontrado:
                                        # Indicamos que no esta
                                        print(":'( "+letra+' no esta')
                                        errores = errores+1  # Agregamos un error al usuario
                                        # Nos pide una tecla para continuar
                                        pausa()

                    elif opc == 4:
                        seg = False
                        pausa()
                    else:
                        print('ERROR: Opción Inválida')
                        pausa()
            elif opc_juego == 4:
                #TERMINAR JUEGO
                mixer.music.stop()
                limpiar()

                colores('amarillo')
                def mostrar(ranking):
                    print('''

                    ________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                 
                    ________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                   /$$$$$$            /$$                                 /$$                 /$$                 /$$$$$$$$                              
                    ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶            /$$__  $$          | $$                                | $$                | $$                | $$_____/                              
                    _¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         | $$  \__/  /$$$$$$ | $$  /$$$$$$  /$$$$$$$         /$$$$$$$  /$$$$$$       | $$  /$$$$$$       | $$    /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
                    ¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶        |  $$$$$$  |____  $$| $$ /$$__  $$| $$__  $$       /$$__  $$ /$$__  $$      | $$ | ____  $$     | $$$$$|____  $$| $$_  $$_  $$ |____  $$
                    ¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶         \____  $$  /$$$$$$$| $$| $$  \ $$| $$  \ $$      | $$  | $$| $$$$$$$$      | $$  /$$$$$$$      | $$__/ /$$$$$$$| $$ \ $$ \ $$  /$$$$$$$
                    ¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶         /$$  \ $$ /$$__  $$| $$| $$  | $$| $$  | $$      | $$  | $$| $$_____/      | $$ / $$__  $$     | $$   /$$__  $$| $$ | $$ | $$ /$$__  $$
                    ¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶        |  $$$$$$/|  $$$$$$$| $$|  $$$$$$/| $$  | $$      |  $$$$$$$|  $$$$$$$      | $$|  $$$$$$$      | $$  |  $$$$$$$| $$ | $$ | $$|  $$$$$$$
                    ¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶         \______/  \_______/|__/ \______/ |__/  |__/       \_______/ \_______/      |__/ \_______/      |__/   \_______/|__/ |__/ |__/ \_______/
                    _¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶____¶¶¶         
                    _¶¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶__¶¶¶¶          
                    ___¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶           PRIMER PUESTO
                    ____¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶                 
                    ______¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶                    {:30} {:4}
                    _______________¶¶¶¶¶¶¶¶¶¶¶¶                        
                    _________________¶¶¶¶¶¶¶¶                          SEGUNDO PUESTO
                    ___________________¶¶¶¶                            
                    ___________________¶¶¶¶                                  {:30} {:4}
                    ___________________¶¶¶¶                            
                    ___________________¶¶¶¶                            TERCER PUESTO
                    _______________¶¶¶¶¶¶¶¶¶¶¶¶                        
                    ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                           {:30} {:4}
                    ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                     
                    ____________¶¶¶____________¶¶¶                     CUARTO PUESTO
                    ____________¶¶¶____________¶¶¶                     
                    ____________¶¶¶____________¶¶¶                           {:30} {:4}
                    ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                     
                    ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                     QUINTO PUESTO
                    __________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                   
                    _________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                        {:30} {:4}

                    '''.format(ranking[0][0],ranking[0][1],ranking[1][0],ranking[1][1],ranking[2][0],ranking[2][1],ranking[3][0],ranking[3][1],ranking[4][0],       ranking[4][1]))


                txtranking = open('ranking.txt','r',encoding='utf8')
                ranking=[]

                for linea in txtranking:
                    linea = linea.replace('\n', '').split(', ')
                    linea = ranking.append(linea)

                txtranking.close()

                for filas in range(len(ranking)):
                    ranking[filas][1] = int(ranking[filas][1])

                def ordenar(rank):
                    rank = sorted(rank, key=operator.itemgetter(1), reverse=True)
                    return rank

                def buscar(lista,palabra):
                    existe=False
                    indice = -1
                    for i in range(len(lista)):
                        if lista[i][0] == palabra:
                            existe = True
                            indice = i
                    return indice

                def try_insertar(datos,rank):
                    rank = ordenar(rank)
                    index = buscar(rank,datos[0])
                    if index != -1 :
                        if rank[index][1] < datos[1]:
                            rank[index][1] = datos[1]
                            rank = ordenar(rank)
                            txt = open('ranking.txt','w')
                            for i in range(len(rank)):
                                txt.write(rank[i][0]+', '+str(rank[i][1]))
                                txt.write('\n')
                            txt.close()
                            return True
                        else:
                            return False
                    else:
                        rank.append(datos)
                        rank = ordenar(rank)
                        rank.remove(rank[len(rank)-1])
                        txt = open('ranking.txt','w')
                        for i in range(len(rank)):
                            txt.write(rank[i][0]+', '+str(rank[i][1]))
                            txt.write('\n')
                        txt.close()
                        if buscar(rank,datos[0]) != -1:
                            return True
                        else:
                            return False
                # =====================================================================
                persona = [usuario , puntaje]
                if try_insertar(persona,ranking):
                    mixer.init()
                    mixer.music.load('music/fama.mp3')
                    mixer.music.play()
                    print('Conseguiste superar un record')
                    txtranking = open('ranking.txt','r',encoding='utf8')
                    ranking=[]

                    for linea in txtranking:
                        linea = linea.replace('\n', '').split(', ')
                        linea = ranking.append(linea)

                    txtranking.close()
                    mostrar(ranking)
                    pausa()
                else:
                    mixer.music.stop()
                    mixer.init()
                    mixer.music.load('music/triste.mp3')
                    mixer.music.play()
                    print('lo sentimos, mas suerte a la Próxima\n')
                    numero(puntaje)
                    pausa()
                # =====================================================================

                continuar_juego = False

            else:
                print('ERROR: Opción Inválida')
                pausa()

    elif opcion == 2:
        cont_opc = True
        while cont_opc == True:
            limpiar()
            print('''

                    OPTIMIZADO PARA : {}

                    ____ ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ _________ ____ ____ ____ ____ ____ 
                    ||O |||P |||C |||I |||O |||N |||E |||S |||       |||D |||E |||L |||       |||J |||U |||E |||G |||O ||
                    ||__|||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||_______|||__|||__|||__|||__|||__||
                    |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|

                        
                    Volumen del Juego

                        1) Modificar Volumen
                        2) Silenciar Juego

                    3)Regresar al Menu Principal   

            '''.format(SO))
            opc_opc = lee_entero('\t\tOPCION: ')
            while opc_opc !=1 and opc_opc !=2 and opc_opc !=3:
                opc_opc = lee_entero('\t\tOPCION: ')
            volumen = mixer.music.get_volume()
            if opc_opc == 1:
                limpiar()
                print('Volumen: {}'.format(volumen*100)+'\n')
                nvol = lee_entero('Nuevo valor (1-100): ')
                while nvol < 1 or nvol>100:
                    mixer.music.set_volume(nvol/100)
                    print('Modificado!\n')
                pausa()
            elif opc_opc==2:
                limpiar()
                mixer.music.stop()
                print('Shhhhh.....\n')
                pausa()
            elif opc_opc==3:
                cont_opc=False
            else:
                print('ERROR: Opcion Incorrecta\n')
                pausa()

    elif opcion == 3:
        limpiar()
        colores('amarillo')
        txtranking = open('ranking.txt','r',encoding='utf8')
        ranking=[]
        for linea in txtranking:
            linea = linea.replace('\n', '').split(', ')
            linea = ranking.append(linea)
        txtranking.close()
        print('''

        ________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                 
        ________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                   /$$$$$$            /$$                                 /$$                 /$$                 /$$$$$$$$                              
        ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶            /$$__  $$          | $$                                | $$                | $$                | $$_____/                              
        _¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         | $$  \__/  /$$$$$$ | $$  /$$$$$$  /$$$$$$$         /$$$$$$$  /$$$$$$       | $$  /$$$$$$       | $$    /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
        ¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶        |  $$$$$$  |____  $$| $$ /$$__  $$| $$__  $$       /$$__  $$ /$$__  $$      | $$ | ____  $$     | $$$$$|____  $$| $$_  $$_  $$ |____  $$
        ¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶         \____  $$  /$$$$$$$| $$| $$  \ $$| $$  \ $$      | $$  | $$| $$$$$$$$      | $$  /$$$$$$$      | $$__/ /$$$$$$$| $$ \ $$ \ $$  /$$$$$$$
        ¶¶________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶         /$$  \ $$ /$$__  $$| $$| $$  | $$| $$  | $$      | $$  | $$| $$_____/      | $$ / $$__  $$     | $$   /$$__  $$| $$ | $$ | $$ /$$__  $$
        ¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶        |  $$$$$$/|  $$$$$$$| $$|  $$$$$$/| $$  | $$      |  $$$$$$$|  $$$$$$$      | $$|  $$$$$$$      | $$  |  $$$$$$$| $$ | $$ | $$|  $$$$$$$
        ¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶         \______/  \_______/|__/ \______/ |__/  |__/       \_______/ \_______/      |__/ \_______/      |__/   \_______/|__/ |__/ |__/ \_______/
        _¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶____¶¶¶         
        _¶¶¶¶___¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶__¶¶¶¶          
        ___¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶           PRIMER PUESTO
        ____¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶                 
        ______¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶                    {:30} {:4}
        _______________¶¶¶¶¶¶¶¶¶¶¶¶                        
        _________________¶¶¶¶¶¶¶¶                          SEGUNDO PUESTO
        ___________________¶¶¶¶                            
        ___________________¶¶¶¶                                  {:30} {:4}
        ___________________¶¶¶¶                            
        ___________________¶¶¶¶                            TERCER PUESTO
        _______________¶¶¶¶¶¶¶¶¶¶¶¶                        
        ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                           {:30} {:4}
        ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                     
        ____________¶¶¶____________¶¶¶                     CUARTO PUESTO
        ____________¶¶¶____________¶¶¶                     
        ____________¶¶¶____________¶¶¶                           {:30} {:4}
        ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                     
        ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                     QUINTO PUESTO
        __________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                   
        _________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                        {:30} {:4}

        '''.format(ranking[0][0],ranking[0][1],ranking[1][0],ranking[1][1],ranking[2][0],ranking[2][1],ranking[3][0],ranking[3][1],ranking[4][0],       ranking[4][1]))
        pausa()
                
    elif opcion == 4:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('music/creditos.mp3')
        mixer.music.play()
        limpiar()
        print('''

        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒░░░░░▓▓
        ▓▓░░░░░░WE░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░▓▓
        ▓▓░░░░░░░░░LOVE░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░PYTHON░░░░░░░░▒▒▒░▒▒▒░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░▓▓
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        _______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ______▒_______________▒▒▒▒▒▒▒▒
        _____▒________________▒▒▒▒▒▒▒▒
        ____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ___▒
        __▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        _▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
        ▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
        ▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
        ▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▒▒

        ''')
        time.sleep(5)
        limpiar()
        print('''
   ===============================================================================================================
   ===============================================================================================================

                            ██████ ██████  ███████ ██████  ██ ████████  ██████  ███████ 
                           ██      ██   ██ ██      ██   ██ ██    ██    ██    ██ ██      
                           ██      ██████  █████   ██   ██ ██    ██    ██    ██ ███████ 
                           ██      ██   ██ ██      ██   ██ ██    ██    ██    ██      ██ 
                            ██████ ██   ██ ███████ ██████  ██    ██     ██████  ███████ 
                                                             
   ===============================================================================================================
   ===============================================================================================================
                                                             
        ''')
        time.sleep(5)
        limpiar()
        colores('verde')
        print('''
                         ██╗    ██╗██╗██╗     ██╗     ██╗ █████╗ ███╗   ███╗
                         ██║    ██║██║██║     ██║     ██║██╔══██╗████╗ ████║
                         ██║ █╗ ██║██║██║     ██║     ██║███████║██╔████╔██║
                         ██║███╗██║██║██║     ██║     ██║██╔══██║██║╚██╔╝██║
                         ╚███╔███╔╝██║███████╗███████╗██║██║  ██║██║ ╚═╝ ██║
                          ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  
        ''')
        time.sleep(3)
        print('''

        ..........................................................................................
        ..........................................................................................
        ..............................................::--:.:.....................................
        ...................................:::-**##%%%%##%#*+=-::.................................
        .................................-+*#######%#%%%%@@%%%#*=-:...............................
        ...............................:*###%%##%%%@@@%%%@%%@%%%*=::..............................
        .............................:+##%%%%%%@@@@@@%@@@@@@@@@@@%+:..............................
        ............................+#%#%@@@@@@@@@@@%%@@@@@@@@@@@@%-:.............................
        ..........................:+#%%%@@@%#+++*#%%%%#####%%%%@@@@%+:............................
        ..........................-%%##%%#*=:::::--======++**##%@@@@%*............................
        ..........................:#%##*-::::..:::::----===+++*#@@@@@%:...........................
        :..........................*%%%+:::::--------=+*###**#**#@@@@+............................
        ...........................*%%%-:----=+**+-:-+#%%#**##***%@@@*............................
        ...........................#%%+:::-=+*#**-:::=###+*##%#***%@@+:...........................
        ...........................*%%-:::---=+=-::::-+**+====++++#@###:..........................
        :........................:=-*#:::::::::::::::-=+++==--=+++#%#*#-..........................
        -:.......................=:::+::::..:::::-+==*##***++=++***%#*+...........................
        -:.......................:::==::::::::--:--:=+*#*************+:...........................
        ...........................:-::::::::--::::--=+****#********+=............................
        ............................:::::::::-=======++*##%%******=-:.............................
        .............................::::::::-+-:::--==+*********+................................
        ................................:::::::::::---==+********:................................
        ................................:-:::::::::::--==++*****=.................................
        .................................:---::::::-==+******##*:::...............................
        ..................................:--======+******#####+-::...............................
        ..................................:::--==+**############@%*::.............................
        ..................................:::::::---+###########%%+--:::..........................
        ................................:++:::::::--+******######+----::::.................::.....
        .....................:----.:::..:#+::::::::--=+*******#+=:::::-----::::..:.:::::::::::::::
        ...............::-:--::::::... .:-+-:::::::--=++==++++--++*+=-::::-----:::::::::::::::::::
        ..........::----:::::-:::...   .::-=-::::::--------:-=+**#####*+=------::::::.::::::::::::
        ::::::::---:::::-:::..          :----...:::::::-===++**********++==-----:::.....::::::::::
        :::--::::::-::...             .=+=--=-.....::-=******++++++++=++===----:::......:::--:::::
        -::::--:::..                .-+=-:..-=-:::::===-=--::::-----------:......::::::::::-==::::
        ---::.......              .:=:.            --::.:.....................:::::::::----===....
        --:-::-:.:.                               ..:..:...................::::::::----====-==:...
        ------=*=-                                .....:......................:.::-----====-==:...
        +++++=+**:                               ......:........................:------=====-=:...
        ''')
        time.sleep(3)
        limpiar()
        colores('morado')
        print('''
        ███████╗███████╗███╗   ██╗██╗   ██╗███████╗ ██████╗███████╗████████╗██╗  ██╗
        ╚══███╔╝██╔════╝████╗  ██║╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝╚══██╔══╝██║  ██║
          ███╔╝ █████╗  ██╔██╗ ██║ ╚████╔╝ █████╗  ██║     █████╗     ██║   ███████║
         ███╔╝  ██╔══╝  ██║╚██╗██║  ╚██╔╝  ██╔══╝  ██║     ██╔══╝     ██║   ██╔══██║
        ███████╗███████╗██║ ╚████║   ██║   ███████╗╚██████╗███████╗   ██║   ██║  ██║
        ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
        ''')
        time.sleep(3)
        print('''
        :::::--------====--=*####%###########*+=-::::::::::::::::::::::::::...::::
        ::::::::::-----=+*######%%%####%%%%%%#**+=-::::::::::::::::::::::::::..:::
        :::::::::::---=*######%%#####***##%%%%%#**+-::::::::::::::::::::::::::::::
        ::::::::::::-+#############*+=---=+#%%%%%#*+-:::::::::::::::::::::::::::::
        ::::::::::::+###########*+=--::::::-=*%%%%#*+-::::::::::::::::::::::::::::
        :::::::::::+#####%%###*=---::::::::::-=#%%%#*+-:::::::::::::::::::::::::::
        ::::::::::=######%###+--:::::::::::::::-#%%%#*=:::::::::::::::::::::::::::
        :::::::::-*#%#%#%%##*---===--:::::::::::=#%%%#+-::::::::::::::::::::::::::
        :::::::::+#%#%%#%%#*=-+++=+***+-::::::::-*%%%%*=::::::::::::::::::::::::::
        ::::::::-##%%%#%%#*+=-:::::::=+++-:::::::=%%%%#+-:::::::::::::::::::::::::
        ::::::::=#%%%%%%%#+=:::-----:::---::::--:-#%%%#*-:::::::::::::::::::::::::
        ::::::::+%%%%%%%#+-:::-+*###==-::::.:-+**+*%%%%#=:::::::::::::::::::::::::
        :::::::-##%%%%%#+=::::::-=++=+=::::::---=+#%%%%#+-::::::::::::::::::::::::
        :::::::=%%%%%%#+-::::::::::---:::::::-=-:-*%%%%%#=-:::::::::::::::::::::::
        :::::::+%%%%%#*-:::::...:::::::::::::+#*+*#%%%%%#+-:::::::::::::::::::::::
        :::::::*%%%%%#=--:::::.....:::::::::::-=+#%%%%%%#*=--:::::::::::::::::::::
        ::::::-#%%%%%*=--:::::......::-::::..::::=%%%%%%%#+=-:::::::::::::::::::::
        ::::::=#%%%%%+=---::::::::.:::--+++-::::::*%%%%%%#*=--::::::::::::::::::::
        ::::::+#%%%%%+-----:::::::::::---:---+::::+@%%%%%##+=--:::::::::::::::::::
        :::::-*%%%%%%+----::::::::::::::::::--:::-*@%%%%%%#+=----:-:::::::::::::::
        :::::-#%%%%%%#---:::::::--=-------:::-:::=%%%%%%%##*===-----::::::::::::::
        :::::-#%%%%%%%+---:::::::-==++++++++=---=#@%%%%%%%##+=-=--------::::::::::
        :::::-#%%%%%%%*=---:::::::::---=====++==#@@@%%%%%%##*==-=---------::::::::
        :::::=#%%%%%%%+++-----:::::::---=====-=*@@@@@%%%%%%##*+===-----------::::-
        :::::*%%%%%%%#==++=----:::::::::-----=*%@@@@@%%%%%%%##*+===---------------
        ::::-#%%%%%@%*====++==---:::::::::--+*%%%%%%%%%%%%%%####**+=--------------
        ::::+%%%%%%@@+=--==+++++=--::::::--=#%%%%##%%%%%%%%%%#####*++++=----------
        :::-*%%%%@@@%=-----==+****+=-----=*%%%#######%%%%%%%#######*+++++=--------
        ::-+#%%%@@@@%--------==+***######%@%%##########%%%######%###**+==++==-----
        ::=*%%%@@@%%+-:-------=++*##%%%%%%%%%%#################%#####**+++++======
        -=*#%%%@@%##*=-----==+*##%%%%%%%%%%%%%%################%%####***+++++=====
        -+**%%@@@%##########%%%%%%%%%%%%%%%%%%%%%##########%#####%####**++++++====
        +**%%@@%%############%#%%%%%%%%%%%%%%%%%%%%######%%%%##########*+++++*+===
        ***%@@%############%%%%%%%%%#####%%%%%%%%%%%####%%%%%###########*+==+++++=
        *+#%%%%############################+#%%%%%%%%%%%%%%%%############*++==++++
        **%#%#%########################*=-:=+%%%%%%%%%%%%%%%%%##*#########**+=====
        +#%##%######################+=--=++**%%%%%%%%%###%%%%%####*########**+++==
        ######%#####################====+*#######%%%#########################*++++
        ######%%###########################################***####*###########*+++
        #######%###########################################****####*########*##*-=
        #######%%########################################*******####*#########*+=:
        ########%#########################################*******####**#%%#%##*+-:
        ########%%########################################********####**#%%%##**-:
        #########%#########################################********####++#%%###=-.
        ##########%#########################################********####++####+--.
        ###########%#########################################*******####*++###+:::

        ''')
        time.sleep(3)
        colores('rojo')
        limpiar()
        print('''
                            █████╗ ███╗   ██╗ █████╗ 
                           ██╔══██╗████╗  ██║██╔══██╗
                           ███████║██╔██╗ ██║███████║
                           ██╔══██║██║╚██╗██║██╔══██║
                           ██║  ██║██║ ╚████║██║  ██║
                           ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
        ''')
        time.sleep(3)
        print('''
        *++##=-++%%@@%%%%%#%#%%##*-*+*-                      .------:::::::::::
        -+==**++*%%@@#*####%%%%#%%##**:.. :                  .:-----:::::::::::
        +-:.*##+#%@%%%%%%##%@@%%%%%+:  .-.-==:                :-----:::::::::::
        *++*##**%%%%#*#%%%%%%**###*=.. ::*=:-=...      ..     .:-:.::::::::::::
        ########%%%%#*#%#%%#***++*++**++=:-:=++*+:    ...      ::: .::::::..:::
        #####%#%%%%%#%%%%%####*+++=*###%#*+=+###+:  :   .      .:: .::::::..:::
        ######%%%%%%%%%%%%%%*=+##*####%%%%%#**###*.:=:...     ..:::::::::::::::
        *#%###%%@%@%%%%%%%%#=+#%%#%@%%%%%%%%%###+:  .-...      ..::.::.-=-=====
        #%#%#%%@%@%%%%%%%%#-=*#%%***#%%%%%%%%%#**-::.......      ....:+#**####*
        #%*#%%%%%%%%%%##%#-:=#%%*+=++*#%@%%%%%%#*=:........       .  .:==+*****
        +*%%%%%%%%%%#####+::+%%*++====+*%%%%%%%%#.. ....::.           :-=*++***
        #*##%%%%%%%#+###*-..+@#++====+##*#%%%%%%%+.   ...:.        .:+**==++*+*
        *=*%%%%%%%%*#%%#+...*%%*++++*######%%%%%%%=.  ...:.     .-+##**+=++****
        *+*%%%%###*=%%%%+.--*%%#**++*###*++*%%%%%%%-.......  .-*#***++++==++***
        #%%%%%###==+###*-.=-*%%%%##+=+**+===#%%%%%%#:.....::::-+++++++++==++***
        %%%%%%*%*=+=***=:.+=+%%%%%#*========+%%%%%%%#:---::..:-==+++++++==++***
        %%%%%%%#**##*#*=.:+=+%%%%#**===+++==+##%%%%%%#*-.::...:=-==++=++==+++**
        #%%%%%#*#**+*#*::-+++%%%#****+**+=+=+##%%%%%%%#+-::...:--++====+==+*+**
        #%#%%###*==+*+-..=***%%%%***#**+++*++#%%@%%%%%%+-::..::-=+++===+==+****
        #####*+#*=**++-.:=##*%%@%#***####*+++*%%@@%%%%%+-:::.:::+=========*****
        #####==**#**++-.-+#*#%%@@@%#####*+=++#%%%@%%%%%+-:::.:::====-==--=++***
        #####*+=:-=*++::+*#*#%%%@@@%##*++++*#%%%%%%@%%*=--::...::-:--=-:-=+****
        #####**++++*+-.=+#*##%%%%@@@%%##**#%%%%%%@@%#+*=-:::..::::::--:--==+***
        *####+++==---::++#+##%%#%@@@@@@%%%%%%%%@%%#*+==##+-:...:::::::---=++***
        *****-::::::::-*=#**##%*#%@@@@%%###%%%%##*++==%@@%%#+=-::::...-=-==****
        =++++-------===*-#*##%%*#%@%%%%%####***+*++==#@@@%@@%%%%#+:...:-:-=****
        ==+==---======+*+####%%%%%@%#######**+++++++#@@@%@@@@@%@@%%*:..::-+****
        =====-=========*#@@%#%%%@@@@%******+++**++=+@@@%@@@@@@@@@@@@%-...-=++**
        ======++=====-*%%@@@%%@@@@@@@*+++++++++++=+%@@@@@@@@@@@@@@@@@#.::-=****
        ===========+++%@@@@@%%@@@@@@@%+++++++==+==#@@@%@@@@@@@@@@@@@@%-:.:=++**
        ============+#%@@@@@@%@@@@@@@@*++====++==+@@@%@@@@@@@@@@@@@@@%+..-=+***
        ============#%%@@@@@@@@@@@@@@@%+=========%@@@@@@@@@@@@@@@@@%%%*::-=++**
        ============##%%@@@@@@@@@@@@@@@%+=======*@@@%@@@@@@@@@@@@@%@@@%:.:=+***
        +++++======+%%@@%%@@@@@@@@@@@@@@%=======%@@%@@@@@@@@@@@@@@@@@@@=..=+***
        +++++++====*@%@@@@@@@@@@@@@@@@@@@%=====#@@@@@@@@@@@@@@@@@@@@@@@*:.=++**
        +***##**#**%@@@@@@@@@@@@@@@@@@%@@@%===+@@@@@@@@@@@@@@@@@@@@@@@@#.:-+***
        **##******+@@@@@@@@@@@@@@@@@@@@%@@@#++%@@%@@@@@@@@@@@@@@@@@@@@@%..-=+**
        **********+@@@@@@@@@@@@@@@@@@@@@%@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@%:.-=***
        ++++*******@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:.-=***
        =====+++++%@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:-=+**
        =========+%@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@====+++
        ===--=-==+%@@@@@%#+=----========+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@==++***
        =------=-*%@@@%+---==-=============+%@@@@@@@@@@@@@@@@@@@@@@@@@@%==+****
        ----===--%%@@*++===-==============++%**#@@@@@@@@@@@@@@@@@@@@@@@%==+****
        :--=----=%%@**+=+*=++=====+++++++++#%++++*#%@@@@@@@@@@@@@@@@@@@%==+****
        --------=%@@@#+#*=+*++++++**#%%#**#%#**#+++++*#%@@%%@@@@@@@@@@@#+=+****
        -----:::=@@%%+##+*#++##%%@@@@@@@@%%***#*++++++++++*#%@@@@@@@@@@#+++*###
        :-:::::-=@@@#*@*+#**#@@@@@@@@@@@@@%##*#*+++++++++++++*%@%%@@@@@***+*###

        ''')
        time.sleep(3)
        limpiar()
        colores('azul')
        print('''
                                                                                
                                                                        
                                                                        
                                                                        
                              .:::---::..                               
                         :-+*######+######*=-:                          
                     .-+###########:.*#####*##*+-.                      
                   :+#############*  .#####.+#####+:                    
                 :*##############*.   *###- .*######+:                  
               :+###############+.   .###=   +########+.                
              =###############*-    .*#*-    *##########-               
            .+###############+.    :*#+.    =#**#########+.             
           .*##############*-    .=#*-     =#*.-##########*.            
          .*##############=.    -*#+.    :*#+. :#####-#####*.           
         .*#############*:    .+#*:    .=##-   -###*: *#####*           
         +#############=     -*#=     :*#+.   .*##*.  +######=          
        -############+.    .+#+:    .+#*-    .+##=    *#######:         
        *##########*-     =#*-     -*#+.    :*#*:    =########*         
       -##########+.    :*#+.    .+#*:    .+##-     =##########:        
       +#########+    .=#*:     =##=.    -*#+.    :*###########=        
       *########*    :*#=.    :*#*:    .+#*-    .=##+-#########*        
      .#########:   -##-    .+##-     =##=.    :*#*- :##########        
      :#########.  :##-    -*#+.    :*#*:    .+##=.  -##########.       
      :#########.  +#+   .+#*-    .=##=     -*#*:   .*##########.       
      .#########- .##-  .*#*.    :*#+.    .+#*-    .+###########.       
       *########*..##:  +#*.   .+##-     =##+.    :*###########*        
       +#########*.*#= =##:   .*#*:    :*#*:    .+#############=        
       -##########**#*.*#+   .*##:    =##+.    -*##############:        
        *#############*##-   *##=    +##*.   .+###############*         
        -################:  -###:   +###:   -#################:         
         +###############-  *###-  =###*   =#################+          
         .*##############*. ####* .####*  =#################*.          
          :*##############+.*####=:#####::#################*.           
           :*##############**#####*#####**################*.            
            .*#####*-------------------------------*#####*.             
             .+#####=.                           .+#####=               
               :*####*-.                       .=*####*:                
                 -*#####+-.                 .-+#####*-                  
                   -+######*+=-:       :-=+*######+:                    
                     .=*#######*       *#######+-.                      
                        .-=+*##*       *##*+=:.                         
                             .::       ::.                              
                                                                        
                                                                        
                                                                        
                                                                        

        ''')
        pausa()
    elif opcion == 5:
        limpiar()
        continuar = False
    else:
        print('ERROR: Opción Inválida')
        pausa()


        
