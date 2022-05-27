
import tkinter
import tkinter.font as tkfont
import random
import time
from typing import Text

ventana = tkinter.Tk()
ventana.geometry("400x450")
ventana.title("juego dados")
ventana.resizable(0,0)

def bienvenida():
    ventana.geometry("300x400")
    font20 = tkfont.Font(family="System",size=20)
    bienvenido = tkinter.Label(ventana,text="bienvenido",bg="black",fg="#31B404",font=font20)
    bienvenido.place(relwidth=1,relheight=1)
    bienvenido.after(2000,lambda: [menu(),bienvenido.destroy()])

def menu():
    ventana.configure(bg="black")
    ventana.geometry("400x450")
    font = tkfont.Font(family="System",size=12)
    txt1 = tkinter.Label(ventana,text="¿Qué modalidad quieres probar?",fg="#31B404",bg="black",font=font)
    opcion1 = tkinter.Button(ventana,text="1. Modalidad simple",fg="#31B404",bg="black",font=font,borderwidth=0,cursor="hand2",command=lambda:simple())
    opcion2 = tkinter.Button(ventana,text="2. Modalidad intermedia",fg="#31B404",bg="black",font=font,borderwidth=0,cursor="hand2",command=lambda:intermedio())
    opcion3 = tkinter.Button(ventana,text="3. Modalidad avanzada",fg="#31B404",bg="black",font=font,borderwidth=0,cursor="hand2",command=lambda:avanzada())
    opcion4 = tkinter.Button(ventana,text="4. Modalidad extrema",fg="#31B404",bg="black",font=font,borderwidth=0,cursor="hand2",command=lambda:extrema())
    opcion5 = tkinter.Button(ventana,text="Salir",fg="#31B404",bg="black",font=font,borderwidth=0,cursor="hand2",command=lambda:salir())

    txt1.place(x=30,y=30)
    opcion1.place(x=30,y=80)
    opcion2.place(x=30,y=130)
    opcion3.place(x=30,y=180)
    opcion4.place(x=30,y=230)
    opcion5.place(x=20,y=400)

    opcion1.configure(activebackground="black",activeforeground="#31B404")
    opcion2.configure(activebackground="black",activeforeground="#31B404")
    opcion3.configure(activebackground="black",activeforeground="#31B404")
    opcion4.configure(activebackground="black",activeforeground="#31B404")
    opcion5.configure(activebackground="black",activeforeground="#31B404")

    #modalidades de juego

    def simple():
        minimo = 0
        maximo = 100
        nAleatorio = random.randint(minimo,maximo)
        clear()
        interfazJuego(minimo,maximo,nAleatorio)        
        

    def intermedio():
        minimo = 0
        maximo = 1000
        nAleatorio = random.randint(minimo,maximo)
        clear()
        interfazJuego(minimo,maximo,nAleatorio)   

    def avanzada():
        minimo = 0
        maximo = 1000000
        nAleatorio = random.randint(minimo,maximo)
        clear()
        interfazJuego(minimo,maximo,nAleatorio)   

    def extrema():
        minimo = 0
        maximo = 1000000000000
        nAleatorio = random.randint(minimo,maximo)
        clear()
        interfazJuego(minimo,maximo,nAleatorio) 

#interfaz del juego

def interfazJuego(minimo,maximo,nAleatorio):
    font16 = tkfont.Font(family="System",size=16,weight="bold")
    font20 = tkfont.Font(family="System",size=20,weight="bold")

    mostrarTexto = tkinter.Label(ventana,text="",fg="black",borderwidth=4,border=5, relief="groove")
    visual = tkinter.Label(ventana,font=font16)
    visual2= tkinter.Label(ventana,font=font16)
    botondel = tkinter.Button(ventana,text="DEL",font=font20,borderwidth=4,border=5, relief="groove",command=lambda: delete())
    boton0 = tkinter.Button(ventana,text="0",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(0))
    botonintro = tkinter.Button(ventana,text="INTRO",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:comprobacion(maximo,minimo,nAleatorio))
    boton1 = tkinter.Button(ventana,text="1",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(1))
    boton2 = tkinter.Button(ventana,text="2",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(2))
    boton3 = tkinter.Button(ventana,text="3",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(3))
    boton4 = tkinter.Button(ventana,text="4",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(4))
    boton5 = tkinter.Button(ventana,text="5",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(5))
    boton6 = tkinter.Button(ventana,text="6",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(6))
    boton7 = tkinter.Button(ventana,text="7",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(7))
    boton8 = tkinter.Button(ventana,text="8",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(8))
    boton9 = tkinter.Button(ventana,text="9",font=font20,borderwidth=4,border=5, relief="groove",command=lambda:calc(9))
    nIntentos = tkinter.Label(ventana,text=0)

    visual.config(text="")
    visual2.config(text="")

    mostrarTexto.place(x=30,y=30,width=340,height=100)
    visual.place(x=50,y=45)
    visual2.place(x=50,y=80)
    botondel.place(x=30,y=349,width=113,height=72)  
    boton0.place(x=143,y=349,width=113,height=72)  
    botonintro.place(x=256,y=349,width=113,height=72)  
    boton1.place(x=30,y=275,width=113,height=72)
    boton2.place(x=143,y=275,width=113,height=72)
    boton3.place(x=256,y=275,width=113,height=72)
    boton4.place(x=30,y=203,width=113,height=72)
    boton5.place(x=143,y=203,width=113,height=72)
    boton6.place(x=256,y=203,width=113,height=72)
    boton7.place(x=30,y=131,width=113,height=72)
    boton8.place(x=143,y=131,width=113,height=72)
    boton9.place(x=256,y=131,width=113,height=72)    
    
    def calc(n):    
        calculo = visual2.cget("text")
        calculo += str(n)
        visual2.config(text=calculo)

    def delete():
        visual2.config(text="")

    #juego
    def jugar(minimo,maximo): 
        txt(minimo,maximo)

    #texto

    def txt(minimo,maximo): #comprobar si el numero es correcto
        enunciado = "Elige un número entre {}  y {} : ".format(str(minimo),str(maximo))
        visual.config(text=enunciado)
    
    #comprobacion del intro

    def comprobacion(maximo,minimo,nAleatorio):
        num_usuario = visual2.cget("text")
        num_usuario = int(num_usuario)
        if num_usuario >= minimo and num_usuario <= maximo:
            resultado(num_usuario,nAleatorio)
        else:
            visual.config(text="Tu número debe ser entre {} y {} :".format(str(minimo),str(maximo)))
            visual2.config(text="")

    #mostrar resultado

    def resultado(num_usuario,nAleatorio):
        print(nAleatorio)
        if num_usuario == nAleatorio:
            num_intento = int(nIntentos.cget("text"))
            print("victoria\nTotal de numero de intentos:",num_intento)
            clear()
            victoria(num_intento)
        elif num_usuario > nAleatorio:
            visual.config(text="El numero {} es demasiado alto".format(num_usuario))
            visual2.config(text="")            
            num_intento = int(nIntentos.cget("text"))
            num_intento += 1
            nIntentos.config(text=num_intento)
        else:
            visual.config(text="El numero {} es demasiado bajo".format(num_usuario))
            visual2.config(text="")            
            num_intento = int(nIntentos.cget("text"))
            num_intento += 1
            nIntentos.config(text=num_intento)
    

    def victoria(num_intento):
        font20 = tkfont.Font(family="System",size=30)
        txtVictoria = tkinter.Label(ventana,text="V I C T O R I A",bg="black",fg="#31B404",font=font20)

        txtVictoria.place(relwidth=1,relheight=0.95)
        
        txtVictoria.after(400,lambda:loop(0))
        txtVictoria.after(800,lambda:loop(1))
        txtVictoria.after(1200,lambda:loop(2))
        txtVictoria.after(1600,lambda:loop(3))
        txtVictoria.after(2000,lambda:loop(4))
        txtVictoria.after(2400,lambda:loop(5))
        txtVictoria.after(2800,lambda:loop(6))
        txtVictoria.after(3200,lambda:loop(7))
        txtVictoria.after(3600,lambda:loop(8))
        txtVictoria.after(4000,lambda:loop(9))
        txtVictoria.after(4400,lambda:loop(10))
        txtVictoria.after(4800,lambda:loop(11))
        txtVictoria.after(5300,lambda:[clear(),intentos(num_intento)])

        txtVictoria.after(100,lambda:serpentina())

        def loop(x):
            
            dictColor = ["#2EFE64",
                        "#2EFE9A",
                        "#58FAD0",
                        "#58FAF4",
                        "#81DAF5",
                        "#81BEF7",
                        "#819FF7",
                        "#8181F7",
                        "#BCA9F5",
                        "#D0A9F5",
                        "#FA58D0",
                        "#FF0040"]
            txtVictoria.config(fg=dictColor[x])        

        def serpentina():
            ejey = 0
            mov = 0
            confeti1 = tkinter.Label(ventana,bg="green")
            confeti2 = tkinter.Label(ventana,bg="green")
            confeti3 = tkinter.Label(ventana,bg="green")
            confeti4 = tkinter.Label(ventana,bg="green")
            confeti5 = tkinter.Label(ventana,bg="green")
            confeti6 = tkinter.Label(ventana,bg="green")
            confeti7 = tkinter.Label(ventana,bg="green")
            confeti8 = tkinter.Label(ventana,bg="green")
            confeti9 = tkinter.Label(ventana,bg="green")
            confeti10 = tkinter.Label(ventana,bg="green")
            
            segundoConfeti1 = tkinter.Label(ventana,bg="green")
            segundoConfeti2 = tkinter.Label(ventana,bg="green")
            segundoConfeti3 = tkinter.Label(ventana,bg="green")
            segundoConfeti4 = tkinter.Label(ventana,bg="green")
            segundoConfeti5 = tkinter.Label(ventana,bg="green")
            segundoConfeti6 = tkinter.Label(ventana,bg="green")
            segundoConfeti7 = tkinter.Label(ventana,bg="green")
            segundoConfeti8 = tkinter.Label(ventana,bg="green")
            segundoConfeti9 = tkinter.Label(ventana,bg="green")
            segundoConfeti10 = tkinter.Label(ventana,bg="green")


            while ejey < 165:
                ejey += 1
                time.sleep(0.02)
                if mov < 20:
                    confeti1.place(x=10,y=ejey,width=5,height=10)
                    confeti2.place(x=50,y=ejey,width=5,height=10)
                    confeti3.place(x=90,y=ejey,width=5,height=10)
                    confeti4.place(x=130,y=ejey,width=5,height=10)
                    confeti5.place(x=170,y=ejey,width=5,height=10)
                    confeti6.place(x=210,y=ejey,width=5,height=10)
                    confeti7.place(x=250,y=ejey,width=5,height=10)
                    confeti8.place(x=290,y=ejey,width=5,height=10)
                    confeti9.place(x=330,y=ejey,width=5,height=10)
                    confeti10.place(x=370,y=ejey,width=5,height=10)

                    segundoConfeti1.place(x=15,y=(ejey-10),width=2,height=10)
                    segundoConfeti2.place(x=55,y=(ejey-10),width=2,height=10)
                    segundoConfeti3.place(x=95,y=(ejey-10),width=2,height=10)
                    segundoConfeti4.place(x=135,y=(ejey-10),width=2,height=10)
                    segundoConfeti5.place(x=175,y=(ejey-10),width=2,height=10)
                    segundoConfeti6.place(x=215,y=(ejey-10),width=2,height=10)
                    segundoConfeti7.place(x=255,y=(ejey-10),width=2,height=10)
                    segundoConfeti8.place(x=295,y=(ejey-10),width=2,height=10)
                    segundoConfeti9.place(x=335,y=(ejey-10),width=2,height=10)
                    segundoConfeti10.place(x=375,y=(ejey-10),width=2,height=10)

                    mov+=1
                elif mov >= 20:
                    if mov == 40:
                        mov = 0
                    confeti1.place(x=15,y=ejey,width=2,height=10)
                    confeti2.place(x=55,y=ejey,width=2,height=10)
                    confeti3.place(x=95,y=ejey,width=2,height=10)
                    confeti4.place(x=135,y=ejey,width=2,height=10)
                    confeti5.place(x=175,y=ejey,width=2,height=10)
                    confeti6.place(x=215,y=ejey,width=2,height=10)
                    confeti7.place(x=255,y=ejey,width=2,height=10)
                    confeti8.place(x=295,y=ejey,width=2,height=10)
                    confeti9.place(x=335,y=ejey,width=2,height=10)
                    confeti10.place(x=375,y=ejey,width=2,height=10)

                    segundoConfeti1.place(x=10,y=(ejey-10),width=5,height=10)
                    segundoConfeti2.place(x=50,y=(ejey-10),width=5,height=10)
                    segundoConfeti3.place(x=90,y=(ejey-10),width=5,height=10)
                    segundoConfeti4.place(x=130,y=(ejey-10),width=5,height=10)
                    segundoConfeti5.place(x=170,y=(ejey-10),width=5,height=10)
                    segundoConfeti6.place(x=210,y=(ejey-10),width=5,height=10)
                    segundoConfeti7.place(x=250,y=(ejey-10),width=5,height=10)
                    segundoConfeti8.place(x=290,y=(ejey-10),width=5,height=10)
                    segundoConfeti9.place(x=330,y=(ejey-10),width=5,height=10)
                    segundoConfeti10.place(x=370,y=(ejey-10),width=5,height=10)

                    mov+=1
                ventana.update()

    def intentos(num_intento):
        font20 = tkfont.Font(family="System",size=16)

        txtIntentos = tkinter.Label(ventana, text="Lo lograste en {} intentos".format(num_intento),bg="black",fg="#5882FA",font=font20)
        txtHacer = tkinter.Label(ventana, text="¿Qué quieres hacer ahora?",bg="black",fg="#31B404",font=font20)
        botonMenu = tkinter.Button(ventana,text="Ir a menú",fg="#31B404",bg="black",font=font20,borderwidth=0,cursor="hand2",command=lambda:[clear(),menu()])
        botonExit = tkinter.Button(ventana,text="Salir",fg="#31B404",bg="black",font=font20,borderwidth=0,cursor="hand2",command=lambda:salir())

        txtIntentos.place(relwidth=1,relheight=0.5)
        txtHacer.place(x=110,y=180)
        botonMenu.place(x=50,y=250)
        botonExit.place(x=280,y=250)

    jugar(minimo,maximo)

def clear():
    list = ventana.place_slaves()
    for l in list:
        l.destroy()
def salir():
    ventana.destroy()

bienvenida()

ventana.mainloop()