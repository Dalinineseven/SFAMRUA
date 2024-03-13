from config import COLOR_CUERPO_PRINCIPAL,COLOR_CUERPO_TITULO,COLOR_CUERPO_SUBTITULO, COLOR_CUERPO_INFORMACION, TEXTO, TITULOS,SUBTITULO, BOTON_T, COLOR_BOTON_ACT,TIEMPO
import tkinter as tk
import random
import winsound
from math import cos, sin, radians,pi
import utileria.util_img as util_img
import os

#CREAMOS UNA CLASE
class EVALUACION():

    #CREAMOS FUNCION DE INICIALIZACION
    def __init__(self, panel_principal,panel_titulo):
        print(panel_principal)

        directory=os.path.dirname(__file__)

        #IMAGENES
        self.r_correcto = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-correcto.png", (50, 50))
        self.r_incorrecto = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-incorrecto.png", (50, 50))
        self.b_siguiente = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-siguiente.png", (80, 80))
        self.b_reintentar = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-reintentar.png", (80, 80))
        #NUMEROS
        self.r_c_0= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-0.png", (200, 200))
        self.r_c_1= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-1.png", (200, 200))
        self.r_c_2= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-2.png", (200, 200))
        self.r_c_3= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-3.png", (200, 200))
        self.r_c_4= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-4.png", (200, 200))
        self.r_c_5= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-5.png", (200, 200))
        self.r_c_6= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-6.png", (200, 200))
        self.r_c_7= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-7.png", (200, 200))
        self.r_c_8= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-8.png", (200, 200))
        self.r_c_9= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-9.png", (200, 200))
        self.r_c_10= util_img.leer_imagen(directory+"/imagenes/Calificacion/icons8-10.png", (200, 200))
        #SOLUCIONES
        self.r_p1 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta1.png", (900, 320))
        self.r_p2 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta2.png", (900, 320))
        self.r_p3 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta3.png", (900, 320))
        self.r_p4 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta4.png", (900, 320))
        self.r_p5 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta5.png", (900, 320))
        self.r_p6 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta6.png", (900, 320))
        self.r_p7 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta7.png", (900, 320))
        self.r_p8 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta8.png", (900, 320))
        self.r_p9 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta9-10.png", (900, 320))
        self.r_p11 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta11.png", (900, 320))
        self.r_p12 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta12.png", (900, 320))
        self.r_p13 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta13.png", (900, 320))
        self.r_p14 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta14.png", (900, 320))
        self.r_p15 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta15.png", (900, 320))
        self.r_p16 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta16.png", (900, 320))
        self.r_p17 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta17.png", (900, 320))
        self.r_p18 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta18.png", (900, 320))
        self.r_p19 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta19.png", (900, 320))
        self.r_p20 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta20.png", (900, 320))
        self.r_p21 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta21.png", (900, 320))
        self.r_p22 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta22.png", (900, 320))
        self.r_p23 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta23-24.png", (900, 320))
        self.r_p25 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta25.png", (900, 320))
        self.r_p26 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta26.png", (900, 320))
        self.r_p27 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta27.png", (900, 320))
        self.r_p28 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta28.png", (900, 320))
        self.r_p29 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta29.png", (900, 320))
        self.r_p30 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta30.png", (900, 320))
        self.r_p31 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta31.png", (900, 320))
        self.r_p32 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta32.png", (900, 320))
        self.r_p33 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta33.png", (900, 320))
        self.r_p34 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta34.png", (900, 320))
        self.r_p35 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta35.png", (900, 320))
        self.r_p36 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta36.png", (900, 320))
        self.r_p37 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta37.png", (900, 320))
        self.r_p38 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta38.png", (900, 320))
        self.r_p39 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta39.png", (900, 320))
        self.r_p40 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta40.png", (900, 320))
        self.r_p41 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta41.png", (900, 320))
        self.r_p42 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta42.png", (900, 320))
        self.r_p43 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta43.png", (900, 320))
        self.r_p44 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta44.png", (900, 320))
        self.r_p45 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta45.png", (900, 320))
        self.r_p46 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta46.png", (900, 320))
        self.r_p47 = util_img.leer_imagen(directory+"/imagenes/Soluciones/Pregunta47.png", (900, 320))


        #
        self.p_numero= tk.IntVar
        self.p_numero=0
        self.respuestas_correctas= tk.IntVar
        self.respuestas_correctas= 0

        panel_titulo.config(bg=COLOR_CUERPO_PRINCIPAL)

        #CREAMOS LABELS (ESPACIOS DE TEXTO)
        # Creamos label para el titulo
        self.label_titulo = tk.Label(panel_titulo, 
                                     text="Control de conocimientos")
        self.label_titulo.config(fg="#ffffff", 
                                 font=(TITULOS, 30), 
                                 bg=COLOR_CUERPO_TITULO)
        self.label_titulo.pack(side=tk.TOP, fill='both', expand=True)
        
        #Contenedor de PROGRESSBAR
        self.progreso=tk.Canvas(panel_titulo,
                                border=0,
                                relief="solid",
                                width=105,
                                height=105,
                                bg=COLOR_CUERPO_PRINCIPAL)
        self.progreso.pack(side=tk.TOP)
        #
        self.nivel=0
        self.preg_num = 1

        self.preguntas()
        self.crear_interfaz_evaluacion(panel_principal,self.enunciado)
        self.progessbar()

    #PROGRESSBAR
    def progessbar(self):
        #global nivel,preg_num
        if self.preg_num<=10:
            self.progreso.create_oval(18,18,90,90,fill="",outline="",width=5)
            self.progreso.create_line(53,55,55+90*sin(radians(self.nivel)),55-90*cos(radians(self.nivel)),
                                        fill=COLOR_BOTON_ACT,width=20)
            self.progreso.create_line(53,55,55+90*sin(radians(self.nivel+10)),55-90*cos(radians(self.nivel+10)),
                                        fill=COLOR_BOTON_ACT,width=30)
            self.progreso.create_oval(0,0,108,108,fill="",outline=COLOR_CUERPO_PRINCIPAL,width=36)
            self.progreso.create_oval(13,13,95,95,fill="",outline=COLOR_CUERPO_TITULO,width=10)
            self.progreso.create_oval(36,36,71,71,fill="#fcc761",outline=COLOR_CUERPO_TITULO,width=5)
            self.progreso.create_text(53,53, text=self.preg_num,fill="white", font=(TIEMPO, 18, "bold"))
            self.nivel=self.nivel+31
            self.preg_num=self.preg_num+1
        else:
            #
            self.nivel=0
            self.preg_num = 1

    #CREAMOS LA LISTA CON LAS PREGUNTAS,RESPUESTAS Y SOLUCIONES
    def preguntas(self):
        self.enunciado=[
        ("¿ Qué significado tiene la variable Vo en la siguiente formula\n 'X=Xo+(Vo*t)+(((1/2)*a)*(t^2))' ?","Aceleración","Velocidad final","Velocidad inicial",self.r_p1),
        ("¿ Qué significado tiene la variable Xo en la siguiente formula\n 'X=Xo+(Vo*t)+(((1/2)*a)*(t^2))' ?","Posicion tangencial","Posición final","Posición inicial",self.r_p2),
        ("¿ Qué significado tiene la variable X en la siguiente formula\n 'X=Xo+(Vo*t)+(((1/2)*a)*(t^2))' ?","Posicion tangencial","Posición inicial","Posición final",self.r_p3),
        ("¿ Qué significado tiene la variable t en la siguiente formula\n 'X=Xo+(Vo*t)+(((1/2)*a)*(t^2))' ?","Tiempo tangencial","Tiempo lineal","Tiempo",self.r_p4),
        ("¿ Qué significado tiene la variable a en la siguiente formula\n 'X=Xo+(Vo*t)+(((1/2)*a)*(t^2))' ?","Posición","Desaceleración","Aceleración",self.r_p5),
        ("¿ Qué significado corresponden las siglas 'MRU' ?","Momento Rectilíneo Unilateral","Movimiento Rectangular Unidimencional","Movimiento Rectilíneo Uniforme",self.r_p6),
        ("¿ Qué significado corresponden las siglas 'MRUA' ?","Momento Rectilieo Unilateral Acelerado","Movimiento Recto Unidimensional Aprobado","Movimiento Rectilíneo Uniformemente Acelerado",self.r_p7),
        ("¿ El Movimiento Rectilíneo Uniformemente Acelerado es lo mismo\n que el Movimiento Rectilíneo Uniformemente Variado ?","Falso","No estoy seguro","Verdadero",self.r_p8),
        ("¿ El Movimiento Rectilíneo Uniformemente Acelerado es lo mismo\n que el Movimiento Rectilíneo Uniforme ?","Verdadero","No estoy seguro","Falso",self.r_p9),
        ("¿ Cual es la diferencia entre el MRU y el MRUA?","El MRU tiene una velocidad constante, en cambio el MRUA tiene una aceleración variada que influye a que la velocidad sea constante","El MRU tiene una velocidad variada, en cambio el MRUA tiene una aceleración que no influye a que la velocidad sea constante","El MRU tiene una velocidad constante, en cambio el MRUA tiene una aceleración que influye a que la velocidad no sea constante",self.r_p9),
        ("¿ La aceleración en el Movimiento Rectilíneo Uniformemente Acelerado es constante ?","Falso","No estoy seguro","Verdadero",self.r_p11),
        ("¿ La aceleración en el Movimiento Rectilíneo Uniformemente Acelerado es constante e igual a 0 ?","Verdadero","No estoy seguro","Falso",self.r_p12),
        ("¿ La aceleracion en el Movimiento Rectilíneo Uniforme aumenta con respecto al tiempo ?","Verdadero","No estoy seguro","Falso",self.r_p13),
        ("¿ La velocidad en el Movimiento Rectilíneo Uniformemente Acelerado es constante ?","Verdadero","No estoy seguro","Falso",self.r_p14),
        ("¿ La velocidad en el Movimiento Rectilíneo Uniformemente Acelerado aumenta o disminuye con respecto a la aceleración aplicada de manera uniforme ?","Falso","No estoy seguro","Verdadero",self.r_p15),
        ("¿ La velocidad en el Movimiento Rectilíneo Uniforme es constante ?","Falso","No estoy seguro","Verdadero",self.r_p16),
        ("¿ La velocidad en el Movimiento Rectilíneo Uniforme aumenta con respecto a una aceleracion distinta de 0 aplicada ?","Verdadero","No lo se","Falso",self.r_p17),
        (" La gráfica de la posición en función del tiempo (X(t)) en el Movimiento Rectilíneo Uniformemente Acelerado es una: ","Línea recta sin pendiente","Línea recta con pendiente","Parábola",self.r_p18),
        (" La gráfica de la velocidad en función del tiempo (V(t)) en el Movimiento Rectilíneo Uniformemente Acelerado es una: ","Línea recta sin pendiente","Parábola","Línea recta con pendiente",self.r_p19),
        (" La gráfica de la aceleracion en función del tiempo (a(t)) en el Movimiento Rectilíneo Uniformemente Acelerado es una: ","Parábola","Línea recta con pendiente","Línea recta sin pendiente",self.r_p20),
        (" La gráfica de la posición en funcion del tiempo (X(t)) en el Movimiento Rectilíneo Uniforme es una: ","Línea recta sin pendiente","Parábola","Línea recta con pendiente",self.r_p21),
        (" La gráfica de la velocidad en función del tiempo (V(t)) en el Movimiento Rectilíneo Uniforme es una: ","Línea recta con pendiente","Parábola","Línea recta sin pendiente",self.r_p22),
        (" El Movimiento de Caída Libre es un tipo de:","Movimiento Circular","Movimiento Rectilíneo Uniforme","Movimiento Rectilíneo Uniformemente Acelerado",self.r_p23),
        (" El Movimiento de Caída Libre es un tipo de Movimiento Rectilíneo Uniformemente Acelerado debiado a: ","Parte de una posición determinada, su movimiento es el linea recta\n de arriba hacia abajo y su velocidad no aumenta","Parte de una posición determinada, su movimiento es el linea recta de abajo hacia arriba\n y su velocidad no aumenta con respecto a la aceleración de la gravedad que se aplica","Parte de una posición determinada, su movimiento es el linea recta de arriba hacia abajo o viceversa\n y su velocidad aumenta o disminuye con respecto a la aceleración de la gravedad existente",self.r_p23),
        (" Seleccione la formula para encontrar la velocidad en un Movimiento Rectilíneo Uniformemente Acelerado ","(Vf-Vo)/t","(Vf-Vo)/a","Vo+a*t",self.r_p25),
        (" Seleccione la formula para encontrar la aceleración en un Movimiento Rectilíneo Uniformemente Acelerado ","(Vf-Vo)/a","Vo+a*t","(Vf-Vo)/t",self.r_p26),
        (" Seleccione la formula para encontrar el tiempo en un Movimiento Rectilíneo Uniformemente Acelerado ","(Vf-Vo)/t","Vo+a*t","(Vf-Vo)/a",self.r_p27),
        (" Seleccione la formula para encontrar la distancia o posición en un Movimiento Rectilíneo Uniformemente Acelerado ","Vo+a*t","(Vf-Vo)/a","Xo+(Vo*t)+(((1/2)*a)*(t^2))",self.r_p28),
        (" La aceleración esta definida por su unidad de medida en la magnitud: ","[Masa/(Tiempo)^2]","[Longitud*(Tiempo)^2]","[Longitud]/[(Tiempo)^2]",self.r_p29),
        (" La velocidad esta definida por su unidad de medida en la magnitud: ","[Longitud/(Tiempo)^2]","[Longitud*(Tiempo)^2]","[Longitud]/[Tiempo]",self.r_p30),
        (" La distancia o posición esta definida por su unidad de medida en la magnitud: ","[Masa]","[Tiempo]","[Longitud]",self.r_p31),
        (" El tiempo esta definido por su unidad de medida en la magnitud: ","[Masa]","[Longitud]","[Tiempo]",self.r_p32),
        ("¿ Cuánto tiempo demora un automóvil en alcanzar la velocidad de 80 km/h, si inicia con una velocidad 0 y una aceleración de 30 Km/h^2 ?","3 h","2 h 60 min","3 h 6 min",self.r_p33), #problema 1
        ("¿ Cuánto tiempo necesita un automóvil para alcanzar la velocidad de 11,11 m/s, si parte del reposo y tarda 10 s en recorrer 20 m ?","26,78 s","26 s","27,78 s",self.r_p34), #problema 5
        ("¿ Qué velocidad tiene un automóvil después de 15 segundos de partir del reposo con una aceleración de 20 m/s^2 ?","301 m/s","299 m/s","300 m/s",self.r_p35), #problema 2
        ("¿ Qué velocidad tiene un automóvil despues de 20 segundos de partir del reposo , si en 5 segundos recorre 20 m ?","34 m/s","30 m/s","32 m/s",self.r_p36),
        ("¿ Qué distancia recorrió un automóvil despues de 15 segundos de partir del reposo con una aceleracion de 20 m/s^2 ?","2251 m","2249 m","2250 m",self.r_p37), #problema2
        ("¿ Qué distancia recorrió un automóvil despues de 20 segundos de partir del reposo con una aceleracion de 40 m/s^2 ?","7990 m","7000 m","8000 m",self.r_p38),
        ("¿ Qué aceleración tiene un automóvil para que a los 5 segundos de partir del reposo alcance una velocidad de 25m/s ?","6 m/s^2","4 m/s^2","5 m/s^2",self.r_p39), #problema 4
        ("¿ Qué aceleración tiene un automóvil para que a los 20 segundos de partir del reposo alcance una velocidad de 40m/s ?","1,6 m/s^2","3 m/s^2","2 m/s^2",self.r_p40),
        (" Un automovil que transitaba con una velocidad constante aplica los frenos durante 25 segundos y recorre 400 metros hasta detenerse.\n Calcular: 1. ¿La velocidad antes de aplicar los frenos? 2.¿La desaceleración que produjeron los frenos? ","Vo=31 m/s, a=-1,4 m/s^2","Vo=30 m/s, a=-1,8 m/s^2","Vo=32 m/s, a=-1,6 m/s^2",self.r_p41), #problema 3
        (" Un automóvil parte del reposo con una aceleración constante de 0,2 m/s^2, transcurridos 2 minutos deja de acelerar y sigue con una velocidad constaste.\n Determinar: 1. ¿Cuantos metros recorrió en los 2 primeros minutos? 2. ¿Que distancia recorrio a la hora de la partida? ","X(2min)= 1400 m, X(1h)= 84900 m","X(2min)= 1450 m, X(1h)= 85960 m","X(2min)= 1440 m, X(1h)= 84960 m",self.r_p42), #problema 7
        (" Los mejores coches deportivos son capaces de acelerar desde el reposo hasta alcanzar una velocidad de 100 km/h en 10 s ¿Halle la aceleración en km/h^2? ","34000 km/h^2","39000km/h^2","36000 km/h^2",self.r_p43),
        (" Una motocicleta se mueve a una velocidad de 10 m/s, es frenada hasta alcanzar el reposo en una distancia de 20 m ¿Cual es la desaceleración? ","-2 m/s^2","2,5 m/s^2","-2,5 m/s^2",self.r_p44),
        (" Un auto se mueve con una velocidad de 20 m/s, cuando el conductor aplica los frenos desacelera uniformemente deteniendose en 4 segundos\n ¿Halle la distancia recorrida en el frenado?","41 m","39 m","40 m",self.r_p45),
        (" Un avión parte del resposo y recorre 196 m en 7 segundos para despegar ¿Cual es su aceleración?","10 m/s^2","7 m/s^2","8 m/s^2",self.r_p46),
        (" Un coche parte desde el reposo acelerando uniformemente con 1 m/s^2, a los 16 segundos ¿A qué distancia del punto de partida se encuentra ?","127 m","129 m","128 m",self.r_p47),
        (" Un coche que estaba en reposo acelera a razón de 1,2 m/s^2, mientras que una motocicleta aparece en el instante de acelerar el automovil con una velocidad constante de 10 m/s. Calcular: 1. ¿Cuanto tiempo se necesita para que el automóvil alcance a la motocicleta? 2. ¿Con que velocidad se mueve el automovil en el instante de encontrarse? 3. ¿Cuantos metros a recorrido para alcanzar la motocicleta? ","t=17 s, v= 21 m/s, x=166 m","t=17,67 s, v= 21,004 m/s, x=166,70 m","t=16,67 s, v= 20,004 m/s, x=166,73 m",""),
        ("","","","",""),
        ]


    #CREAMOS LA FUNCION DONDE SE CREA LA INTERFAZ EN LA QUE SE MOSTRARAN LAS PREGUNTAS, RESPUESTAS Y SOLUCIONES
    def crear_interfaz_evaluacion(self,panel_principal,enunciado):
        #CREAMOS LABELS (ESPACIOS DE TEXTO)
        #CREAMOS FRAME PARA INTEGRAR EL FORMATO DE PRESENTACION DE LAS PREGUNTAS
        self.panel_evaluacion=tk.Frame(panel_principal,
                                       #pady=10,
                                       #padx=10,
                                       bg=COLOR_CUERPO_PRINCIPAL)
        self.panel_evaluacion.pack(side=tk.TOP, fill='both', expand=False)

        # Creamos El modelo de grid que vamos a utilizar para insertar las preguntas, respuestas, soluciones
        #LABEL PREGUNTAS
        #Configuramos las columnas de la tabla que organizara los titulos, enunciados y respuestas en el frame panel princiapl (p_informaciong) para que se redimencionen
        self.panel_evaluacion.columnconfigure(0, weight=1)
        self.panel_evaluacion.columnconfigure(1, weight=0)
        #Configuramos las filas de la tabla que organizara los graficos en el frame p_informacioncb para que se redimencionen
        self.panel_evaluacion.rowconfigure(0, weight=0)
        self.panel_evaluacion.rowconfigure(1, weight=1)
        self.panel_evaluacion.rowconfigure(2, weight=0)
        self.panel_evaluacion.rowconfigure(3, weight=1)
        self.panel_evaluacion.rowconfigure(4, weight=1)
        self.panel_evaluacion.rowconfigure(5, weight=1)
        self.panel_evaluacion.rowconfigure(6, weight=1)

        #
        print("Pregunta nº "+str(self.p_numero))
        if self.p_numero != 10:
            self.p_numero+=1
            print("Pregunta nº "+str(self.p_numero))

            #
            
            print("Pregunta correcta: "+str(self.respuestas_correctas))

            #Titulo pregunta
            self.label_t_pregunta = tk.Label(self.panel_evaluacion,
                                        text="Pregunta:"
                                        )
            self.label_t_pregunta.config(fg="#222d33",
                                     anchor="w", 
                                        font=(SUBTITULO, 14), 
                                        bg=COLOR_CUERPO_INFORMACION,
                                        padx=5,pady=5)
            self.label_t_pregunta.grid(row=0,column=0,columnspan=2, sticky="snew")
            #Enunciado de la pregunta
            #Utilizamos la libreria random para generar un numero aleatorio para selecionar una pregunta de la lista
            self.numero_pregunta= random.randint(0, 47) #47
            self.label_e_pregunta = tk.Label(self.panel_evaluacion,
                                        text=enunciado[self.numero_pregunta][0]
                                        )
            self.label_e_pregunta.config(fg="#222d33",
                                     anchor="w", 
                                        font=(TEXTO, 12), 
                                        bg=COLOR_CUERPO_PRINCIPAL,
                                        padx=5,pady=5)
            self.label_e_pregunta.grid(row=1,column=0, sticky="snew")
            #RESPUESTAS
            #Ttitulo de la respuesta
            self.label_t_respuesta = tk.Label(self.panel_evaluacion,
                                        text="Respuestas:"
                                        )
            self.label_t_respuesta.config(fg="#222d33",
                                     anchor="w", 
                                        font=(SUBTITULO, 14), 
                                        bg=COLOR_CUERPO_INFORMACION,
                                        padx=5,pady=5)
            self.label_t_respuesta.grid(row=2,column=0,columnspan=2, sticky="snew")
            #Respuestas de la pregunta
            #Definimos la variable con la que se va a relacionar los radiobotones
            self.opcion_seleccionada=tk.StringVar()
            # Creamos los radiobotones asignandole los valores de la lista creada anteriormente (preguntas)
            '''for x in range(1,4):
                self.r_b_t_="self.radioboton_r_"+str(x)
                print(self.r_b_t_)
                self.r_b_t_ = tk.Radiobutton(self.panel_evaluacion,
                                            text=enunciado[self.numero_pregunta][x])
                self.r_b_t_.config(fg="#222d33",
                                    anchor="w", 
                                    font=(TEXTO, 12), 
                                    bg=COLOR_CUERPO_INFORMACION,
                                    padx=5,pady=5,
                                    variable=self.opcion_seleccionada,
                                    value=enunciado[self.numero_pregunta][x])
                self.r_b_t_.grid(row=(3+(x-1)),column=0, sticky="snew")'''
            #Radioboton 1
            self.radioboton_r_1=tk.Radiobutton(self.panel_evaluacion,
                                                text=enunciado[self.numero_pregunta][1])
            self.radioboton_r_1.config(fg="#222d33",
                                    anchor="w", 
                                    font=(TEXTO, 12), 
                                    bg=COLOR_CUERPO_PRINCIPAL,
                                    padx=5,pady=5,
                                    variable=self.opcion_seleccionada,
                                    value=enunciado[self.numero_pregunta][1])
            self.radioboton_r_1.grid(row=3,column=0, sticky="snew")
            #Radioboton 2
            self.radioboton_r_2=tk.Radiobutton(self.panel_evaluacion,
                                                text=enunciado[self.numero_pregunta][2])
            self.radioboton_r_2.config(fg="#222d33",
                                    anchor="w", 
                                    font=(TEXTO, 12), 
                                    bg=COLOR_CUERPO_PRINCIPAL,
                                    padx=5,pady=5,
                                    variable=self.opcion_seleccionada,
                                    value=enunciado[self.numero_pregunta][2])
            self.radioboton_r_2.grid(row=4,column=0, sticky="snew")
            #Radioboton 3
            self.radioboton_r_3=tk.Radiobutton(self.panel_evaluacion,
                                                text=enunciado[self.numero_pregunta][3])
            self.radioboton_r_3.config(fg="#222d33",
                                    anchor="w", 
                                    font=(TEXTO, 12), 
                                    bg=COLOR_CUERPO_PRINCIPAL,
                                    padx=5,pady=5,
                                    variable=self.opcion_seleccionada,
                                    value=enunciado[self.numero_pregunta][3])
            self.radioboton_r_3.grid(row=5,column=0, sticky="snew")
                #Imprimimos por consola los valores que recibe la variable de control de los radiobotones
            print(self.opcion_seleccionada.get())
            #Autoseleccionamos una opcion por defecto para que no se selecionen las 3 al mismo tiempo
            self.opcion_seleccionada.set(enunciado[self.numero_pregunta][1])
                

            #BOTONES
            #Label identificador de respuesta correcta o incorrecta
            self.label_respuesta_c_i=tk.Label(self.panel_evaluacion,
                                            text="Escoje una respuesta",
                                            font=(TEXTO, 10),
                                            bg=COLOR_CUERPO_PRINCIPAL,
                                            padx=5,pady=5,
                                            state="disabled")
            self.label_respuesta_c_i.grid(row=1,column=1, sticky="snew")
            #Boton de enviar respuesta
            self.button_responder=tk.Button(self.panel_evaluacion,
                                            text="Comprobar",
                                            font=(BOTON_T, 10),
                                            bg=COLOR_BOTON_ACT,
                                            padx=5,pady=5,
                                            bd=0,
                                            state="normal",
                                            command=self.comprobar_solucion)
            self.button_responder.grid(row=3,column=1,rowspan=3, sticky="snew")
        else:
            print("Respondiste correctamente:"+str(self.respuestas_correctas))
            #self.limpiar()
            self.puntaje()     

    #Creamos la funcion para comprobar la respuesta
    def comprobar_solucion(self):
        #self.button_solucion.config(state="normal")
        if self.opcion_seleccionada.get() == self.enunciado[self.numero_pregunta][3]:
            print("respuesta correcta")
            winsound.PlaySound('C:/Windows/Media/tada.wav', winsound.SND_FILENAME)
            #
            self.respuestas_correctas+=1
            print("Pregunta correcta: "+str(self.respuestas_correctas))
            '''for x in range(1,4):
                self.r_b_t_="self.radioboton_r_"+str(x)
                print(self.r_b_t_)
                self.r_b_t_ = tk.Radiobutton
                self.r_b_t_.config(state="disabled")'''
            self.radioboton_r_1.config(state="disabled")
            self.radioboton_r_2.config(state="disabled")
            self.radioboton_r_3.config(state="disabled")
            #hacer que cambie a una imagen de correcto
            self.button_responder.config(state="disabled")
            self.label_respuesta_c_i.config(state="normal",
                                            image=self.r_correcto,
                                            text="CORRECTO")
            self.boton_siguiente_pregunta()
        else:
            print("respuesta incorrecta")
            winsound.PlaySound('C:/Windows/Media/Windows Critical Stop.wav', winsound.SND_FILENAME)
            #
            print("Pregunta correcta: "+str(self.respuestas_correctas))

            self.radioboton_r_1.config(state="disabled")
            self.radioboton_r_2.config(state="disabled")
            self.radioboton_r_3.config(state="disabled")
            #hacer que cambie a una imagen de incorrecto
            self.button_responder.config(state="disabled")
            self.label_respuesta_c_i.config(state="normal",
                                            image=self.r_incorrecto,
                                            text="INCORRECTO")
            self.abrir_solucion()

    #Creamos la funcion para abrir la solucion a la respuesta
    def abrir_solucion(self):
        self.label_solucion=tk.Label(self.panel_evaluacion,
                                     image=self.enunciado[self.numero_pregunta][4],
                                     text=self.enunciado[self.numero_pregunta][3],
                                     bg=COLOR_CUERPO_PRINCIPAL)
        self.label_solucion.grid(row=6,column=0, sticky="snew")
        self.boton_siguiente_pregunta()

    #Creamos la funcion que cree y muestre la siguiente pregunta
    def boton_siguiente_pregunta(self):
        #Creamos el boton de siguiente pregunta
        self.button_siguiente=tk.Button(self.panel_evaluacion,
                                        image=self.b_siguiente,
                                        text="SIGUIENTE",
                                        font=(BOTON_T, 10),
                                        bg="#ffffff", #FCC419
                                        bd=0,
                                        padx=5,pady=5,
                                        state="normal",
                                        command=self.limpiar)
        self.button_siguiente.grid(row=6,column=1, sticky="snew")

    #Creamos la funcion para limpiar el enunciado, las respuestas y la solucion
    def limpiar(self):
        #Destruye los hijos (WIDGETS) que contiene el frame o panel principal
        for widget in self.panel_evaluacion.winfo_children():
            widget.destroy()
        #Llamamos a la funcion que crea la interfaz de la evaluacion
        self.panel_evaluacion.after(1000,self.crear_interfaz_evaluacion(self.panel_evaluacion,self.enunciado))
        self.progessbar()

    def puntaje (self):

        self.label_e_r_c=tk.Label(self.panel_evaluacion,
                                text="Respondiste correctamente: ",
                                font=(SUBTITULO,15),
                                bg=COLOR_CUERPO_SUBTITULO,
                                pady=10)
        self.label_e_r_c.grid(row=0,column=0,columnspan=2, sticky="snew")

        self.label_respuestas_correctas=tk.Label(self.panel_evaluacion,
                                                text=str(self.respuestas_correctas),
                                                bg=COLOR_CUERPO_PRINCIPAL,
                                                )
        self.label_respuestas_correctas.grid(row=1,column=0,columnspan=2,rowspan=4, sticky="snew",pady=80)

        self.label_reintentar=tk.Label(self.panel_evaluacion,
                                                text="¿ Deseas intentarlo denuevo ?",
                                                font=(SUBTITULO,15),
                                                bg=COLOR_CUERPO_INFORMACION,
                                                pady=10)
        self.label_reintentar.grid(row=5,column=0,columnspan=2, sticky="snew")

        self.button_reintentar=tk.Button(self.panel_evaluacion,
                                        image=self.b_reintentar,
                                        text="REINTENTAR",
                                        font=(BOTON_T, 10),
                                        bg=COLOR_CUERPO_INFORMACION,
                                        bd=0,
                                        padx=5,pady=10,
                                        state="normal",
                                        command=self.limpiar)
        self.button_reintentar.grid(row=6,column=0,columnspan=2, sticky="snew")

        if self.respuestas_correctas == 0:
            self.label_respuestas_correctas.config(image=self.r_c_0)
        elif self.respuestas_correctas == 1:
            self.label_respuestas_correctas.config(image=self.r_c_1)
        elif self.respuestas_correctas == 2:
            self.label_respuestas_correctas.config(image=self.r_c_2)
        elif self.respuestas_correctas == 3:
            self.label_respuestas_correctas.config(image=self.r_c_3)
        elif self.respuestas_correctas == 4:
            self.label_respuestas_correctas.config(image=self.r_c_4)
        elif self.respuestas_correctas == 5:
            self.label_respuestas_correctas.config(image=self.r_c_5)
        elif self.respuestas_correctas == 6:
            self.label_respuestas_correctas.config(image=self.r_c_6)
        elif self.respuestas_correctas == 7:
            self.label_respuestas_correctas.config(image=self.r_c_7)
        elif self.respuestas_correctas == 8:
            self.label_respuestas_correctas.config(image=self.r_c_8)
        elif self.respuestas_correctas == 9:
            self.label_respuestas_correctas.config(image=self.r_c_9)
        elif self.respuestas_correctas == 10:
            self.label_respuestas_correctas.config(image=self.r_c_10)

        self.respuestas_correctas=0
        self.p_numero=0

        self.progreso.after(1000,self.progreso.delete("all"))
        
        

        '''for self.label_informacioncb in range(0,50):
            self.label_informacioncb = tk.Label(panel_principal,
                                            text=self.label_informacioncb 
                                            )
            self.label_informacioncb.config(fg="#222d33", 
                                        font=("Roboto", 10), 
                                        bg=COLOR_CUERPO_INFORMACION)
            self.label_informacioncb.pack(side=tk.TOP, fill='both', expand=True)'''