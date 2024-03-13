from config import COLOR_CUERPO_TITULO, COLOR_CUERPO_INFORMACION, TITULOS, TEXTO,SUBTITULO
import tkinter as tk
import utileria.util_img as util_img
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

#CREAMOS UNA CLASE
class MRUA():

    #CREAMOS FUNCION DE INICIALIZACION
    def __init__(self, panel_principal,panel_titulo):
        print(panel_principal)

        #Control variable para video
        self.retry_play = True
        
        #Inicializamos las imagenes en variables
        directory=os.path.dirname(__file__)
        mrua_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_6.png"))
        mrua_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_7.png"))
        mrua_3 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_8.png"))
        mrua_4 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/mrua_9.png"))
        cl_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/cl_10.png"))
        cl_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/cl_11.png"))
        tv_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/tv_12.png"))
        tv_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/tv_13.png"))
        ej_1 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_14.png"))
        ej_2 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_15.png"))
        ej_3 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_16.png"))
        ej_4 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_17.png"))
        ej_5 = tk.PhotoImage(file=resource_path(directory+"/imagenes/Material/ejercicios_18.png"))


        #CREAMOS LABELS (ESPACIOS DE TEXTO)
        # Creamos label para el titulo
        self.label_titulo = tk.Label(panel_titulo, 
                                     text="Movimiento Rectilíneo Uniformemente Acelerado (MRUA)")
        self.label_titulo.config(fg="#ffffff", 
                                 font=(TITULOS, 30, "bold"), 
                                 bg=COLOR_CUERPO_TITULO)
        self.label_titulo.pack(side=tk.TOP, fill='both', expand=True)
        #Parrafo de introduccion
        self.label_introduccion=tk.Label(panel_principal,
                                         text="Una vez abarcados y comprendidos los conceptos básicos del movimiento y del Movimiento Rectilíneo Uniforme pasamos a la comprension del \nMovimiento Rectilíneo Uniformemente Acelerado (MRUA), en este apartado visualizaremos su concepto, características, tipos, gráficas, formulas, además de algunos ejercicios.",
                                         font=(TEXTO, 12),
                                         anchor="w",
                                         justify="left",
                                         padx=10,pady=10
                                         )
        self.label_introduccion.pack(side=tk.TOP, fill='both', expand=True)

        #Separador
        self.separador(panel_principal)

        # Creamos label para la informacion
        #Infografia 1
        self.label_elemento_1 = tk.Label(panel_principal,
                                        image=mrua_1,
                                        )
        self.label_elemento_1.image=mrua_1
        self.label_elemento_1.pack(side=tk.TOP)
        #Infografia 2
        self.label_elemento_2 = tk.Label(panel_principal,
                                        image=mrua_2,
                                        )
        self.label_elemento_2.image=mrua_2
        self.label_elemento_2.pack(side=tk.TOP)
        #Infografia 3
        self.label_elemento_3 = tk.Label(panel_principal,
                                        image=mrua_3,
                                        )
        self.label_elemento_3.image=mrua_3
        self.label_elemento_3.pack(side=tk.TOP)
        
        #Separador
        self.separador(panel_principal)
        #Infografia 4
        self.label_elemento_4 = tk.Label(panel_principal,
                                        image=mrua_4,
                                        )
        self.label_elemento_4.image=mrua_4
        self.label_elemento_4.pack(side=tk.TOP)
        #Separador
        self.separador(panel_principal)
        

        #video
        #Creamos frame para contener el video
        self.frame_cvmrua_info=tk.Frame(panel_principal,
                                bg="black",
                                #width=1000,
                                #height=600
                                )
        self.frame_cvmrua_info.pack(side=tk.TOP,fill="both", expand=0)

        self.frame_cvmrua=tk.Frame(panel_principal,
                                bg="black",
                                #width=1000,
                                #height=600
                                )
        self.frame_cvmrua.pack(side=tk.TOP,fill="both", expand=0)
        self.boton_mrua=0
        self.esquema_video(self.frame_cvmrua_info,self.frame_cvmrua)
        

        #Infografia 5
        self.label_elemento_5 = tk.Label(panel_principal,
                                        image=cl_1,
                                        )
        self.label_elemento_5.image=cl_1
        self.label_elemento_5.pack(side=tk.TOP)
        #Infografia 6
        self.label_elemento_6 = tk.Label(panel_principal,
                                        image=cl_2,
                                        )
        self.label_elemento_6.image=cl_2
        self.label_elemento_6.pack(side=tk.TOP)
        
        #Separador
        self.separador(panel_principal)
        #Infografia 7
        self.label_elemento_7 = tk.Label(panel_principal,
                                        image=tv_1,
                                        )
        self.label_elemento_7.image=tv_1
        self.label_elemento_7.pack(side=tk.TOP)
        #Infografia 8
        self.label_elemento_8 = tk.Label(panel_principal,
                                        image=tv_2,
                                        )
        self.label_elemento_8.image=tv_2
        self.label_elemento_8.pack(side=tk.TOP)

        '''#DEFINIMOS LA FUNCION DEL BOTON PARA VIDEO
        def abrirvideo_mrua():
            print("BOTON ABRIR PRESIONADO")
            from ventanas.v_abrirvideo1 import Reproductor
            Reproductor()'''

        #Separador
        self.separador(panel_principal)

        #video
        #Creamos frame para contener el video
        self.frame_cvcl_info=tk.Frame(panel_principal,
                                bg="black",
                                #width=1000,
                                #height=600
                                )
        self.frame_cvcl_info.pack(side=tk.TOP,fill="both", expand=0)

        self.frame_cvcl=tk.Frame(panel_principal,
                                bg="black",
                                #width=1000,
                                #height=600
                                )
        self.frame_cvcl.pack(side=tk.TOP,fill="both", expand=0)
        self.boton_mrua=1
        self.esquema_video(self.frame_cvcl_info,self.frame_cvcl )

        #Separador
        self.separador(panel_principal)
        #Infografia 9
        self.label_elemento_9 = tk.Label(panel_principal,
                                        image=ej_1,
                                        )
        self.label_elemento_9.image=ej_1
        self.label_elemento_9.pack(side=tk.TOP)
        #Infografia 10
        self.label_elemento_10 = tk.Label(panel_principal,
                                        image=ej_2,
                                        )
        self.label_elemento_10.image=ej_2
        self.label_elemento_10.pack(side=tk.TOP)
        #Infografia 11
        self.label_elemento_11 = tk.Label(panel_principal,
                                        image=ej_3,
                                        )
        self.label_elemento_11.image=ej_3
        self.label_elemento_11.pack(side=tk.TOP)
        #Infografia 12
        self.label_elemento_12 = tk.Label(panel_principal,
                                        image=ej_4,
                                        )
        self.label_elemento_12.image=ej_4
        self.label_elemento_12.pack(side=tk.TOP)
        #Infografia 13
        self.label_elemento_13 = tk.Label(panel_principal,
                                        image=ej_5,
                                        )
        self.label_elemento_13.image=ej_5
        self.label_elemento_13.pack(side=tk.TOP)

    #Funcion que crea un label como separador
    def separador (self, panel_principal):
        self.label_separador=tk.Label(panel_principal,
                                      bg=COLOR_CUERPO_TITULO)
        self.label_separador.pack(side=tk.TOP, fill='both', expand=True)
    
    #DEFINIMOS LA FUNCION DEL BOTON PARA VIDEO
        
    def esquema_video(self,frame_v_info,frame_c_video):
         #
        self.label_titulo_video=tk.Label(frame_v_info,
                                         text="Vídeo explicativo",
                                         fg="white", 
                                         font=(TITULOS, 18, "bold"),
                                         bg=COLOR_CUERPO_TITULO,
                                         padx=10,pady=5)
        self.label_titulo_video.pack(side=tk.TOP, fill="both")

        self.label_instru_video=tk.Label(frame_v_info,
                                         text="Instrucciones:",
                                         fg="white", 
                                         font=(SUBTITULO, 14, "bold"),
                                         bg=COLOR_CUERPO_TITULO,
                                         padx=10,pady=5,
                                         justify="left",
                                         anchor="w")
        self.label_instru_video.pack(side=tk.TOP, fill="both")

        self.label_info_video=tk.Label(frame_v_info,
                                       text='''1. Si deseas visualizar el vídeo presiona en el botón "Mostrar vídeo".\n2. Una vez mostrado el vídeo puedes pausarlo o reproducirlo con el botón de reproducir ubicado en la parte inferior derecha.\n3. Para volver a reproducir el vídeo presiona el botón "Ocultar vídeo" y después el botón "Mostrar vídeo".''',
                                       fg="black", 
                                        font=(TEXTO, 12),
                                        padx=20,pady=5,
                                        justify="left",
                                        anchor="w")
        self.label_info_video.pack(side=tk.TOP,fill="both")
        
        self.label_impor_video=tk.Label(frame_v_info,
                                         text="Importante:",
                                         fg="white", 
                                         font=(SUBTITULO, 14, "bold"),
                                         bg=COLOR_CUERPO_TITULO,
                                         padx=10,pady=5,
                                         justify="left",
                                         anchor="w")
        self.label_impor_video.pack(side=tk.TOP, fill="both")

        self.label_info_video=tk.Label(frame_v_info,
                                       text='''*No olvides detener u ocultar el vídeo antes de dirigirte a otra opción del menú''',
                                       fg="black", 
                                        font=(TEXTO, 12, "bold"),
                                        padx=20,pady=5,
                                        justify="left",
                                        anchor="w")
        self.label_info_video.pack(side=tk.TOP,fill="both")

        #
        
        self.frame_i=tk.Frame(frame_c_video)
        self.frame_i.pack(side=tk.LEFT,fill="y",expand=0)

        if self.boton_mrua==0:
            self.boton_mostrar=tk.Button (self.frame_i,
                                        text="Mostrar video",
                                        height=13,
                                        command=self.mostrar_video_mrua)
            self.boton_mostrar.pack(side="top",fill="y",expand=0,padx=5,pady=5)
        else:
            self.boton_mostrar=tk.Button (self.frame_i,
                                        text="Mostrar video",
                                        height=13,
                                        command=self.mostrar_video_tvycl)
            self.boton_mostrar.pack(side="top",fill="y",expand=0,padx=5,pady=5)

        if self.boton_mrua==0:
            self.boton_esconder=tk.Button (self.frame_i,
                                        text="Ocultar video",
                                        height=13,
                                        command=self.ocultar_video_mrua)
            self.boton_esconder.pack(side="bottom",fill="y",expand=0,padx=5,pady=5)
        else:
            self.boton_esconder=tk.Button (self.frame_i,
                                       text="Ocultar video",
                                       height=13,
                                       command=self.ocultar_video_tvycl)
            self.boton_esconder.pack(side="bottom",fill="y",expand=0,padx=5,pady=5)
    
        #Creamos frame para contener el video
        if self.boton_mrua==0:
            self.frame_d_mrua=tk.Frame(frame_c_video,
                                    bg="black",
                                    width=900,
                                    height=600
                                    )
            self.frame_d_mrua.pack(side=tk.RIGHT,fill="both",expand=1,padx=160)

            self.frame_video_mrua=tk.Frame(self.frame_d_mrua,
                                    bg="black",
                                    width=800,
                                    height=400
                                    )
            self.frame_video_mrua.pack(side=tk.BOTTOM, fill="both", expand=1)
        else:
            self.frame_d_tvycl=tk.Frame(frame_c_video,
                                    bg="black",
                                    width=900,
                                    height=600
                                    )
            self.frame_d_tvycl.pack(side=tk.RIGHT,fill="both",expand=1,padx=160)

            self.frame_video_tvycl=tk.Frame(self.frame_d_tvycl,
                                    bg="black",
                                    width=800,
                                    height=400
                                    )
            self.frame_video_tvycl.pack(side=tk.BOTTOM, fill="both", expand=1)

    def mostrar_video_mrua(self):
        print("MOSTRAR VIDEO")
        directory=os.path.dirname(__file__)
        if self.retry_play==True:
            from ventanas.video_reproductor.mi_player_mpv import MiPlayerMPV
            V_P=MiPlayerMPV(self.frame_video_mrua, volumen=50)
            vd1=resource_path(directory+"/videos/MRUA.mp4")
            V_P.reproduce(vd1,'00:00:00')
            V_P._teclas_rapidas_mi_player(self.frame_video_mrua)
            V_P.pack(fill='both', expand=1)
            self.retry_play=False
            #else:
                #pass
    def mostrar_video_tvycl(self):
        print("MOSTRAR VIDEO")
        directory=os.path.dirname(__file__)
        if self.retry_play==True:
            from ventanas.video_reproductor.mi_player_mpv import MiPlayerMPV
            V_P=MiPlayerMPV(self.frame_video_tvycl, volumen=50)
            vd1=resource_path(directory+"/videos/TVYCL.mp4")
            V_P.reproduce(vd1,'00:00:00')
            V_P._teclas_rapidas_mi_player(self.frame_video_tvycl)
            V_P.pack(fill='both', expand=1)
            self.retry_play=False
            #else:
                #pass

    def ocultar_video_mrua(self):
            #Variable de control de video
            
            for widget in self.frame_video_mrua.winfo_children():
                widget.pack_forget()
                widget.stop()
            self.retry_play=True

    def ocultar_video_tvycl(self):
            #Variable de control de video
            
            for widget in self.frame_video_tvycl.winfo_children():
                widget.pack_forget()
                widget.stop()
            self.retry_play=True