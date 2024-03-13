from config import COLOR_CUERPO_TITULO, COLOR_CUERPO_INFORMACION, TITULOS, TEXTO, SUBTITULO
import tkinter as tk
import utileria.util_img as util_img
import os, sys
#from tkinter import ttk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

#CREAMOS UNA CLASE
class CONCEPTOSBASICOS():

    #CREAMOS FUNCION DE INICIALIZACION
    def __init__(self, panel_principal,panel_titulo):
        print(panel_principal)

        '''elemento_1 = util_img.leer_imagen("p1/imagenes/Material/elementos_1.png", (1000,2000))
        elemento_2 = util_img.leer_imagen("p1/imagenes/Material/elementos_2.png", (1000, 2200))
        medidas = util_img.leer_imagen("p1/imagenes/Material/medidas_3.png", (50, 50))
        mru_1 = util_img.leer_imagen("p1/imagenes/Material/mru_4.png", (50, 50))
        mru_2 = util_img.leer_imagen("p1/imagenes/Material/mru_5.png", (50, 50))'''

        directory=os.path.dirname(__file__)
        movimiento_0 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/movimiento_0.png"))
        elemento_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/elementos_1.png"))
        elemento_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/elementos_2.png"))
        medidas = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/medidas_3.png"))
        mru_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mru_4.png"))
        mru_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mru_5.png"))
        
        #Control variable para video
        self.retry_play = True
        

        #CREAMOS LABELS (ESPACIOS DE TEXTO)
        # Creamos label para el titulo
        self.label_titulo = tk.Label(panel_titulo, 
                                     text="Conceptos básicos")
        self.label_titulo.config(fg="#ffffff", 
                                 font=(TITULOS, 30, "bold"), 
                                 bg=COLOR_CUERPO_TITULO)
        self.label_titulo.pack(side=tk.TOP, fill='both', expand=True)

        #
        self.label_introduccion=tk.Label(panel_principal,
                                         text="A continuacón se presenta algunos elementos primordiales sobre el movimiento a manera de resumen, así como elementos del Movimiento Rectilíneo Uniforme (MRU)\n que son una base para la comprensión del Movimiento Rectilíneo Uniformemente Acelerado (MRUA)",
                                         font=(TEXTO, 12),
                                         anchor="w",
                                         justify="left",
                                         padx=10,pady=10
                                         )
        self.label_introduccion.pack(side=tk.TOP, fill='both', expand=True)

        #Separador
        self.separador(panel_principal)

        # Creamos label para la informacion
        #Infografia 0
        self.label_elemento_1 = tk.Label(panel_principal,
                                        image=movimiento_0,
                                        )
        self.label_elemento_1.image=movimiento_0
        self.label_elemento_1.pack(side=tk.TOP)
        #Infografia 1
        self.label_elemento_1 = tk.Label(panel_principal,
                                        image=elemento_1,
                                        )
        self.label_elemento_1.image=elemento_1
        self.label_elemento_1.pack(side=tk.TOP)
        #Infografia 2
        self.label_elemento_2 = tk.Label(panel_principal,
                                        image=elemento_2,
                                        )
        self.label_elemento_2.image=elemento_2
        self.label_elemento_2.pack(side=tk.TOP)

        #Separador
        self.separador(panel_principal)

        #Infografia 3
        self.label_medidas = tk.Label(panel_principal,
                                        image=medidas,
                                    )
        self.label_medidas.image=medidas
        self.label_medidas.pack(side=tk.TOP)

        #Separador
        self.separador(panel_principal)

        #Infografia 4
        self.label_mru_1 = tk.Label(panel_principal,
                                        image=mru_1,
                                    )
        self.label_mru_1.image=mru_1
        self.label_mru_1.pack(side=tk.TOP)
        #Infografia 5
        self.label_mru_2 = tk.Label(panel_principal,
                                        image=mru_2,
                                    )
        self.label_mru_2.image=mru_2
        self.label_mru_2.pack(side=tk.TOP)

        #Separador
        self.separador(panel_principal)

        #Creamos frame para contener el video
        self.frame_cvcb_info=tk.Frame(panel_principal,
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
        self.frame_cvcb=tk.Frame(panel_principal,
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

        #lienzo_principal.bind()

        '''from expandir_menu import expandir_menu
        expandir_menu(barralateral)
        expandir_menu(barralateral)'''

    def mostrar_video(self):
        #Variable de control de video
        #global retry_play
        #Variable de control de video
        #global retry_play
        print("MOSTRAR VIDEO")
        directory=os.path.dirname(__file__)
        if self.retry_play==True:
            from ventanas.video_reproductor.mi_player_mpv import MiPlayerMPV
            V_P=MiPlayerMPV(self.frame_video, volumen=50)
            vd1= resource_path(directory+"/videos/CONCEPTOSBASICOS.mp4")
            V_P.reproduce(vd1,'00:00:00')
            V_P._teclas_rapidas_mi_player(self.frame_video)
            V_P.pack(fill='both', expand=1)
            self.retry_play=False
            #else:
                #pass
        '''print("MOSTRAR VIDEO")
        ventana_video=tk.Tk()
        ventana_video.geometry ("520x480")
        frame_video=tk.Frame(ventana_video)
        frame_video.pack(side="top",fill="both")
        from ventanas.video_reproductor.mi_player_mpv import MiPlayerMPV
        V_P=MiPlayerMPV(frame_video, volumen=50)
        vd1= "VOCALE.mp4"
        V_P.reproduce(vd1,'00:00:00')
        V_P._teclas_rapidas_mi_player(frame_video)
        V_P.pack(fill='both', expand=1)
        ventana_video.mainloop()'''

    def ocultar_video(self):
            #Variable de control de video
            
            for widget in self.frame_video.winfo_children():
                widget.pack_forget()
                widget.stop()
            self.retry_play=True

    #Funcion que crea un label como separador
    def separador (self, panel_principal):
        self.label_separador=tk.Label(panel_principal,
                                      bg=COLOR_CUERPO_TITULO)
        self.label_separador.pack(side=tk.TOP, fill='both', expand=True)

        '''#Configuramos las columnas de la tabla que organizara los titulos, enunciados y respuestas en el frame panel princiapl (p_informaciong) para que se redimencionen
        self.frame_vcb.columnconfigure(0, weight=1)
        self.frame_vcb.columnconfigure(1, weight=1)
        #Configuramos las filas de la tabla que organizara los graficos en el frame p_informacioncb para que se redimencionen
        self.frame_vcb.rowconfigure(0, weight=0)
        self.frame_vcb.rowconfigure(1, weight=0)
        self.frame_vcb.rowconfigure(2, weight=1)
        #
        self.boton_mostrar=tk.Button (self.frame_vcb,
                                      text="Mostrar video",
                                      command=self.mostrar_video)
        self.boton_mostrar.grid(row=0,column=0,padx=5,pady=5)
        self.label_mostrar=tk.Label(self.frame_vcb, text="Mostrar video")
        self.label_mostrar.grid(row=1,column=0)

        self.boton_esconder=tk.Button (self.frame_vcb,
                                       text="Ocultar video",
                                       command=self.ocultar_video)
        self.boton_esconder.grid(row=0,column=1,padx=5,pady=5)
        self.label_ocultar=tk.Label(self.frame_vcb, text="Ocultar video")
        self.label_ocultar.grid(row=1,column=1)
        self.frame_video=tk.Frame(self.frame_vcb,
                                bg="blue",
                                width=500,
                                height=500)
        self.frame_video.grid(row=2,column=0,columnspan=2,
                            padx=10,pady=10, sticky="snew")'''
    






    '''def mostrar_video(self):
            #Variable de control de video
            #global retry_play
            print("MOSTRAR VIDEO")
            if self.retry_play==True:
                from ventanas.mi_player_mpv import MiPlayerMPV
                V_P=MiPlayerMPV(self.frame_video, volumen=50)
                vd1= "VOCALE.mp4"
                V_P.reproduce(vd1,'00:00:00')
                V_P._teclas_rapidas_mi_player(self.frame_video)
                V_P.pack(fill='both', expand=1)
                self.retry_play=False
            #else:
                #pass

        def ocultar_video(self):
                #Variable de control de video
                
                for widget in self.frame_video.winfo_children():
                    widget.pack_forget()
                    widget.stop()
                self.retry_play=True'''


    # Creamos label para la informacion
    '''for self.label_informacioncb in range(0,2):
            self.label_informacioncb = tk.Label(panel_principal,
                                                image=logo,
                                                text=self.label_informacioncb 
                                                )
            self.label_informacioncb.config(fg="#222d33", 
                                        font=(TEXTO, 10), 
                                        bg="red")
            self.label_informacioncb.image = logo
            self.label_informacioncb.pack(side=tk.TOP) #place(x=0, y=0, relwidth=1, relheight=1)'''
            
        
    '''# CREAMOS FRAMES (ESPACIOS,PANELES)
        #PANEL DE TITULO
        #Creamos frame para titulo en el cuerpo_principal
        #lo empaquetamos y lo posicionamos en la parte superrior (TOP) y que ocupeel eje x, no se expande
        self.p_titulo = tk.Frame(panel_principal)
        self.p_titulo.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        # PANEL DE INFORMACION
        #Creamos frame para informacion en el cuerpo_principal
        #lo empaquetamos y lo posicionamos en la parte inferior (BOTTOM) y se expande
        self.p_informacioncb = tk.Frame(panel_principal)
        self.p_informacioncb.pack(side=tk.BOTTOM, fill='both', expand=True)
        #Configuramos las columnas de la tabla que organizara los el lienzo principal y scrollbar en el frame p_informacioncb para que se redimencionen
        self.p_informacioncb.columnconfigure(0, weight=1)
        self.p_informacioncb.columnconfigure(1, weight=0)
        #Configuramos las filas de la tabla que organizara los graficos en el frame p_informacioncb para que se redimencionen
        self.p_informacioncb.rowconfigure(0, weight=1)
        #CREAMOS LIENZO PRINCIPAL dentro del frame de informacion p_informacioncb que contiene otro frame donde se insertara la informacion
        #y para poder desplazarnos mediante YSCROLLBAR (barra de desplazamiento)
        self.lienzo_principal=tk.Canvas(self.p_informacioncb)
        #Se empaqueta el lienzo principal en grid fila=0,colum=0 para poner en la derecha la barra de desplzamiento
        self.lienzo_principal.grid(row=0,column=0, sticky="nsew")
        #Se crea un evento para que se pueda desplazar la barra de desplazamiento
        self.lienzo_principal.bind("<Configure>", lambda e: self.lienzo_principal.config(scrollregion = self.lienzo_principal.bbox("all")))
        #CREAMOS EL YSCROLLBAR O BARRA DE DESPLAZAMIENTO
        self.puente=ttk.Scrollbar(self.p_informacioncb,
                                  orient="vertical", 
                                  command=self.lienzo_principal.yview)
        #Empaquetamos la barra de desplzamiento hacia la derecha en fila=0,colum=1
        self.puente.grid(row=0,column=1,sticky="ns")
        self.lienzo_principal.config(yscrollcommand=self.puente.set)
        #Llamamos a funcion crear_frame_grafica para que cree un frame dentro de lienzo principal y podes desplazarnos con la barra
        self.crear_frame_informacioncb ()

        #CREAMOS LABELS (ESPACIOS DE TEXTO)
        # Creamos label para el titulo
        self.label_titulo = tk.Label(
            self.p_titulo, text="Conceptos básicos")
        self.label_titulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_TITULO)
        self.label_titulo.pack(side=tk.TOP, fill='both', expand=True)

        # Creamos label para la informacion
        self.label_informacioncb = tk.Label(self.p_informacioncb1, image=logo)
        self.label_informacioncb.config(fg="#222d33", font=("Roboto", 10), bg=COLOR_CUERPO_INFORMACION)
        self.label_informacioncb.pack(side=tk.TOP, fill='both', expand=True) #place(x=0, y=0, relwidth=1, relheight=1)
        

    #Creamos funcion para crear el frame que contiene la grafica
    def crear_frame_informacioncb(self):
        self.p_informacioncb1=tk.Frame(self.lienzo_principal, bg="red")
        #self.p_grafica1.pack(side=tk.LEFT)#grid(row=0,column=0)
        self.lienzo_principal.create_window((0,0),window=self.p_informacioncb1, anchor="nw")'''