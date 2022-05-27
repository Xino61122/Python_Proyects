# generar un programa en el que el usuario tenga diferentes opciones, 1 para elegir el número máximo y el número minimo en el que pueda acertar el número    

import time
import random
import os
import sys
import pickle
import errno
import msvcrt as m

def clear(): #limpiar consola
    os.system("cls")

def registrarNombre(puntuacion):
    clear()
    if eleccion == 1:
        valor = 'simple'
    elif eleccion == 2:
        valor = 'intermedio'
    elif eleccion == 3:
        valor = 'avanzado'
    else:
        valor = 'extremo'


    if puntuacion > registro[valor]['jugador1']['puntuacion']:
        nombre = comprobarNombre() 
        registro[valor]['jugador5']['nombre'] = registro[valor]['jugador4']['nombre']
        registro[valor]['jugador5']['puntuacion'] = registro[valor]['jugador4']['puntuacion']
        registro[valor]['jugador4']['nombre'] = registro[valor]['jugador3']['nombre']
        registro[valor]['jugador4']['puntuacion'] = registro[valor]['jugador3']['puntuacion']
        registro[valor]['jugador3']['nombre'] = registro[valor]['jugador2']['nombre']
        registro[valor]['jugador3']['puntuacion'] = registro[valor]['jugador2']['puntuacion']
        registro[valor]['jugador2']['nombre'] = registro[valor]['jugador1']['nombre']
        registro[valor]['jugador2']['puntuacion'] = registro[valor]['jugador1']['puntuacion']
        registro[valor]['jugador1']['puntuacion'] = puntuacion
        registro[valor]['jugador1']['nombre'] = nombre
    elif (puntuacion > registro[valor]['jugador2']['puntuacion']): #and (puntuacion > registro[valor]['jugador3']['puntuacion']):        
        nombre = comprobarNombre() 
        registro[valor]['jugador5']['nombre'] = registro[valor]['jugador4']['nombre']
        registro[valor]['jugador5']['puntuacion'] = registro[valor]['jugador4']['puntuacion']
        registro[valor]['jugador4']['nombre'] = registro[valor]['jugador3']['nombre']
        registro[valor]['jugador4']['puntuacion'] = registro[valor]['jugador3']['puntuacion']
        registro[valor]['jugador3']['nombre'] = registro[valor]['jugador2']['nombre']
        registro[valor]['jugador3']['puntuacion'] = registro[valor]['jugador2']['puntuacion']
        registro[valor]['jugador2']['puntuacion'] = puntuacion
        registro[valor]['jugador2']['nombre'] = nombre
    elif (puntuacion >registro[valor]['jugador3']['puntuacion']): #and (puntuacion > registro[valor]['jugador4']['puntuacion']):
        nombre = comprobarNombre()  
        registro[valor]['jugador5']['nombre'] = registro[valor]['jugador4']['nombre']
        registro[valor]['jugador5']['puntuacion'] = registro[valor]['jugador4']['puntuacion']
        registro[valor]['jugador4']['nombre'] = registro[valor]['jugador3']['nombre']
        registro[valor]['jugador4']['puntuacion'] = registro[valor]['jugador3']['puntuacion']
        registro[valor]['jugador3']['puntuacion'] = puntuacion
        registro[valor]['jugador3']['nombre'] = nombre
    elif (puntuacion >registro[valor]['jugador4']['puntuacion']): #and (puntuacion > registro[valor]['jugador5']['puntuacion']):
        nombre = comprobarNombre()  
        registro[valor]['jugador5']['nombre'] = registro[valor]['jugador4']['nombre']
        registro[valor]['jugador5']['puntuacion'] = registro[valor]['jugador4']['puntuacion']
        registro[valor]['jugador4']['puntuacion'] = puntuacion
        registro[valor]['jugador4']['nombre'] = nombre
    elif puntuacion > registro[valor]['jugador5']['puntuacion']: 
        nombre = comprobarNombre() 
        registro[valor]['jugador5']['puntuacion'] = puntuacion
        registro[valor]['jugador5']['nombre'] = nombre
    
    if eleccion == 1:
        with open('dir1/puntuaciones_simple','wb') as carpickle:
            pickle.dump(registro,carpickle)
    elif eleccion == 2:
        with open('dir1/puntuaciones_intermedia','wb') as carpickle:
            pickle.dump(registro,carpickle)
    elif eleccion == 3:
        with open('dir1/puntuaciones_avanzado','wb') as carpickle:
            pickle.dump(registro,carpickle)
    elif eleccion == 2:
        with open('dir1/puntuaciones_extremo','wb') as carpickle:
            pickle.dump(registro,carpickle)

    leer_diccionario()
    menu()
     
    

def comprobarNombre():
    while True:
        nombre = input("Selecciona 3 caracteres para indicar el record: ")
        if len(nombre) != 3:
            print("Tu nombre tiene que tener 3 caracteres")
            time.sleep(2)
        else:             
            nombre = nombre.upper()
            return nombre
        clear()

def leer_diccionario():
    if eleccion == 1:
        valor = 'simple'
    elif eleccion == 2:
        valor = 'intermedio'
    elif eleccion == 3:
        valor = 'avanzado'
    else:
        valor = 'extremo'
    clear()
    print('''   ***Tabla de puntuaciones***

        1º {} con {} puntos.
        2º {} con {} puntos.
        3º {} con {} puntos.
        4º {} con {} puntos.
        5º {} con {} puntos.
    '''.format(registro[valor]['jugador1']['nombre'],int(registro[valor]['jugador1']['puntuacion']),registro[valor]['jugador2']['nombre'],int(registro[valor]['jugador2']['puntuacion']),registro[valor]['jugador3']['nombre'],
    int(registro[valor]['jugador3']['puntuacion']),registro[valor]['jugador4']['nombre'],int(registro[valor]['jugador4']['puntuacion']),registro[valor]['jugador5']['nombre'],int(registro[valor]['jugador5']['puntuacion'])))
    print("\nPulsa cualquier tecla para continuar")
    m.getch()
    
#menu
def menu():
    while True:
        clear()
        print('''
                1.Juego Normal
                2.Juego Personalizado
                3.Juego IA

                9.Salir
            ''')
        try: 
            modo = int(input("¿Qué modo quieres jugar? : "))
        except ValueError:
            print("Debes elegir un número del 1 al 3")
            time.sleep(1)
        else:
            if (modo > 0 and modo < 4) or modo == 9:
                if modo == 1:
                    menuJuegoNormal(IA = False)
                elif modo == 2:
                    print("estamos trabajando en ello")
                    time.sleep(2)
                    clear()
                elif modo == 3:
                    menuJuegoNormal(IA = True)
                else:
                    clear()
                    sys.exit()
            else:
                print("Debes elegir un número entre 1 y 3")
                time.sleep(1)

def menuJuegoNormal(IA):
    while True:
        clear()
        global eleccion
        print('''
            1. Modalidad simple (acierta un número entre 0 y 100)
            2. Modalidad intermedia (acierta un número entre 0 y 1.000)
            3. Modalidad avanzada (acierta un número entre 0 y 1.000.000)
            4. Modalidad extrema (acierta un número entre 0 y 1.000.000.000.000)

            9. Salir
        ''')
        try:
            eleccion = int(input("¿Que modalidad desea escoger? : "))
        except ValueError:
            print("Debes elegir un número del 1 al 4")
            time.sleep(1)
        else:
            if (eleccion > 0 and eleccion < 5) or eleccion == 9:
                if eleccion == 1:
                    comprobarRegistro()
                    simple(IA)
                elif eleccion == 2:
                    comprobarRegistro()
                    intermedio(IA)
                elif eleccion == 3:
                    comprobarRegistro()
                    avanzado(IA)
                elif eleccion == 4:
                    comprobarRegistro()
                    extremo(IA)
                elif eleccion == 9:
                    clear()
                    sys.exit()
            else:
                print("Debes elegir un número del 1 al 4")
                time.sleep(1)
            
                

#modalidades de Juego 

def simple(IA):
    minimo = 0
    maximo = 100
    num_intento = 0
    nAleatorio = random.randint((minimo+1),(maximo-1))
    jugar(num_intento,minimo,maximo,nAleatorio,IA)

def intermedio(IA):
    minimo = 0
    maximo = 1000
    num_intento = 0
    nAleatorio = random.randint((minimo+1),(maximo-1))
    jugar(num_intento,minimo,maximo,nAleatorio,IA)

def avanzado(IA):
    minimo = 0
    maximo = 1000000
    num_intento = 0
    nAleatorio = random.randint((minimo+1),(maximo-1))
    jugar(num_intento,minimo,maximo,nAleatorio,IA)

def extremo(IA):
    minimo = 0
    maximo = 1000000000000
    num_intento = 0
    nAleatorio = random.randint((minimo+1),(maximo-1))
    jugar(num_intento,minimo,maximo,nAleatorio,IA)

#juego

def jugar(num_intento,minimo,maximo,nAleatorio,IA):    
    clear()
    while True:
        num_usuario = comprobacion(texto_repetido,minimo,maximo,IA)
        num_intento,maximo,minimo = resultado(num_usuario,num_intento,nAleatorio,minimo,maximo)


def comprobacion(texto,minimo,maximo,IA): #comprobar si el numero es correcto
    if IA == False:
        texto += "entre " + str(minimo) + " y " + str(maximo) + ": "
        while True:        
            try:
                num_usuario = int(input(texto))
            except:
                pass
            if 'num_usuario' in locals():
                if num_usuario >= minimo and num_usuario <= maximo:
                    return num_usuario
                else:
                    print("Su número tiene que estar entre ",minimo, " y ",maximo)
                    time.sleep(2)
                    clear()
            else: 
                print("Debe seleccionar un número, no una letra.")
                time.sleep(2)
                clear()
    else:
        num_IA = random.randint((minimo+1),(maximo-1))
        print(texto,"entre " + str(minimo) + " y " + str(maximo) + ": ",num_IA)
        return num_IA

def resultado(num_usuario,num_intento,num_aleatorio,minimo,maximo):
    num_intento += 1
    if num_usuario == num_aleatorio:
        print("victoria\nTotal de numero de intentos:",num_intento)
        time.sleep(3)
        puntuaciones(num_intento)
    elif num_usuario > num_aleatorio:
        print("El numero introducido",num_usuario, "es demasiado alto.")
        print("Tu número de intentos es de",num_intento)
        maximo = num_usuario
        time.sleep(2)
        clear()
        return num_intento,maximo,minimo
    else:
        print("El numero introducido",num_usuario, "es demasiado bajo.")
        print("Tu número de intentos es de",num_intento)
        minimo = num_usuario
        time.sleep(2)
        clear()
        return num_intento,maximo,minimo

def puntuaciones(intentos):
    if eleccion == 1:
        MIN = 0
        MAX = 6
        calc(MIN,MAX,intentos,1)
    elif eleccion == 2:
        MIN = 6
        MAX = 12    
        calc(MIN,MAX,intentos,1)
    elif eleccion == 3:
        MIN = 13
        MAX = 24    
        calc(MIN,MAX,intentos,2)
    elif eleccion == 4:
        MIN = 30
        MAX = 40    
        calc(MIN,MAX,intentos,2)


def calc(MIN,MAX,intentos,x):
    if intentos <= MIN:
        registrarNombre(10000)
    elif intentos > MIN and intentos < MAX:
        num = MAX - intentos
        num = num * (2000 / x)
        registrarNombre(num)
    elif intentos < (MAX+(5*x)):
        MAX = MAX+5*x
        num = MAX - intentos
        num = num * (200 / x)  
        registrarNombre(num)        
    elif intentos < (MAX+10*x):
        MAX = MAX+10*x
        num = MAX - intentos 
        num = num * (20 / x)
        registrarNombre(num)        
    else:
        registrarNombre(0)

texto_repetido = "Seleccione un número "
def comprobarRegistro():
    try:
        os.mkdir('dir1')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    global registro
    registro = {
        'simple':{
            'jugador1':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador2':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador3':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador4':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador5':{
                'nombre':'',
                'puntuacion':0
                        }
                },
        'intermedio':{
            'jugador1':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador2':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador3':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador4':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador5':{
                'nombre':'',
                'puntuacion':0
                        }
                },
        'avanzado':{
            'jugador1':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador2':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador3':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador4':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador5':{
                'nombre':'',
                'puntuacion':0
                        }
                },
        'extremo':{
            'jugador1':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador2':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador3':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador4':{
                'nombre':'',
                'puntuacion':0
                        },
            'jugador5':{
                'nombre':'',
                'puntuacion':0
                        }
                }
    }
    if eleccion == 1:
        try:
            open('dir1/puntuaciones_simple')
        except FileNotFoundError:
            with open('dir1/puntuaciones_simple','wb') as carpickle:
                pickle.dump(registro,carpickle)
        else:      
            with open('dir1/puntuaciones_simple','rb') as carpickle:
                registro=pickle.load(carpickle) 
    elif eleccion == 2:
        try:
            open('dir1/puntuaciones_intermedia')
        except FileNotFoundError:
            with open('dir1/puntuaciones_intermedia','wb') as carpickle:
                pickle.dump(registro,carpickle)
        else:      
            with open('dir1/puntuaciones_intermedia','rb') as carpickle:
                registro=pickle.load(carpickle) 
    elif eleccion == 3:
        try:
            open('dir1/puntuaciones_avanzado')
        except FileNotFoundError:
            with open('dir1/puntuaciones_avanzado','wb') as carpickle:
                pickle.dump(registro,carpickle)
        else:      
            with open('dir1/puntuaciones_avanzado','rb') as carpickle:
                registro=pickle.load(carpickle) 
    elif eleccion == 4:
        try:
            open('dir1/puntuaciones_extremo')
        except FileNotFoundError:
            with open('dir1/puntuaciones_extremo','wb') as carpickle:
                pickle.dump(registro,carpickle)
        else:      
            with open('dir1/puntuaciones_extremo','rb') as carpickle:
                registro=pickle.load(carpickle) 


if __name__ == '__main__':
    clear()
    menu()


