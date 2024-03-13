import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import subprocess
import winsound
#from tkinter import *
from config import COLOR_BARRA_SUPERIOR,COLOR_BARRA_LATERAL,COLOR_CUERPO_PRINCIPAL,COLOR_MENU_CURSOR_ENCIMA,TITULOS,BOTON_T,COLOR_SUBBOTON_DES,TIEMPO,SUBTITULO,COLOR_CUERPO_TITULO,TEXTO
import utileria.util_img as util_img
from ventanas.v_conceptosbasicos import CONCEPTOSBASICOS
from ventanas.v_mrua import MRUA
from ventanas.v_graficas import GRAFICAS
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)


class propuesta(tk.Tk):
    
    #Creamos funcion de inicio de programa
    def __init__(self):
        super().__init__()
        #Variable de control para el CRONOMETRO
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.contar = 0
        #Control de bajada de barra de desplazamiento
        self.c_baja=0.0
        #Control de video
        self.retry_play=True  
        #Control del submenu
        self.Submenu_cb_abierto=False
        self.Submenu_mrua_abierto=False
        #LLAMAMOS ESTILO DE LETRA A USAR
        #font_awesome = font.Font(family="FontAwesome", size=12)
        #LLAMA IMAGENES A USAR
        directory=os.path.dirname(__file__)
        self.logo = util_img.leer_imagen(directory+"/imagenes/utilizados/inicio_1.png", (1300, 750))
        self.menu_abierto = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-atras-r.png", (40, 40))
        self.menu_cerrado = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-menu-1-r.png", (40, 40))
        self.logo_grafico = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-grafico-a.png", (40, 40))
        self.logo_conceptos_b = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-conceptosb-a.png", (40, 40))
        self.logo_contenido = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-contenido-a.png", (40, 40))
        self.logo_evaluacion = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-evalua-a.png", (40, 40))
        self.logo_info = util_img.leer_imagen(directory+"/imagenes/utilizados/icons8-informacion-a.png", (40, 40))
        self.info_propuesta= util_img.leer_imagen(directory+"/imagenes/utilizados/informacion.png", (900, 700))
        #imagenes de submenu conceptos basicos
        self.movimiento_0 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/movimiento_0.png"))
        self.elemento_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/elementos_1.png"))
        self.elemento_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/elementos_2_1.png"))
        self.representacion = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/elementos_2_2.png"))
        self.medidas = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/medidas_3.png"))
        self.mru_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mru_4.png"))
        self.mru_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mru_5.png"))
        #imagenes de submenu MRUA
        self.mrua_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_6.png"))
        self.mrua_cara = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_7_1.png"))
        self.mrua_tipo = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_7_2.png"))
        self.mrua_g = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_8_1.png"))
        self.mrua_representacion = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_8_2.png"))
        self.mrua_f = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_9.png"))
        self.cl_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/cl_10.png"))
        self.cl_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/cl_11.png"))
        self.tv_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/tv_12.png"))
        self.tv_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/tv_13.png"))
        self.ej_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_14.png"))
        self.ej_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_15.png"))
        self.ej_3 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_16.png"))
        self.ej_4 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_17.png"))
        self.ej_5 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_18.png"))

        #self.perfil = util_img.leer_imagen("p2/imagenes/iconomenu.png", (100, 100))
        #Control de evaluacion
        self.v_evaluacion_abierta=False
        #LLAMA LAS FUNCIONES A USAR
        self.ventana_principal()
        self.paneles()
        self.elementosbs()
        self.elementosbl()
        self.controles_cuerpo()
        self.Label_logo=tk.Label(self.p_informaciong, image=self.logo)
        self.Label_logo.pack(side="left",fill="both",expand=True)
        self.cronometro()
        self.desplazar()
    
    #CREAMOS FUNCION DE CONFIGURACION DE VENTANA PRINCIPAL
    def ventana_principal (self):
        # Configuración inicial de la ventana
        directory=os.path.dirname(__file__)
        self.title('Aprende MRUA')
        self.iconbitmap(directory+"/AMRUA.ico")
        self.geometry("1500x750+20+20")
        #w, h = 1024, 600        
        #util_ventana.centrar_ventana(self, w, h)
        winsound.PlaySound('C:/Windows/Media/Bienvenida.wav', winsound.SND_FILENAME)

    #CREAMOS LA DISTRIBUCION DE LA VENTAMA PRINCIPAL (MAQUETA)
    def paneles (self):
        #Creamos un frame definido como encabezado, tomara un color definido en el archivo config.py de la variable establecida
        #El frame sera empaquetado en la parte superior y al centro (TOP), con fill ="both"
        self.barrasuperior= tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barrasuperior.pack(side=tk.TOP, fill="both")
        #Creamos un frame definido como barra lateral que sirve para el menu, tomara un color definido en el archivo config.py de la variable establecida
        #El frame sera empaquetado en la parte izquierda (LEFT), con fill ="both"
        self.barralateral= tk.Frame(self, bg=COLOR_BARRA_LATERAL, width=150)
        self.barralateral.pack(side=tk.LEFT, fill="both", expand=False)
        #Creamos un frame definido como barra lateral que sirve para el menu, tomara un color definido en el archivo config.py de la variable establecida
        #El frame sera empaquetado en la parte derecha (RIGHT), con fill ="both" que rellena todo lo restante en la pantalla
        self.cuerpoprincipal= tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpoprincipal.pack(side=tk.RIGHT, fill="both", expand=True)
        #
        self.barralateral.columnconfigure(0, weight=1)
        self.barralateral.columnconfigure(1, weight=1)

    #Creamos los elementos que contiene la BARRA SUPERIOR
    def elementosbs (self):
        #LLAMAMOS ESTILO DE LETRA A USAR Broadway
        #font_awesome = font.Font(family=BOTON_T, size=12)
        
        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barrasuperior, 
                                           image=self.menu_abierto,
                                           text="MENU", 
                                           font="BOTON_T",
                                           command=self.expandir_menu, 
                                           bd=0, 
                                           bg=COLOR_BARRA_SUPERIOR, 
                                           fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT, padx=20, pady=5)
        # Etiqueta de título
        self.labelMRUA = tk.Label(self.barrasuperior, text="AMRUA")
        self.labelMRUA.config(fg="#c63637", 
                              font=("Broadway", 20), 
                              bg=COLOR_BARRA_SUPERIOR, 
                              pady=10, width=9)
        self.labelMRUA.pack(side=tk.LEFT)

        #Frame para cronometro
        self.frame_cronometro=tk.Frame(self.barrasuperior,
                                       bg=COLOR_BARRA_SUPERIOR,
                                       padx=10,pady=5)
        self.frame_cronometro.pack(side=tk.RIGHT, fill="y")
        #Creamos empaquetado grid para cronometro
        #
        self.frame_cronometro.rowconfigure(0, weight=1)
        self.frame_cronometro.rowconfigure(1, weight=0)
        #Minutos
        self.label_crono_minutos=tk.Label(self.frame_cronometro,
                                        text="00",
                                        fg="#c63637", 
                                        font=(TIEMPO, 18, "bold"),
                                        bg=COLOR_BARRA_SUPERIOR)
        self.label_crono_minutos.grid(row=0,column=0, sticky="snew")
        #texto minutos
        self.label_texto_minutos=tk.Label(self.frame_cronometro,
                                        text="min",
                                        fg="#c63637", 
                                        font=(TIEMPO, 10),
                                        bg=COLOR_BARRA_SUPERIOR)
        self.label_texto_minutos.grid(row=1,column=0, sticky="snew")
        #:
        self.label_texto_dp=tk.Label(self.frame_cronometro,
                                        text=":",
                                        fg="#c63637", 
                                        font=(TIEMPO, 18, "bold"),
                                        bg=COLOR_BARRA_SUPERIOR)
        self.label_texto_dp.grid(row=0,column=1, sticky="snew")
        #Segundos
        self.label_crono_segundos=tk.Label(self.frame_cronometro,
                                        text="00",
                                        fg="#c63637", 
                                        font=(TIEMPO, 18, "bold"),
                                        bg=COLOR_BARRA_SUPERIOR)
        self.label_crono_segundos.grid(row=0,column=2, sticky="snew")
        #Texto segundos
        self.label_texto_segundos=tk.Label(self.frame_cronometro,
                                        text="seg",
                                        fg="#c63637", 
                                        font=(TIEMPO, 10),
                                        bg=COLOR_BARRA_SUPERIOR)
        self.label_texto_segundos.grid(row=1,column=2, sticky="snew")

        # Etiqueta de informacion
        self.labelMRUA = tk.Label(
            self.barrasuperior, text="SOFTWARE DE FÍSICA 'AMRUA'")
        self.labelMRUA.config(fg="#fff", 
                              font=(TITULOS, 18, "bold"), 
                              bg=COLOR_BARRA_SUPERIOR, 
                              padx=10, width=60)
        self.labelMRUA.pack(side=tk.RIGHT)
    
    #Creamos funcion para cronometrar los minutos de permanencia en el programa
    def cronometro(self):
        self.segundos=self.segundos+1
        self.label_crono_segundos.config(text=self.segundos)
        if self.segundos == 59:
            self.segundos = 00
            self.minutos=self.minutos+1
            self.label_crono_minutos.config(text=self.minutos)
        contar=self.frame_cronometro.after(1000,self.cronometro)

    #Creamos la funcion para expandir o retraer la BARRA LATERAL
    def expandir_menu(self):
        # Pregunta si esta visible o mapeado con (winfo_ismapped) el frame barralateral
        if self.barralateral.winfo_ismapped():
            #Si es verdadero desempaqueta el frame barralateral y lo esconde
            self.barralateral.pack_forget()
            #Cambia el boton del menu
            self.buttonMenuLateral.config(image=self.menu_cerrado)
            #Crea el frame donde se ubicaran los elemento de solo icono
            self.barralateral_si= tk.Frame(self, bg=COLOR_BARRA_LATERAL, width=150)
            #Empaquetamos hacia la izquierda la barra solo icono
            self.barralateral_si.pack(side=tk.LEFT, fill="both", expand=False)
            #Llamamos a la funcion solo icono para que cree y integre los iconos
            self.solo_icono()
        else:
            #Caso contrario empaqueta el frame barralateral, lo alinea a la izquierda
            #hace que se ajuste al eje Y
            self.barralateral.pack(side=tk.LEFT, fill='y')
            #cambia el boton del menu
            self.buttonMenuLateral.config(image=self.menu_abierto)
            #Desempaqueta el frame barralateral_si y lo esconde
            self.barralateral_si.pack_forget()

    #Creamos elementos que contiene BARRA LATERAL
    def elementosbl (self):

        # Configuración del menú lateral
        ancho_menu = 17
        alto_menu = 4
        font_awesome = font.Font(family=BOTON_T, size=14)

        # Crea los label que almacenaran los iconos del menu lateral
        self.label_c_b = tk.Label(self.barralateral)        
        self.label_mrua = tk.Label(self.barralateral)
        self.label_b_g = tk.Label(self.barralateral)        
        self.label_evaluacion = tk.Label(self.barralateral)
        self.label_info = tk.Label(self.barralateral) 
        
        # Botones del menú lateral
        self.botoncbasico = tk.Button(self.barralateral)
        self.botonmrua = tk.Button(self.barralateral)        
        self.botongrafica = tk.Button(self.barralateral)
        self.botonevaluacion = tk.Button(self.barralateral)        
        self.botoninfo = tk.Button(self.barralateral)

        # Creamos una lista, tupla que contenga variable de boton, texto a reflejar, comando, variable de label, icono y fila 
        #para empaquetarlo mediante metodo grid
        info_botones = [
            (self.botoncbasico ,"Conceptos básicos",self.abrir_conceptosbasicos, self.label_c_b,self.logo_conceptos_b,0),
            (self.botonmrua, "M R U A",self.abrir_mrua, self.label_mrua,self.logo_contenido,1),
            (self.botongrafica, "Gráficas",self.abrir_graficas, self.label_b_g,self.logo_grafico,2),
            (self.botonevaluacion, "Conocimientos",self.abrir_evaluacion, self.label_evaluacion,self.logo_evaluacion,3),
            (self.botoninfo, "Información",self.abrir_info, self.label_info,self.logo_info,4)]
        # Creamos un ciclo for para que incerte los valores de variable de boton, texto, icono, etc
        #y llame y envie al proceso o funcion configurar_boton_menu
        for button, text, comando, label, icon, fila in info_botones:
            self.configurar_boton_menu(button, text, comando, font_awesome, ancho_menu, alto_menu,label,icon,fila)                    
    
    #Creamos funcion para configurar los botones donde capturamos los datos definidos en la tupla o lista anterior
    #damos icono nombre, fuente, color de fondo, color de letra, ancho y alto
    def configurar_boton_menu(self, button, text, comando, font_awesome, ancho_menu, alto_menu,label,icon,fila):
        
        button.config(text=f"{text}", 
                      command=comando, 
                      anchor="w", 
                      font=font_awesome,
                      bd=0, 
                      bg=COLOR_BARRA_LATERAL, 
                      fg="white",
                      width=ancho_menu, 
                      height=alto_menu,
                      padx=10)
        #Lo empaquetamos y dentro del contenedor barralateral los situamos mediante grid para tener icono y texto    
        button.grid(row=fila,column=1,sticky="nsew") #pack(side=tk.TOP)
        #Le damos la imagen al label por medio de icono
        label.config(image=icon,
                     bg=COLOR_BARRA_LATERAL)
        #Lo empaquetamos y dentro del contenedor barralateral los situamos mediante grid para tener icono y texto
        label.grid(row=fila,column=0,sticky="nsew")

        #Capturamos la variable del boton en button y label para enviarla a eventos de desplazamiento
        self.eventos_desplazamiento(button, label)
#
    def Submenu_cb (self):
        if self.Submenu_cb_abierto==False:
            #self.borrar_submenu()
            #Creamos frame para contener botones
            '''self.canva_subboton= tk.Frame (self.barralateral,width=200, height=300, bg="red")
            self.canva_subboton.grid(row=0,column=2)'''
            self.canva_subboton= tk.Frame (self.cuerpoprincipal,width=200, height=300)
            self.canva_subboton.place(x=0,y=0)
            #Control de que el submenu esta abierto
            self.Submenu_cb_abierto=True
            #Crea botones
            '''self.subboton_cb1=tk.Button(self.canva_subboton, text="El movimiento", command=self.subboton_cb_1)
            self.subboton_cb1.pack()
            self.subboton_cb1=tk.Button(self.canva_subboton, text="Medidas")
            self.subboton_cb1.pack()
            self.subboton_cb1=tk.Button(self.canva_subboton, text="Representación gráfica")
            self.subboton_cb1.pack()'''
            self.subboton_cb1=tk.Button(self.canva_subboton)
            self.subboton_cb2=tk.Button(self.canva_subboton)
            self.subboton_cb3=tk.Button(self.canva_subboton)
            self.subboton_cb4=tk.Button(self.canva_subboton)
            self.subboton_cb5=tk.Button(self.canva_subboton)
            self.subboton_cb6=tk.Button(self.canva_subboton)
            info_subbotones = [
                                (self.subboton_cb1 ,"1. El movimiento",self.subboton_cb_1),
                                (self.subboton_cb2 ,"2. Elementos",self.subboton_cb_2),
                                (self.subboton_cb3 ,"3. Magnitudes",self.subboton_cb_3),
                                (self.subboton_cb4 ,"4. Representación",self.subboton_cb_4),
                                (self.subboton_cb5 ,"5. M R U",self.subboton_cb_5),
                                (self.subboton_cb6 ,"6. Vídeo",self.subboton_cb_6)
                            ]
            for button, text, comando in info_subbotones:
                self.configurar_boton_submenu(button, text, comando)
        else:
            print("EL MENU CB YA ESTA ABIERTO")

    def Submenu_mrua (self):
        if self.Submenu_mrua_abierto==False:
            #self.borrar_submenu()
            #Creamos frame para contener botones
            '''self.canva_subboton= tk.Frame (self.barralateral,width=200, height=300, bg="red")
            self.canva_subboton.grid(row=1,column=2)'''
            self.canva_subboton= tk.Frame (self.cuerpoprincipal,width=200, height=300)
            self.canva_subboton.place(x=0,y=110)
            #Control de que el submenu esta abierto
            self.Submenu_mrua_abierto=True
            #Crea botones
            self.subboton_mrua1=tk.Button(self.canva_subboton)
            self.subboton_mrua2=tk.Button(self.canva_subboton)
            self.subboton_mrua3=tk.Button(self.canva_subboton)
            self.subboton_mrua4=tk.Button(self.canva_subboton)
            self.subboton_mrua5=tk.Button(self.canva_subboton)
            self.subboton_mrua6=tk.Button(self.canva_subboton)
            self.subboton_mrua7=tk.Button(self.canva_subboton)
            self.subboton_mrua8=tk.Button(self.canva_subboton)
            self.subboton_mrua9=tk.Button(self.canva_subboton)
            self.subboton_mrua10=tk.Button(self.canva_subboton)
            self.subboton_mrua11=tk.Button(self.canva_subboton)
            info_subbotones = [
                                (self.subboton_mrua1 ,"1.- Definición",self.subboton_mrua_1),
                                (self.subboton_mrua2 ,"2.- Características",self.subboton_mrua_2),
                                (self.subboton_mrua3 ,"3.- Tipos",self.subboton_mrua_3),
                                (self.subboton_mrua4 ,"4.- Gráficas",self.subboton_mrua_4),
                                (self.subboton_mrua5 ,"5.- Representación",self.subboton_mrua_5),
                                (self.subboton_mrua6 ,"6.- Formulas",self.subboton_mrua_6),
                                (self.subboton_mrua7 ,"7.- Vídeo",self.subboton_mrua_7),
                                (self.subboton_mrua8 ,"8.- Ejercicios",self.subboton_mrua_8),
                                (self.subboton_mrua9 ,"9.- Caída libre",self.subboton_mrua_9),
                                (self.subboton_mrua10 ,"10.- Tiro vertical",self.subboton_mrua_10),
                                (self.subboton_mrua11 ,"11.- Vídeo ",self.subboton_mrua_11),

                            ]
            for button, text, comando in info_subbotones:
                self.configurar_boton_submenu(button, text, comando)
        else:
            print("EL MENU MRUA YA ESTA ABIERTO")

    def configurar_boton_submenu (self, button, text, comando):
        button.config(text=f"{text}", 
                      command=comando, 
                      anchor="w", 
                      font=(BOTON_T,12),
                      bd=0, 
                      bg=COLOR_BARRA_LATERAL, 
                      fg="white",
                      #width=ancho_menu, 
                      #height=alto_menu,
                      padx=10)
        #Lo empaquetamos y dentro del contenedor barralateral los situamos mediante grid para tener icono y texto    
        button.pack(side=tk.TOP, fill="both", expand=False) #grid(row=fila,column=1,sticky="nsew")
        self.eventos_desplazamiento_submenu(button)

#
    def subboton_cb_1(self):
        self.c_baja=0.0
        print("Ingresaste a El movimiento")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_cb_abierto=False
        #
        self.label_elemento_1 = tk.Label(self.p_informaciong,
                                        image=self.movimiento_0,
                                        )
        self.label_elemento_1.image=self.movimiento_0
        self.label_elemento_1.pack(side=tk.TOP)

    def subboton_cb_2(self):
        self.c_baja=0.0
        print("Ingresaste a elementos")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_cb_abierto=False
        #
        self.label_elemento_2 = tk.Label(self.p_informaciong,
                                        image=self.elemento_1,
                                        )
        self.label_elemento_2.image=self.elemento_1
        self.label_elemento_2.pack(side=tk.TOP)
        #
        self.label_elemento_3 = tk.Label(self.p_informaciong,
                                        image=self.elemento_2,
                                        )
        self.label_elemento_3.image=self.elemento_2
        self.label_elemento_3.pack(side=tk.TOP)
    def subboton_cb_3(self):
        self.c_baja=0.0
        print("Ingresaste a magnitudes")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_cb_abierto=False
        #
        self.label_elemento_4 = tk.Label(self.p_informaciong,
                                        image=self.medidas,
                                        )
        self.label_elemento_4.image=self.medidas
        self.label_elemento_4.pack(side=tk.TOP)
    def subboton_cb_4(self):
        self.c_baja=0.0
        print("Ingresaste a representación")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_cb_abierto=False
        #
        self.label_elemento_5 = tk.Label(self.p_informaciong,
                                        image=self.representacion,
                                        )
        self.label_elemento_5.image=self.representacion
        self.label_elemento_5.pack(side=tk.TOP)
    def subboton_cb_5(self):
        self.c_baja=0.0
        print("Ingresaste a MRU")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_cb_abierto=False
        #
        self.label_elemento_6 = tk.Label(self.p_informaciong,
                                        image=self.mru_1,
                                        )
        self.label_elemento_6.image=self.mru_1
        self.label_elemento_6.pack(side=tk.TOP)
        #
        self.label_elemento_7 = tk.Label(self.p_informaciong,
                                        image=self.mru_2,
                                        )
        self.label_elemento_7.image=self.mru_2
        self.label_elemento_7.pack(side=tk.TOP)
    def subboton_cb_6(self):
        self.c_baja=0.0
        print("Ingresaste a video")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_cb_abierto=False
        self.boton_video=1
        self.contenedor_video()


    def subboton_mrua_1(self):
        self.c_baja=0.0
        print("Ingresaste a elementos")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_1 = tk.Label(self.p_informaciong,
                                        image=self.mrua_1,
                                        )
        self.label_elemento_1.image=self.mrua_1
        self.label_elemento_1.pack(side=tk.TOP)
    def subboton_mrua_2(self):
        self.c_baja=0.0
        print("Ingresaste a magnitudes")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_2 = tk.Label(self.p_informaciong,
                                        image=self.mrua_cara,
                                        )
        self.label_elemento_2.image=self.mrua_cara
        self.label_elemento_2.pack(side=tk.TOP)
    def subboton_mrua_3(self):
        self.c_baja=0.0
        print("Ingresaste a representación")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_3 = tk.Label(self.p_informaciong,
                                        image=self.mrua_tipo,
                                        )
        self.label_elemento_3.image=self.mrua_tipo
        self.label_elemento_3.pack(side=tk.TOP)
    def subboton_mrua_4(self):
        self.c_baja=0.0
        print("Ingresaste a video")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_4 = tk.Label(self.p_informaciong,
                                        image=self.mrua_g,
                                        )
        self.label_elemento_4.image=self.mrua_g
        self.label_elemento_4.pack(side=tk.TOP)
    def subboton_mrua_5(self):
        self.c_baja=0.0
        print("Ingresaste a video")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_5 = tk.Label(self.p_informaciong,
                                        image=self.mrua_representacion,
                                        )
        self.label_elemento_5.image=self.mrua_representacion
        self.label_elemento_5.pack(side=tk.TOP)
    def subboton_mrua_6(self):
        self.c_baja=0.0
        print("Ingresaste a formulas")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_6 = tk.Label(self.p_informaciong,
                                        image=self.mrua_f,
                                        )
        self.label_elemento_6.image=self.mrua_f
        self.label_elemento_6.pack(side=tk.TOP)
    def subboton_mrua_7(self):
        self.c_baja=0.0
        print("Ingresaste a video")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        self.boton_video=2
        self.contenedor_video()
    def subboton_mrua_8(self):
        self.c_baja=0.0
        print("Ingresaste a ejercicios")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_11 = tk.Label(self.p_informaciong,
                                        image=self.ej_1,
                                        )
        self.label_elemento_11.image=self.ej_1
        self.label_elemento_11.pack(side=tk.TOP)
        #
        self.label_elemento_12 = tk.Label(self.p_informaciong,
                                        image=self.ej_2,
                                        )
        self.label_elemento_12.image=self.ej_2
        self.label_elemento_12.pack(side=tk.TOP)
        #
        self.label_elemento_13 = tk.Label(self.p_informaciong,
                                        image=self.ej_3,
                                        )
        self.label_elemento_13.image=self.ej_3
        self.label_elemento_13.pack(side=tk.TOP)
        #
        self.label_elemento_14 = tk.Label(self.p_informaciong,
                                        image=self.ej_4,
                                        )
        self.label_elemento_14.image=self.ej_4
        self.label_elemento_14.pack(side=tk.TOP)
        #
        self.label_elemento_15 = tk.Label(self.p_informaciong,
                                        image=self.ej_5,
                                        )
        self.label_elemento_15.image=self.ej_5
        self.label_elemento_15.pack(side=tk.TOP)

    def subboton_mrua_9(self):
        self.c_baja=0.0
        print("Ingresaste a caida libre")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_7 = tk.Label(self.p_informaciong,
                                        image=self.cl_1,
                                        )
        self.label_elemento_7.image=self.cl_1
        self.label_elemento_7.pack(side=tk.TOP)
        #
        self.label_elemento_8 = tk.Label(self.p_informaciong,
                                        image=self.cl_2,
                                        )
        self.label_elemento_8.image=self.cl_2
        self.label_elemento_8.pack(side=tk.TOP)
    def subboton_mrua_10(self):
        self.c_baja=0.0
        print("Ingresaste a tiro vertical")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        #
        self.label_elemento_9 = tk.Label(self.p_informaciong,
                                        image=self.tv_1,
                                        )
        self.label_elemento_9.image=self.tv_1
        self.label_elemento_9.pack(side=tk.TOP)
        #
        self.label_elemento_10 = tk.Label(self.p_informaciong,
                                        image=self.tv_2,
                                        )
        self.label_elemento_10.image=self.tv_2
        self.label_elemento_10.pack(side=tk.TOP)
    def subboton_mrua_11(self):
        self.c_baja=0.0
        print("Ingresaste a video")
        self.borrar_submenu()
        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        self.Submenu_mrua_abierto=False
        self.boton_video=3
        self.contenedor_video()


    def borrar_submenu (self):
        '''self.canva_subboton.grid_forget()'''
        self.canva_subboton.place_forget()

    #
    def contenedor_video(self):
        #Creamos frame para contener el video
        self.frame_cvcb_info=tk.Frame(self.p_informaciong,
                                bg="black",
                                #width=1000,
                                #height=600
                                )
        self.frame_cvcb_info.pack(side=tk.TOP,fill="both", expand=0)

        self.label_titulo_video=tk.Label(self.frame_cvcb_info,
                                         text="Vídeo explicativo",
                                         fg="white", 
                                         font=(TITULOS, 18, "bold"),
                                         bg=COLOR_CUERPO_TITULO,
                                         padx=10,pady=5)
        self.label_titulo_video.pack(side=tk.TOP, fill="both")

        self.label_instru_video=tk.Label(self.frame_cvcb_info,
                                         text="Instrucciones:",
                                         fg="white", 
                                         font=(SUBTITULO, 14, "bold"),
                                         bg=COLOR_CUERPO_TITULO,
                                         padx=10,pady=5,
                                         justify="left",
                                         anchor="w")
        self.label_instru_video.pack(side=tk.TOP, fill="both")

        self.label_info_video=tk.Label(self.frame_cvcb_info,
                                       text='''1. Si deseas visualizar el vídeo presiona en el botón "Mostrar vídeo".\n2. Una vez mostrado el vídeo puedes pausarlo o reproducirlo con el botón de reproducir ubicado en la parte inferior derecha.\n3. Para volver a reproducir el vídeo presiona el botón "Ocultar vídeo" y después el botón "Mostrar vídeo".''',
                                       fg="black", 
                                        font=(TEXTO, 12),
                                        padx=20,pady=5,
                                        justify="left",
                                        anchor="w")
        self.label_info_video.pack(side=tk.TOP,fill="both")
        
        self.label_impor_video=tk.Label(self.frame_cvcb_info,
                                         text="Importante:",
                                         fg="white", 
                                         font=(SUBTITULO, 14, "bold"),
                                         bg=COLOR_CUERPO_TITULO,
                                         padx=10,pady=5,
                                         justify="left",
                                         anchor="w")
        self.label_impor_video.pack(side=tk.TOP, fill="both")

        self.label_info_video=tk.Label(self.frame_cvcb_info,
                                       text='''*No olvides detener u ocultar el vídeo antes de dirigirte a otra opción del menú''',
                                       fg="black", 
                                        font=(TEXTO, 12, "bold"),
                                        padx=20,pady=5,
                                        justify="left",
                                        anchor="w")
        self.label_info_video.pack(side=tk.TOP,fill="both")

        #
        self.frame_cvcb=tk.Frame(self.p_informaciong,
                                bg="black",
                                #width=1000,
                                #height=600
                                )
        self.frame_cvcb.pack(side=tk.TOP,fill="both", expand=0)
        
        self.frame_i=tk.Frame(self.frame_cvcb)
        self.frame_i.pack(side=tk.LEFT,fill="y",expand=0)
        
        self.boton_mostrar=tk.Button (self.frame_i,
                                      text="Mostrar video",
                                      height=13,
                                      command=self.mostrar_video)
        self.boton_mostrar.pack(side="top",fill="y",expand=0,padx=5,pady=5)

        self.boton_esconder=tk.Button (self.frame_i,
                                       text="Ocultar video",
                                       height=13,
                                       command=self.ocultar_video)
        self.boton_esconder.pack(side="bottom",fill="y",expand=0,padx=5,pady=5)

        #Creamos frame para contener el video
        self.frame_d=tk.Frame(self.frame_cvcb,
                                bg="black",
                                width=900,
                                height=600
                                )
        self.frame_d.pack(side=tk.RIGHT,fill="both",expand=1,padx=160)

        self.frame_video=tk.Frame(self.frame_d,
                                bg="black",
                                width=800,
                                height=400
                                )
        self.frame_video.pack(side=tk.BOTTOM, fill="both", expand=1)

    def mostrar_video(self):
        print("MOSTRAR VIDEO")
        directory=os.path.dirname(__file__)
        if self.retry_play==True:
            if self.boton_video == 1:
                vd= resource_path(directory+"/videos/CONCEPTOSBASICOS.mp4")
            elif self.boton_video == 2:
                vd= resource_path(directory+"/videos/MRUA.mp4")
            elif self.boton_video == 3:
                vd= resource_path(directory+"/videos/TVYCL.mp4")

            from ventanas.video_reproductor.mi_player_mpv import MiPlayerMPV
            V_P=MiPlayerMPV(self.frame_video, volumen=50)
            V_P.reproduce(vd,'00:00:00')
            V_P._teclas_rapidas_mi_player(self.frame_video)
            V_P.pack(fill='both', expand=1)
            self.retry_play=False

    def ocultar_video(self):
            #Variable de control de video
            
            for widget in self.frame_video.winfo_children():
                widget.pack_forget()
                widget.stop()
            self.retry_play=True
    
    #Creamos la funcion de eventos de desplazamiento donde capturamos la variable de boton (button) y label
    #para asociarle un evento
    def eventos_desplazamiento_submenu(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.dentro_submenu(event, button))
        button.bind("<Leave>", lambda event: self.fuera_submenu(event, button))
        button.bind("<ButtonPress>", lambda event: self.lienzo_principal.yview_moveto(0.0))

    #Creamos el evento cuando el raton este dentro del boton
    #capturando el evento <Enter>
    def dentro_submenu(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')
    
    #Creamos el evento cuando el raton este fuera del boton
    #capturando el evento <Leave>
    def fuera_submenu(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_BARRA_LATERAL, fg='white')        

    #Creamos la funcion de eventos de desplazamiento donde capturamos la variable de boton (button) y label
    #para asociarle un evento
    def eventos_desplazamiento(self, button, label):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.dentro(event, button,label))
        button.bind("<Leave>", lambda event: self.fuera(event, button,label))
        button.bind("<ButtonPress>", lambda event: self.lienzo_principal.yview_moveto(0.0))

    #Creamos el evento cuando el raton este dentro del boton
    #capturando el evento <Enter>
    def dentro(self, event, button,label):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')
        label.config(bg=COLOR_MENU_CURSOR_ENCIMA)
        #
        '''print(self.Submenu_abierto, "a")
        if self.Submenu_abierto == True:
            self.Subboton()
            print("verdadero")
            #self.Submenu_abierto=False
        else:
            self.canva_subboton.grid_forget()
            print("negativo")
            self.Submenu_abierto=True'''

    #Creamos el evento cuando el raton este fuera del boton
    #capturando el evento <Leave>
    def fuera(self, event, button,label):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_BARRA_LATERAL, fg='white')
        label.config(bg=COLOR_BARRA_LATERAL)
        '''if self.Submenu_abierto==False:
            print("5 s")
            self.barralateral.after(2000,self.canva_subboton.grid_forget())
            self.Submenu_abierto=True'''
    
    #BARRA SOLO ICONOS
    #Creamos funcion para crear los elementos de la barra solo iconos
    def solo_icono (self):

        # Configuración del menú lateral solo icono
        ancho_menu = 100
        alto_menu = 100

        # Botones del menú lateral solo icono
        self.botoncbasico_si = tk.Button(self.barralateral_si)
        self.botonmrua_si = tk.Button(self.barralateral_si)        
        self.botongrafica_si = tk.Button(self.barralateral_si)
        self.botonevaluacion_si = tk.Button(self.barralateral_si)        
        self.botoninfo_si = tk.Button(self.barralateral_si)

        # Creamos una lista, tupla que contenga variable de boton solo icono, comando , icono y un numero que sera la fila para empaquetarlo con grid
        info_botones = [
            (self.botoncbasico_si,self.abrir_conceptosbasicos, self.logo_conceptos_b,0),
            (self.botonmrua_si,self.abrir_mrua,self.logo_contenido,1),
            (self.botongrafica_si,self.abrir_graficas,self.logo_grafico,2),
            (self.botonevaluacion_si,self.abrir_evaluacion,self.logo_evaluacion,3),
            (self.botoninfo_si,self.abrir_info,self.logo_info,4)]
        
        for button, comando, icon, fila in info_botones:
            self.configurar_boton_menu_si(button, comando, ancho_menu, alto_menu,icon,fila)                    
    
    #Creamos funcion para configurar los botones solo icono donde capturamos los datos definidos en la tupla o lista anterior
    #damos icono,coamndo, color de fondo, ancho y alto
    def configurar_boton_menu_si(self, button, comando, ancho_menu, alto_menu,icon,fila):
        
        button.config(image=icon, 
                      command=comando, 
                      anchor="center", 
                      bd=0, 
                      bg=COLOR_BARRA_LATERAL, 
                      width=ancho_menu, 
                      height=alto_menu,
                      padx=5)
        #Lo empaquetamos y dentro del contenedor barralateral los situamos en la parte central de arriba a abajo    
        button.grid(row=fila,column=0,sticky="nsew") #pack(side=tk.TOP)
        #Capturamos la variable del boton en button para enviarla a eventos de desplazamiento solo icono
        self.eventos_desplazamiento_si(button)

    #Creamos la funcion de eventos de desplazamiento donde capturamos la variable de boton (button) solo icono
    #para asociarle un evento
    def eventos_desplazamiento_si(self, button):
        # Asociar eventos Enter y Leave con la función dinámica en la barra solo icono
        button.bind("<Enter>", lambda event: self.dentro_si(event, button))
        button.bind("<Leave>", lambda event: self.fuera_si(event, button))
        button.bind("<ButtonPress>", lambda event: self.lienzo_principal.yview_moveto(0.0))
        

    #Creamos el evento cuando el raton este dentro del boton solo icono
    #capturando el evento <Enter>
    def dentro_si(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA)

    #Creamos el evento cuando el raton este fuera del boton solo icono
    #capturando el evento <Leave>
    def fuera_si(self, event, button,):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_BARRA_LATERAL)

    #Creamos el contenedor que almacenara informacion en el CUERPO PRINCIPAL
    def controles_cuerpo(self):
        # Informacion en el cuerpo principal
        '''label = tk.Label(self.cuerpoprincipal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)'''

        # CREAMOS FRAMES (ESPACIOS,PANELES)
        #PANEL DE TITULO
        #Creamos frame para titulo en el cuerpo_principal
        #lo empaquetamos y lo posicionamos en la parte superrior (TOP) y que ocupeel eje x, no se expande
        self.p_titulo = tk.Frame(self.cuerpoprincipal)
        self.p_titulo.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        # PANEL DE INFORMACION
        #Creamos frame para informacion en el cuerpo_principal
        #lo empaquetamos y lo posicionamos en la parte inferior (BOTTOM) y se expande
        self.p_informacion = tk.Frame(self.cuerpoprincipal)
        self.p_informacion.pack(side=tk.BOTTOM, fill='both', expand=True)
        #Configuramos las columnas de la tabla que organizara los el lienzo principal y scrollbar en el frame p_informacioncb para que se redimencionen
        self.p_informacion.columnconfigure(0, weight=1)
        self.p_informacion.columnconfigure(1, weight=0)
        #Configuramos las filas de la tabla que organizara los graficos en el frame p_informacioncb para que se redimencionen
        self.p_informacion.rowconfigure(0, weight=1)
        #CREAMOS LIENZO PRINCIPAL dentro del frame de informacion p_informacioncb que contiene otro frame donde se insertara la informacion
        #y para poder desplazarnos mediante YSCROLLBAR (barra de desplazamiento)
        self.lienzo_principal=tk.Canvas(self.p_informacion, bg=COLOR_CUERPO_PRINCIPAL)
        #Se empaqueta el lienzo principal en grid fila=0,colum=0 para poner en la derecha la barra de desplzamiento
        self.lienzo_principal.grid(row=0,column=0, sticky="nsew")
        #Se crea un evento para que se pueda desplazar la barra de desplazamiento
        self.lienzo_principal.bind("<Configure>", lambda e: self.lienzo_principal.config(scrollregion = self.lienzo_principal.bbox("all")))
        #CREAMOS EL YSCROLLBAR O BARRA DE DESPLAZAMIENTO
        self.puente=ttk.Scrollbar(self.p_informacion,
                                  orient="vertical", 
                                  command=self.lienzo_principal.yview)
        #Empaquetamos la barra de desplzamiento hacia la derecha en fila=0,colum=1
        self.puente.grid(row=0,column=1,sticky="ns")
        self.lienzo_principal.config(yscrollcommand=self.puente.set)
        #Llamamos a funcion crear_frame_grafica para que cree un frame dentro de lienzo principal y podes desplazarnos con la barra
        self.crear_frame_informacion ()

    #Creamos funcion para crear el frame que contiene la grafica
    def crear_frame_informacion(self):
        self.p_informaciong=tk.Frame(self.lienzo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        #self.p_grafica1.pack(side=tk.LEFT)#grid(row=0,column=0)
        self.lienzo_principal.create_window((0,0),window=self.p_informaciong, anchor="nw",width=1280) #1280 #800 #1410
        
    def desplazar(self):
        import keyboard
        keyboard.on_press_key("Down",lambda event: self.bajar(event))
        keyboard.on_press_key("Up",lambda event: self.subir(event))
        #self.label_mrua.bind("<Key>", lambda event: self.bajar(event))
        #self.lienzo_principal.bind("<ButtonPress>", lambda event:)
    def bajar(self,event):
        self.c_baja=self.c_baja+0.02
        self.lienzo_principal.yview_moveto(self.c_baja)
        print(event)
        if self.c_baja>=1.0:
            self.c_baja=1
    def subir(self,event):
        self.c_baja=self.c_baja-0.02
        self.lienzo_principal.yview_moveto(self.c_baja)
        print(event)
        if self.c_baja<=0.0:
            self.c_baja=0.0

    #Creamos una funcion para abrir la ventana conceptos basicos
    def abrir_conceptosbasicos(self):
        print(self.v_evaluacion_abierta)
        self.c_baja=0.0

        '''if self.Submenu_mrua_abierto==True:
            print("El submenu MRUA desaparecera")
            self.barralateral.after(500,self.borrar_submenu())
            #Control de que el submenu esta Cerrado
            self.Submenu_mrua_abierto=False
        elif self.Submenu_cb_abierto==True:
            print("El submenu CONCEPTOS BASICOS desaparecera")
            self.barralateral.after(5000,self.borrar_submenu())
            #Control de que el submenu esta Cerrado
            self.Submenu_cb_abierto=False
        else:
            print("Menu cerrado")'''

        if self.v_evaluacion_abierta == False :
            if self.Submenu_mrua_abierto==True:
                print("El submenu MRUA desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_mrua_abierto=False
            if self.Submenu_cb_abierto==True:
                print("El submenu CONCEPTOS BASICOS desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_cb_abierto=False
            else:
                self.Submenu_cb()
            self.limpiar_cuerpo(self.p_informaciong)
            self.limpiar_cuerpo(self.p_titulo)
            #self.crear_frame_informacion()
            #self.cuerpoprincipal.after(100,self.crear_frame_informacion)
            CONCEPTOSBASICOS(self.p_informaciong,self.p_titulo)
        else:
            self.salir_evaluacion()

    #Creamos una funcion para abrir la ventana conceptos basicos
    def abrir_mrua(self):
        print(self.v_evaluacion_abierta)
        self.c_baja=0.0

        '''if self.Submenu_abierto==True:
                print("El submenu desaparecera")
                self.barralateral.after(500,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_abierto=False
        else:
            print("Menu cerrado")'''
        
        if self.v_evaluacion_abierta == False :
            if self.Submenu_cb_abierto==True:
                print("El submenu MRUA desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_cb_abierto=False
            if self.Submenu_mrua_abierto==True:
                print("El submenu CONCEPTOS BASICOS desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_mrua_abierto=False
            else:
                self.Submenu_mrua()
            self.limpiar_cuerpo(self.p_informaciong)
            self.limpiar_cuerpo(self.p_titulo)
            MRUA(self.p_informaciong,self.p_titulo)
        else:
            self.salir_evaluacion()

    #Creamos funcion para abrir ventana graficos
    def abrir_graficas(self):
        print(self.v_evaluacion_abierta)
        self.c_baja=0.0

        '''if self.Submenu_abierto==True:
                print("El submenu desaparecera")
                self.barralateral.after(500,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_abierto=False
        else:
            print("Menu cerrado")'''

        if self.v_evaluacion_abierta == False :
            if self.Submenu_cb_abierto==True:
                print("El submenu MRUA desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_cb_abierto=False
            if self.Submenu_mrua_abierto==True:
                print("El submenu CONCEPTOS BASICOS desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_mrua_abierto=False
            self.limpiar_cuerpo(self.p_informaciong)
            self.limpiar_cuerpo(self.p_titulo)
            GRAFICAS(self.p_informaciong,self.p_titulo)
        else:
            self.salir_evaluacion()
        '''
            self.limpiar_cuerpo(self.cuerpoprincipal)
            GRAFICAS(self.cuerpoprincipal)
        '''
    
    def abrir_evaluacion(self):
        self.c_baja=0.0
        #Control de que evaluacion esta abierta
        self.v_evaluacion_abierta=True
        print(self.v_evaluacion_abierta)

        '''if self.Submenu_abierto==True:
                print("El submenu desaparecera")
                self.barralateral.after(500,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_abierto=False
        else:
            print("Menu cerrado")'''
        if self.Submenu_cb_abierto==True:
                print("El submenu MRUA desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_cb_abierto=False
        if self.Submenu_mrua_abierto==True:
                print("El submenu CONCEPTOS BASICOS desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_mrua_abierto=False

        self.limpiar_cuerpo(self.p_informaciong)
        self.limpiar_cuerpo(self.p_titulo)
        from ventanas.v_evaluacion import EVALUACION
        EVALUACION(self.p_informaciong,self.p_titulo)
        

    def salir_evaluacion(self):
        print(self.v_evaluacion_abierta)
        self.v_evaluacion_abierta=messagebox.askyesno("Salir del control de conocimientos", "¿ Estas seguro de salir del control de conocimientos ?\n\nEl progreso de perderá")
        if self.v_evaluacion_abierta == True:
            self.v_evaluacion_abierta = False
            self.abrir_conceptosbasicos()
        else:
            self.v_evaluacion_abierta = True
            pass

    #Creamos funcion para abrir ventana graficos
    def abrir_info(self):
        print(self.v_evaluacion_abierta)
        self.c_baja=0.0

        '''if self.Submenu_abierto==True:
                print("El submenu desaparecera")
                self.barralateral.after(500,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_abierto=False
        else:
            print("Menu cerrado")'''

        if self.v_evaluacion_abierta == False :
            if self.Submenu_cb_abierto==True:
                print("El submenu MRUA desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_cb_abierto=False
            if self.Submenu_mrua_abierto==True:
                print("El submenu CONCEPTOS BASICOS desaparecera")
                self.barralateral.after(200,self.borrar_submenu())
                #Control de que el submenu esta Cerrado
                self.Submenu_mrua_abierto=False
            self.limpiar_cuerpo(self.p_informaciong)
            self.limpiar_cuerpo(self.p_titulo)
            self.Label_propuesta_info=tk.Label(self.p_informaciong, image=self.info_propuesta)
            self.Label_propuesta_info.pack(side="left",fill="both",expand=True)
        else:
            self.salir_evaluacion()
    
    #Creamos funcion para lipiar cuerpo
    def limpiar_cuerpo(self,panel):
    #Destruye los hijos (WIDGETS) que contiene el frame o panel principal
        for widget in panel.winfo_children():
            widget.pack_forget()


app=propuesta()
app.mainloop()  