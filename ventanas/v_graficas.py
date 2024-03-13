#%matplotlib notebook
import tkinter as tk
from tkinter import ttk
#import numpy as np
from matplotlib.ticker import MultipleLocator
#import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import COLOR_CUERPO_TITULO,COLOR_CUERPO_PRINCIPAL,COLOR_CUERPO_INFORMACION,TITULOS,TEXTO,COLOR_BOTON_ACT,COLOR_BOTON_DES

#CREAMOS LA CLASE PARA LA VENTANA GRAFICAS
class GRAFICAS():
    #Creamos la funcion para iniciar el FRAME de grafica glpbal
    def __init__(self, panel_grafico, panel_titulo):
        #CREAMOS LABELS (ESPACIOS DE TEXTO)
        print(panel_grafico)
        # Creamos label para el titulo
        self.label_titulo = tk.Label(panel_titulo, 
                                     text="Graficas del MRUA")
        self.label_titulo.config(fg="#ffffff", 
                                 font=(TITULOS, 30), 
                                 bg=COLOR_CUERPO_TITULO)
        self.label_titulo.pack(side=tk.TOP, fill='both', expand=True)

        #Creamos frame para informacion en el cuerpo_principal
        #lo empaquetamos y lo posicionamos en la parte inferior (BOTTOM) y se expande
        self.p_informacion_g = tk.Frame(panel_titulo, 
                                      pady=10,
                                      padx=10,
                                      bg=COLOR_CUERPO_INFORMACION)
        self.p_informacion_g.pack(side=tk.TOP, fill='both', expand=True)

        #Redimencionamos la tabla o grid que contiene p_informacion (FRAME) con la ventana en sus columnas
        #--columnconfigure-- Da prioridades de redimencion a la columna especificada desde 0-n
        self.p_informacion_g.columnconfigure(0, weight=1)
        self.p_informacion_g.columnconfigure(1, weight=0)
        self.p_informacion_g.columnconfigure(2, weight=0)
        self.p_informacion_g.columnconfigure(3, weight=1)
        self.p_informacion_g.columnconfigure(4, weight=0)
        self.p_informacion_g.columnconfigure(5, weight=0)
        self.p_informacion_g.columnconfigure(6, weight=3)
        # Creamos label para etiquetas de INFORMACION
        #Creamos label para tiempo y se empaqueta en metodo grid o tabla
        self.label_tiempo = tk.Label(self.p_informacion_g, text="Ingrese el tiempo:")
        self.label_tiempo.config(fg="#222d33", 
                                 font=(TEXTO, 12), 
                                 bg=COLOR_CUERPO_INFORMACION, 
                                 padx=5,pady=5,
                                 width=20,)    
        self.label_tiempo.grid(row=0, column=0)
        self.label_um_tiempo = tk.Label(self.p_informacion_g, text="(s)")
        self.label_um_tiempo.config(fg="#222d33", 
                                 font=(TEXTO, 12), 
                                 bg=COLOR_CUERPO_INFORMACION, 
                                 #padx=5,pady=5,
                                 width=7)    
        self.label_um_tiempo.grid(row=0, column=2)
        #Creamos label para posicion y se empaqueta en metodo grid o tabla       
        self.label_posicion = tk.Label(self.p_informacion_g, text="Ingrese la posición:")
        self.label_posicion.config(fg="#222d33", 
                                   font=(TEXTO, 12), 
                                   bg=COLOR_CUERPO_INFORMACION, 
                                   padx=5,pady=5,
                                   width=20)    
        self.label_posicion.grid(row=1, column=0)
        self.label_um_posicion = tk.Label(self.p_informacion_g, text="(m)")
        self.label_um_posicion.config(fg="#222d33", 
                                   font=(TEXTO, 12), 
                                   bg=COLOR_CUERPO_INFORMACION, 
                                   #padx=5,pady=5,
                                   width=7)    
        self.label_um_posicion.grid(row=1, column=2)
        #Creamos label para velocidad inicial y se empaqueta en metodo grid o tabla
        self.label_velocidad_i = tk.Label(self.p_informacion_g, text="Ingrese la velocidad inicial:")
        self.label_velocidad_i.config(fg="#222d33", 
                                 font=(TEXTO, 12), 
                                 bg=COLOR_CUERPO_INFORMACION, 
                                 padx=5,pady=5,
                                 width=30)    
        self.label_velocidad_i.grid(row=0, column=3)
        self.label_um_velocidad_i = tk.Label(self.p_informacion_g, text="(m/s)")
        self.label_um_velocidad_i.config(fg="#222d33", 
                                 font=(TEXTO, 12), 
                                 bg=COLOR_CUERPO_INFORMACION, 
                                 #padx=5,pady=5,
                                 width=7)    
        self.label_um_velocidad_i.grid(row=0, column=5)
        #Creamos label para aceleracion y se empaqueta en metodo grid o tabla       
        self.label_aceleracion = tk.Label(self.p_informacion_g, text="Ingrese la aceleración:")
        self.label_aceleracion.config(fg="#222d33", 
                                   font=(TEXTO, 12), 
                                   bg=COLOR_CUERPO_INFORMACION, 
                                   padx=5,pady=5,
                                   width=30)    
        self.label_aceleracion.grid(row=1, column=3)
        self.label_um_aceleracion = tk.Label(self.p_informacion_g, text="(m/s^2)")
        self.label_um_aceleracion.config(fg="#222d33", 
                                   font=(TEXTO, 12), 
                                   bg=COLOR_CUERPO_INFORMACION,
                                   #padx=5,pady=5,
                                   width=7)    
        self.label_um_aceleracion.grid(row=1, column=5)
        #Creamos label para errores, sin ningun texto para despues modificarlo
        self.label_error = tk.Label(self.p_informacion_g, 
                                    text="* Ingrese todos los valores requeridos, si desconoce un valor ingrese '0'")
        self.label_error.config(fg="#222d33", 
                                font=(TEXTO, 12, "bold"), 
                                bg=COLOR_CUERPO_TITULO, 
                                padx=5,pady=5,
                                width=60)
        self.label_error.grid(row=2, column=0, columnspan=7, sticky="nsew")


        # CREAMOS ENTRY PARA ENTRADA DE DATOS
        #Creamos entry para tiempo y se empaqueta en metodo grid o tabla
        self.entry_tiempo = tk.Entry(self.p_informacion_g)
        #Damos atributos (.config): largo de 5 caracteres, alineado a la derecha, y estado normal para posteriormente desactivarlo
        self.entry_tiempo.config(width=5,
                                 justify="right",
                                 state="normal")
        self.entry_tiempo.grid(row=0, column=1, padx=10)
        #Creamos entry para posicion inicial y se empaqueta en metodo grid o tabla
        self.entry_posicion = tk.Entry(self.p_informacion_g)
        #Damos atributos (.config): largo de 5 caracteres, alineado a la derecha, y estado normal para posteriormente desactivarlo
        self.entry_posicion.config(width=5,
                                   justify="right",
                                   state="normal")
        self.entry_posicion.grid(row=1, column=1,padx=10)
        #Creamos entry para velocidad inicial y se empaqueta en metodo grid o tabla
        self.entry_velocidad_i = tk.Entry(self.p_informacion_g)
        #Damos atributos (.config): largo de 5 caracteres, alineado a la derecha, y estado normal para posteriormente desactivarlo
        self.entry_velocidad_i.config(width=5,
                                 justify="right",
                                 state="normal")
        self.entry_velocidad_i.grid(row=0, column=4, padx=10)
        #Creamos entry para aceleracion y se empaqueta en metodo grid o tabla
        self.entry_aceleracion = tk.Entry(self.p_informacion_g)
        #Damos atributos (.config): largo de 5 caracteres, alineado a la derecha, y estado normal para posteriormente desactivarlo
        self.entry_aceleracion.config(width=5,
                                   justify="right",
                                   state="normal")
        self.entry_aceleracion.grid(row=1, column=4,padx=10)

        # CREAMOS BOTONES
        # Creamos boton para ENVIAR DATOS a proceso o funcion graficar y damos atributos
        self.b_graficar = tk.Button(self.p_informacion_g, 
                                    text="GRAFICAR", 
                                    padx=10,pady=10, 
                                    bd=0,
                                    relief="ridge", 
                                    bg=COLOR_BOTON_ACT,
                                    command=self.graficar,
                                    state="normal")
        #Se empaqueta en metodo grid o tabla, 
        #sticky=expande alinea boton en direcciones norte,sur,este,oeste
        self.b_graficar.grid(row=0, column=6, sticky="nsew")
        
        # Creamos boton para NUEVO GRAFICO y enviarlo al proceso o funcion nuevo grafico y damos atributos
        self.b_nuevo_g = tk.Button(self.p_informacion_g, 
                                   text="NUEVO GRÁFICO", 
                                   padx=10,pady=10, 
                                   bd=0,
                                   relief="ridge", 
                                   bg=COLOR_BOTON_DES,
                                   command=self.nuevo_grafico,
                                   state="disabled")
        #Se empaqueta en metodo grid o tabla, 
        #sticky=expande alinea boton en direcciones norte,sur,este,oeste con siglas en ingles
        self.b_nuevo_g.grid(row=1, column=6, sticky="nsew")

        #CREAMOS FRAME PARA INTEGRAR EL GRAFICO EN EL PANEL PRINCIPAL (panel_grafico)
        #lo empaquetamos y lo posicionamos en la parte inferior (BOTTOM) y se expande
        self.p_grafica1 = tk.Frame(panel_grafico, 
                                      pady=10,
                                      padx=10,
                                      bg=COLOR_CUERPO_PRINCIPAL)
        self.p_grafica1.pack(side=tk.TOP, fill='both', expand=True)

        #Redimencionamos la tabla o grid que contiene p_informacion (FRAME) con la ventana en sus columnas
        #--columnconfigure-- Da prioridades de redimencion a la columna especificada desde 0-n
        #self.p_informacion.columnconfigure(0, weight=1)

        #Accion de boton graficar
    def graficar(self):
           #Iniciamos proceso
           try:
            #Creamos variables y obtenemos datos por metodo get() y las convertimos en vriables enteras y float
            tiempo=int(self.entry_tiempo.get())
            xi=float(self.entry_posicion.get())
            vi=float(self.entry_velocidad_i.get())
            a=float(self.entry_aceleracion.get())
            
            #Damos texto a label de error xq todo esta correcto
            self.label_error.config(text="")

            #Creamos lista donde se almacena los puntos para generar la grafica
            lista_posicion_final=self.l_p_f=[]
            variable_tiempo=self.v_t=[]
            lista_velocidad_final=self.l_v_f=[]
            #Imprimimos en consola los elementos que contienen las listas
            print(variable_tiempo,lista_posicion_final,lista_velocidad_final)
            #Imprimimos en consola las variables para ver contenido
            print(tiempo,xi,vi,a)

            #OJO: ESPACIO PARA INSERTAR TABLA DE RESULTADOS
            '''resultado=tiempo*xi
            
            self.label_dato1=tk.Label(self.p_grafica1, text=resultado, width=30,bg=COLOR_CUERPO_TITULO)
            self.label_dato1.pack(side=tk.TOP)'''

            #Se crea espacio (Figure) donde se insertara la grafica
            #LIENZO=--SINXTAXIS--variablefigura=Figure(figsize=(x,y), dpi=separacion, frameon=muestra(V) u oculta(F))
            self.figura1=Figure(figsize=(13,10),dpi=95, frameon=True ) #Espacio para agregar grafico x(t)
            self.figura2=Figure(figsize=(13,5),dpi=95, frameon=True ) #Espacio para agregar grafico v(t)
            #Creamos variable de la figura que se creara mediante .add_subplot()
            ax1=self.figura1.add_subplot() #sera grafico x(t)
            ax2=self.figura2.add_subplot()  #sera grafico v(t)
            #Llamamos al proceso o funcion y enviandole los datos requeridos:
            #tiempo, posicion inicial, velocidad inicial, aceleracion y las listas para que pueda llenarlas con datos
            self.grafico1(ax1,tiempo,xi,vi,a,lista_posicion_final,variable_tiempo) #Proceso o funcion para crear grafico x(t)
            self.grafico2(ax2,vi,a,lista_velocidad_final,variable_tiempo) #Proceso o funcion para crear grafico x(t)
            #Acabado el proceso o funcion anterior creamos el lienzo o canva donde se pondra el grafico creado
            #y se insertara en el frame p_grafica1
            self.lienzo1 = FigureCanvasTkAgg(figure=self.figura1,master= self.p_grafica1) #para grafico x(t)
            self.lienzo2 = FigureCanvasTkAgg(figure=self.figura2,master= self.p_grafica1) #para grafico v(t)
            #Dibujamos el lienzo (.draw))
            self.lienzo1.draw() 
            self.lienzo2.draw()
            #Capturamos el lienzo donde se dibujo la figura (.get_tk_widget()) y 
            #lo empaquetamos y lo ubicamos en la posicion uno debajo de otro mediante TOP
            self.lienzo1.get_tk_widget().pack(side=tk.BOTTOM) #Obtenemos grafico x(t) dibujado #place(x=0,y=0, relwidth=1,relheight=1)#pack(side=tk.LEFT)
            self.lienzo2.get_tk_widget().pack(side=tk.BOTTOM) #Obtenemos grafico v(t) dibujado

            #Desactivamos los entry y el boton graficar hasta que se presione boton nuevo grafico
            #Imprimimos variables tiempo,posicion para verificar su contenido
            print(tiempo,xi,vi,a)
            #Convertimos a enteros para poder comparar los valores ingresados y tomar decisiones
            xi_v=int(xi)
            vi_v=int(vi)
            a_v=int(a)
            #Condicion donde se compara si el valor de las variables tiempo,posicion,velocidad y aceleracion es igual a 0
            if tiempo == 0 & xi_v == 0 & vi_v == 0 & a_v == 0:
                #Si es verdadero desactivamos el boton nuevo grafico
                self.b_nuevo_g.config(state="disabled")
                #requerimos al usuario ingrese valores diferentes de 0
                self.label_error.config(text="! Ingrese almenos una elemento diferente de 0 ¡")
                #Llama a la funcion para limpiar lienzo
                self.nuevo_grafico()
                pass
            else:
                #Si es falso y las variables tiempo,posicion es que son diferentes de 0 y bloquean los botones y entry correspondientes
                #hasta que se presione boton NUEVO GRAFICO para limpiar lienzo
                self.b_graficar.config(state="disabled", bg=COLOR_BOTON_DES)
                self.entry_tiempo.config(state="disabled")
                self.entry_posicion.config(state="disabled")
                self.entry_velocidad_i.config(state="disabled")
                self.entry_aceleracion.config(state="disabled")
                #Habilita boton nuevo grafico
                self.b_nuevo_g.config(state="normal", bg=COLOR_BOTON_ACT)

            #Imprimimos en consola el contenido de las listas para verificar contenido
            print(variable_tiempo,lista_posicion_final)

           #Notifica un error
           except Exception as e:
               #notifica el error en consola
               print(e)
               #Condicion donde se compara si se ingresaron datos en los entry anteriores
               if self.entry_tiempo.get()=="" or self.entry_posicion.get()=="" or self.entry_velocidad_i.get()=="" or self.entry_aceleracion.get()=="":
                    #Si es verdadero se notifica que se ingrese valores cabiando el texto por medio de .config
                    self.label_error.config(text="! Ingrese todos los valores requeridos ¡")
               else:
                    #Si es falso se notifica que se ingrese valores numericos cabiando el texto por medio de .config
                    self.label_error.config(text="! Ingrese solamente datos numéricos ¡")
                    pass
               
    #Creacion del grafico x(t)
    def grafico1(self, ax,tiempo,xi,vi,a,lista_posicion_final,variable_tiempo):
                #Capturado todos los datos y creada el espacio donde va el grafico
                #Creamos el grafico
                #Creamos un rango de 0 al tiempo que brindo el usuario por entry (no existe tiempo -)
                #sirve para definir el eje x del grafico donde estar tiempo ya que es variable independiente
                #Creamos los decimales para generar un rango mas detallado ti=(ti/10)
                #Creamos una lista que defina un rango desde 0 hasta el tiempo que ingreso el usuario
                #Multiplicado por 10 para extender el rango y poder tener el tiempo recorrido en cantidades de 0.1
                #Round redondea los decimales-- SINTAXIS: round(variable, numeros a mostrar)
                tiempo_usuario=[round(ti/10,2) for ti in range(0,(tiempo+1)*10)]#np.arange(0,tiempo+1,0.1)
                
                #Creamos un for que pase por todos los elementos que se crearon en lista tiempo_usuario
                for t in tiempo_usuario:
                    #Variable t toma el valor de tiempo_usuario y lo agregamos a lista variable_tiempo
                    #por medio de metodo de listas (.append(valor))
                    variable_tiempo.append(t)
                    #Imprimimos en consola t para ver los valores
                    print(t)

                #Creamos un for que pase por todos los elementos que se insertaron en lista variable_tiempo y los tranfiera a t_f
                for t_f in variable_tiempo:
                    #Variable t_f (tiempo final) toma los valores de la lista variable_tiempo 1x1
                    #y resuelve la formula de posicion final (p_f) con cada valor del tiempo y de los datos proporcionados al principio
                    p_f=xi+(vi*t_f)+(((1/2)*a)*(t_f**2))
                    
                    #Variable p_f (posicion final) recibe el valor para almacenarlos en lista posicion_final
                    #por medio de metodo de listas (.append(valor))
                    lista_posicion_final.append(round(p_f,2))
                    #Imprimimos en consola los elementos de la lista para verificacion
                    print(lista_posicion_final)

                #Una vez ingresado los datos en las listas correspondientes 
                #donde variable_tiempo = x, lista_posicion_final = y
                #Creamos el grafico mediante ax.plot(elementos de eje x, elementos de eje y, ...atributos)
                ax.plot(variable_tiempo, lista_posicion_final, label='Gráfico x(t)', color='red')
                #Damos titulo al grafico
                ax.set_title('Gráfico x(t)',)
                #Damos nombres a los ejes
                ax.set_xlabel('Tiempo (s)', fontsize=12)
                ax.set_ylabel('Posición (m)', fontsize=12)
                #Damos atributos al grafico: malla, tipo de linea, etc
                ax.grid(True, linestyle='--', alpha=0.5)

                ax.set_xscale( "linear")
                ax.xaxis.set_minor_locator(MultipleLocator(0.5))   # X: separación cada 0.5 unidades
                ax.xaxis.grid(which='minor', linestyle='dashed', color='gray')
                ax.xaxis.set_minor_formatter('{x:.1f}')
                ax.tick_params(axis='x', which='minor', labelsize=8, labelcolor='gray')
                
                ax.set_yscale("linear")
                ax.yaxis.set_minor_locator(MultipleLocator(1))  # Y: separación cada 1 unidades
                ax.yaxis.grid(which='minor', linestyle='dashed', color='lightskyblue')
                ax.yaxis.set_minor_formatter('{x:.0f}')  
                ax.tick_params(axis='y', which='minor', labelsize=5, labelcolor='lightskyblue')

                ax.legend()

    #Creacion del grafico v(t)
    def grafico2(self, ax,vi,a,lista_velocidad_final,variable_tiempo):
                #Capturado todos los datos y creada el espacio donde va el grafico
                #Creamos el grafico
                
                #Creamos un for que pase por todos los elementos que se insertaron en lista variable_tiempo y los tranfiera a t_f
                for t_f in variable_tiempo:
                    #Variable t_f (tiempo final) toma los valores de la lista variable_tiempo 1x1
                    #y resuelve la formula de velocidad final (v_f) con cada valor del tiempo y de los datos proporcionados al principio
                    v_f=vi+a*t_f
                    
                    #Variable v_f (velocidad final) recibe el valor para almacenarlos en lista velocidad_final
                    #por medio de metodo de listas (.append(valor))
                    lista_velocidad_final.append(round(v_f,2))
                    #Imprimimos en consola los elementos de la lista para verificacion
                    print(lista_velocidad_final)

                #Una vez ingresado los datos en las listas correspondientes 
                #donde variable_tiempo = x, lista_velocidad_final = y
                #Creamos el grafico mediante ax.plot(elementos de eje x, elementos de eje y, ...atributos)
                ax.plot(variable_tiempo, lista_velocidad_final, label='Gráfico v(t)', color='red')
                #Damos titulo al grafico
                ax.set_title('Gráfico v(t)',)
                #Damos nombres a los ejes
                ax.set_xlabel('Tiempo (s)', fontsize=12)
                ax.set_ylabel('Velocidad (m/s)', fontsize=12)
                #Damos atributos al grafico: malla, tipo de linea, etc
                ax.grid(True, linestyle='--', alpha=0.5)

                ax.set_xscale( "linear")
                ax.xaxis.set_minor_locator(MultipleLocator(0.5))   # X: separación cada 0.5 unidades
                ax.xaxis.grid(which='minor', linestyle='dashed', color='gray')
                ax.xaxis.set_minor_formatter('{x:.1f}')
                ax.tick_params(axis='x', which='minor', labelsize=8, labelcolor='gray')
                
                ax.set_yscale("linear")
                ax.yaxis.set_minor_locator(MultipleLocator(1))  # Y: separación cada 1 unidades
                ax.yaxis.grid(which='minor', linestyle='dashed', color='lightskyblue')
                ax.yaxis.set_minor_formatter('{x:.0f}')  
                ax.tick_params(axis='y', which='minor', labelsize=5, labelcolor='lightskyblue')

                ax.legend()


    #Accion del boton NUEVO GRAFICO
    def nuevo_grafico(self):
        #Habilitamos los entry de datos y boton graficar para ingresar nuevos datos para grficar
        print(self.l_p_f,self.v_t)
        self.entry_tiempo.config(state="normal")
        self.entry_posicion.config(state="normal")
        self.entry_velocidad_i.config(state="normal")
        self.entry_aceleracion.config(state="normal")
        #Cambiamos el color de boton nuevo grafico a desactivado
        self.b_nuevo_g.config(state="disabled", bg=COLOR_BOTON_DES)
        #Cambiamos el color de boton graficar a activado
        self.b_graficar.config(state="normal", bg=COLOR_BOTON_ACT)
        #Vaciamos los entry mediante metodo(.delete(posicion_inicial,posicion_final))
        self.entry_tiempo.delete(0, 5)
        self.entry_posicion.delete(0, 5)
        self.entry_velocidad_i.delete(0, 5)
        self.entry_aceleracion.delete(0, 5)
                
        #Eliminamos los datos de la lista de los elemento tiempo, posicion y velocidad
        #para poder ingresar nuevos datos, mediante metodo (.clear())
        self.l_p_f.clear()
        self.v_t.clear()
        self.l_v_f.clear()
        #Imprimimos por consola los elementos de las listas para verificar eliminacion
        print(self.l_p_f,self.v_t,self.l_v_f)
        
        #Limpiamos el espacio que se dio para la figura mediante metodo (.destroy())
        #es decir destruimos el frame que esta dentro del lienzo principal que contiene a los graficos
        #self.p_grafica1.destroy()
        
        #Imprimimos mediante consola para visualizar que datos reciben los entry al presionar boton nuevo grafco
        print(self.entry_tiempo.get(),self.entry_posicion.get(),self.entry_velocidad_i.get(),self.entry_aceleracion.get() )
        #Insertamos en entry el valor de "0" para que mande datos en 0
        self.entry_tiempo.insert(0, "0")
        self.entry_posicion.insert(0, "0")
        self.entry_velocidad_i.insert(0, "0")
        self.entry_aceleracion.insert(0, "0")
        #Imprimimos mediante consola para verificar el valor insertado de los entry anteriormente
        print(self.entry_tiempo.get(),self.entry_posicion.get(),self.entry_velocidad_i.get(),self.entry_aceleracion.get() )
        
        #Mediante metodo AFTER (.after(tiempo,funcion)) llamamos desde el panel padre p_grafica
        #a la funcion crear_frame_grafica para que vuelva a crear el frame p_grafica1 destruido anteriormente
        #y asi poder volver a generar otros graficos
        self.p_grafica1.after(1000,self.limpiar_grafica(self.p_grafica1))

    #Creamos funcion para lipiar grafica
    def limpiar_grafica(self,panel):
    #Destruye los hijos (WIDGETS) que contiene el frame o panel principal
        for widget in panel.winfo_children():
            widget.destroy()



    '''
    #Creamos la funcion para iniciar el FRAME de grafica glpbal
    def __init__(self, panel_principal):

        #CREAMOS FRAMES (ESPACIOS,PANELES)
        #Creamos frame para titulo en el cuerpo_principal
        #lo empaquetamos y lo posicionamos en la parte superrior (TOP) y que ocupeel eje x, no se expande
        self.p_titulo = tk.Frame(panel_principal)
        self.p_titulo.pack(side=tk.TOP, fill=tk.X, expand=False)
        
        #Creamos frame para informacion en el cuerpo_principal
        #lo empaquetamos y lo posicionamos en la parte inferior (BOTTOM) y se expande
        self.p_informacion = tk.Frame(panel_principal, 
                                      pady=10,
                                      padx=10,
                                      bg=COLOR_CUERPO_INFORMACION)
        self.p_informacion.pack(side=tk.TOP, fill='both', expand=False)

        #Creamos frame para la grafica en el cuerpo_principal
        #lo empaquetamos y lo posicionamos en la parte inferior (BOTTOM) y se expande
        self.p_grafica = tk.Frame(panel_principal, bg="grey")
        self.p_grafica.pack(side=tk.BOTTOM, fill='both', expand=True,)
        

        #CREAMOS LABELS (ESPACIOS DE TEXTO)
        
        # Creamos label para el titulo
        self.label_titulo = tk.Label(
            self.p_titulo, text="Graficas del MRUA")
        self.label_titulo.config(fg="#222d33", 
                                 font=(SUBTITULO, 30), 
                                 bg=COLOR_CUERPO_TITULO)
        self.label_titulo.pack(side=tk.TOP, fill='both', expand=True)

        
        #Redimencionamos la tabla o grid que contiene p_informacion (FRAME) con la ventana en sus columnas
        #--columnconfigure-- Da prioridades de redimencion a la columna especificada desde 0-n
        self.p_informacion.columnconfigure(0, weight=1)
        self.p_informacion.columnconfigure(1, weight=0)
        self.p_informacion.columnconfigure(2, weight=0)
        self.p_informacion.columnconfigure(3, weight=1)
        self.p_informacion.columnconfigure(4, weight=0)
        self.p_informacion.columnconfigure(5, weight=0)
        self.p_informacion.columnconfigure(6, weight=3)
        # Creamos label para etiquetas de INFORMACION
        #Creamos label para tiempo y se empaqueta en metodo grid o tabla
        self.label_tiempo = tk.Label(self.p_informacion, text="Ingrese el tiempo:")
        self.label_tiempo.config(fg="#222d33", 
                                 font=(TEXTO, 12), 
                                 bg=COLOR_CUERPO_INFORMACION, 
                                 padx=5,pady=5,
                                 width=20,)    
        self.label_tiempo.grid(row=0, column=0)
        self.label_um_tiempo = tk.Label(self.p_informacion, text="(s)")
        self.label_um_tiempo.config(fg="#222d33", 
                                 font=(TEXTO, 12), 
                                 bg=COLOR_CUERPO_INFORMACION, 
                                 #padx=5,pady=5,
                                 width=7)    
        self.label_um_tiempo.grid(row=0, column=2)
        #Creamos label para posicion y se empaqueta en metodo grid o tabla       
        self.label_posicion = tk.Label(self.p_informacion, text="Ingrese la posición:")
        self.label_posicion.config(fg="#222d33", 
                                   font=(TEXTO, 12), 
                                   bg=COLOR_CUERPO_INFORMACION, 
                                   padx=5,pady=5,
                                   width=20)    
        self.label_posicion.grid(row=1, column=0)
        self.label_um_posicion = tk.Label(self.p_informacion, text="(m)")
        self.label_um_posicion.config(fg="#222d33", 
                                   font=(TEXTO, 12), 
                                   bg=COLOR_CUERPO_INFORMACION, 
                                   #padx=5,pady=5,
                                   width=7)    
        self.label_um_posicion.grid(row=1, column=2)
        #Creamos label para velocidad inicial y se empaqueta en metodo grid o tabla
        self.label_velocidad_i = tk.Label(self.p_informacion, text="Ingrese la velocidad inicial:")
        self.label_velocidad_i.config(fg="#222d33", 
                                 font=(TEXTO, 12), 
                                 bg=COLOR_CUERPO_INFORMACION, 
                                 padx=5,pady=5,
                                 width=30)    
        self.label_velocidad_i.grid(row=0, column=3)
        self.label_um_velocidad_i = tk.Label(self.p_informacion, text="(m/s)")
        self.label_um_velocidad_i.config(fg="#222d33", 
                                 font=(TEXTO, 12), 
                                 bg=COLOR_CUERPO_INFORMACION, 
                                 #padx=5,pady=5,
                                 width=7)    
        self.label_um_velocidad_i.grid(row=0, column=5)
        #Creamos label para aceleracion y se empaqueta en metodo grid o tabla       
        self.label_aceleracion = tk.Label(self.p_informacion, text="Ingrese la aceleración:")
        self.label_aceleracion.config(fg="#222d33", 
                                   font=(TEXTO, 12), 
                                   bg=COLOR_CUERPO_INFORMACION, 
                                   padx=5,pady=5,
                                   width=30)    
        self.label_aceleracion.grid(row=1, column=3)
        self.label_um_aceleracion = tk.Label(self.p_informacion, text="(m/s^2)")
        self.label_um_aceleracion.config(fg="#222d33", 
                                   font=(TEXTO, 12), 
                                   bg=COLOR_CUERPO_INFORMACION,
                                   #padx=5,pady=5,
                                   width=7)    
        self.label_um_aceleracion.grid(row=1, column=5)
        #Creamos label para errores, sin ningun texto para despues modificarlo
        self.label_error = tk.Label(self.p_informacion, text="")
        self.label_error.config(fg="#222d33", 
                                font=(TEXTO, 12), 
                                bg=COLOR_CUERPO_TITULO, 
                                padx=5,pady=5,
                                width=60)
        self.label_error.grid(row=2, column=0, columnspan=7, sticky="nsew")


        # CREAMOS ENTRY PARA ENTRADA DE DATOS
        #Creamos entry para tiempo y se empaqueta en metodo grid o tabla
        self.entry_tiempo = tk.Entry(self.p_informacion)
        #Damos atributos (.config): largo de 5 caracteres, alineado a la derecha, y estado normal para posteriormente desactivarlo
        self.entry_tiempo.config(width=5,
                                 justify="right",
                                 state="normal")
        self.entry_tiempo.grid(row=0, column=1, padx=10)
        #Creamos entry para posicion inicial y se empaqueta en metodo grid o tabla
        self.entry_posicion = tk.Entry(self.p_informacion)
        #Damos atributos (.config): largo de 5 caracteres, alineado a la derecha, y estado normal para posteriormente desactivarlo
        self.entry_posicion.config(width=5,
                                   justify="right",
                                   state="normal")
        self.entry_posicion.grid(row=1, column=1,padx=10)
        #Creamos entry para velocidad inicial y se empaqueta en metodo grid o tabla
        self.entry_velocidad_i = tk.Entry(self.p_informacion)
        #Damos atributos (.config): largo de 5 caracteres, alineado a la derecha, y estado normal para posteriormente desactivarlo
        self.entry_velocidad_i.config(width=5,
                                 justify="right",
                                 state="normal")
        self.entry_velocidad_i.grid(row=0, column=4, padx=10)
        #Creamos entry para aceleracion y se empaqueta en metodo grid o tabla
        self.entry_aceleracion = tk.Entry(self.p_informacion)
        #Damos atributos (.config): largo de 5 caracteres, alineado a la derecha, y estado normal para posteriormente desactivarlo
        self.entry_aceleracion.config(width=5,
                                   justify="right",
                                   state="normal")
        self.entry_aceleracion.grid(row=1, column=4,padx=10)

        # CREAMOS BOTONES
        # Creamos boton para ENVIAR DATOS a proceso o funcion graficar y damos atributos
        self.b_graficar = tk.Button(self.p_informacion, 
                                    text="GRAFICAR", 
                                    padx=10,pady=10, 
                                    bd=0,
                                    relief="ridge", 
                                    bg=COLOR_BOTON_ACT,
                                    command=self.graficar,
                                    state="normal")
        #Se empaqueta en metodo grid o tabla, 
        #sticky=expande alinea boton en direcciones norte,sur,este,oeste
        self.b_graficar.grid(row=0, column=6, sticky="nsew")
        
        # Creamos boton para NUEVO GRAFICO y enviarlo al proceso o funcion nuevo grafico y damos atributos
        self.b_nuevo_g = tk.Button(self.p_informacion, 
                                   text="NUEVO GRÁFICO", 
                                   padx=10,pady=10, 
                                   bd=0,
                                   relief="ridge", 
                                   bg=COLOR_BOTON_DES,
                                   command=self.nuevo_grafico,
                                   state="disabled")
        #Se empaqueta en metodo grid o tabla, 
        #sticky=expande alinea boton en direcciones norte,sur,este,oeste con siglas en ingles
        self.b_nuevo_g.grid(row=1, column=6, sticky="nsew")

        # PANEL DE LA GRAFICA
        #Configuramos las columnas de la tabla que organizara los graficos en el frame p_grafica para que se redimencionen
        self.p_grafica.columnconfigure(0, weight=1)
        self.p_grafica.columnconfigure(1, weight=0)
        #Configuramos las filas de la tabla que organizara los graficos en el frame p_grafica para que se redimencionen
        self.p_grafica.rowconfigure(0, weight=1)

        #CREAMOS EL LIENZO PRINCIPAL que se encontrara dentro de la tabla mencionada anteriormente en p_grafica
        #en este lienzo principal se integra los graficos y nos ayudara con la barra de desplazamiento
        self.lienzo_principal=tk.Canvas(self.p_grafica)
        #Se empaqueta el lienzo principal en grid fila=0,colum=0 para poner en la derecha la barra de desplzamiento
        self.lienzo_principal.grid(row=0,column=0, sticky="nsew")
        #Se crea un evento para que se pueda desplazar la barra de desplazamiento
        self.lienzo_principal.bind("<Configure>", lambda e: self.lienzo_principal.config(scrollregion = self.lienzo_principal.bbox("all")))

        #CREAMOS EL YSCROLLBAR O BARRA DE DESPLAZAMIENTO
        self.puente=ttk.Scrollbar(self.p_grafica,
                                  orient="vertical", 
                                  command=self.lienzo_principal.yview)
        #Empaquetamos la barra de desplzamiento hacia la derecha en fila=0,colum=1
        self.puente.grid(row=0,column=1,sticky="ns")
        self.lienzo_principal.config(yscrollcommand=self.puente.set)
        
        #Llamamos a funcion crear_frame_grafica para que cree un frame dentro de lienzo principal y podes desplazarnos con la barra
        self.crear_frame_grafica ()

    #Creamos funcion para crear el frame que contiene la grafica
    def crear_frame_grafica(self):
        self.p_grafica1=tk.Frame(self.lienzo_principal, bg="red")
        #self.p_grafica1.pack(side=tk.LEFT)#grid(row=0,column=0)
        self.lienzo_principal.create_window((0,0),window=self.p_grafica1, anchor="nw")

    
    #Accion de boton graficar
    def graficar(self):
           #Iniciamos proceso
           try:
            #Creamos variables y obtenemos datos por metodo get() y las convertimos en vriables enteras y float
            tiempo=int(self.entry_tiempo.get())
            xi=float(self.entry_posicion.get())
            vi=float(self.entry_velocidad_i.get())
            a=float(self.entry_aceleracion.get())
            
            #Damos texto a label de error xq todo esta correcto
            self.label_error.config(text="")

            #Creamos lista donde se almacena los puntos para generar la grafica
            lista_posicion_final=self.l_p_f=[]
            variable_tiempo=self.v_t=[]
            lista_velocidad_final=self.l_v_f=[]
            #Imprimimos en consola los elementos que contienen las listas
            print(variable_tiempo,lista_posicion_final,lista_velocidad_final)
            #Imprimimos en consola las variables para ver contenido
            print(tiempo,xi,vi,a)

            #OJO: ESPACIO PARA INSERTAR TABLA DE RESULTADOS
            resultado=tiempo*xi
            #
            self.label_dato1=tk.Label(self.p_grafica1, text=resultado, width=30,bg=COLOR_CUERPO_TITULO)
            self.label_dato1.pack(side=tk.TOP)

            #Se crea espacio (Figure) donde se insertara la grafica
            #LIENZO=--SINXTAXIS--variablefigura=Figure(figsize=(x,y), dpi=separacion, frameon=muestra(V) u oculta(F))
            self.figura1=Figure(figsize=(13,10),dpi=100, frameon=True ) #Espacio para agregar grafico x(t)
            self.figura2=Figure(figsize=(13,5),dpi=100, frameon=True ) #Espacio para agregar grafico v(t)
            #Creamos variable de la figura que se creara mediante .add_subplot()
            ax1=self.figura1.add_subplot() #sera grafico x(t)
            ax2=self.figura2.add_subplot()  #sera grafico v(t)
            #Llamamos al proceso o funcion y enviandole los datos requeridos:
            #tiempo, posicion inicial, velocidad inicial, aceleracion y las listas para que pueda llenarlas con datos
            self.grafico1(ax1,tiempo,xi,vi,a,lista_posicion_final,variable_tiempo) #Proceso o funcion para crear grafico x(t)
            self.grafico2(ax2,vi,a,lista_velocidad_final,variable_tiempo) #Proceso o funcion para crear grafico x(t)
            #Acabado el proceso o funcion anterior creamos el lienzo o canva donde se pondra el grafico creado
            #y se insertara en el frame p_grafica1
            self.lienzo1 = FigureCanvasTkAgg(figure=self.figura1,master= self.p_grafica1) #para grafico x(t)
            self.lienzo2 = FigureCanvasTkAgg(figure=self.figura2,master= self.p_grafica1) #para grafico v(t)
            #Dibujamos el lienzo (.draw))
            self.lienzo1.draw() 
            self.lienzo2.draw()
            #Capturamos el lienzo donde se dibujo la figura (.get_tk_widget()) y 
            #lo empaquetamos y lo ubicamos en la posicion uno debajo de otro mediante TOP
            self.lienzo1.get_tk_widget().pack(side=tk.TOP) #Obtenemos grafico x(t) dibujado #place(x=0,y=0, relwidth=1,relheight=1)#pack(side=tk.LEFT)
            self.lienzo2.get_tk_widget().pack(side=tk.TOP) #Obtenemos grafico v(t) dibujado

            #Desactivamos los entry y el boton graficar hasta que se presione boton nuevo grafico
            #Imprimimos variables tiempo,posicion para verificar su contenido
            print(tiempo,xi,vi,a)
            #Convertimos a enteros para poder comparar los valores ingresados y tomar decisiones
            xi_v=int(xi)
            vi_v=int(vi)
            a_v=int(a)
            #Condicion donde se compara si el valor de las variables tiempo,posicion,velocidad y aceleracion es igual a 0
            if tiempo == 0 & xi_v == 0 & vi_v == 0 & a_v == 0:
                #Si es verdadero desactivamos el boton nuevo grafico
                self.b_nuevo_g.config(state="disabled")
                #requerimos al usuario ingrese valores diferentes de 0
                self.label_error.config(text="! Ingrese almenos una elemento diferente de 0 ¡")
                #Llama a la funcion para limpiar lienzo
                self.nuevo_grafico()
                pass
            else:
                #Si es falso y las variables tiempo,posicion es que son diferentes de 0 y bloquean los botones y entry correspondientes
                #hasta que se presione boton NUEVO GRAFICO para limpiar lienzo
                self.b_graficar.config(state="disabled", bg=COLOR_BOTON_DES)
                self.entry_tiempo.config(state="disabled")
                self.entry_posicion.config(state="disabled")
                self.entry_velocidad_i.config(state="disabled")
                self.entry_aceleracion.config(state="disabled")
                #Habilita boton nuevo grafico
                self.b_nuevo_g.config(state="normal", bg=COLOR_BOTON_ACT)

            #Imprimimos en consola el contenido de las listas para verificar contenido
            print(variable_tiempo,lista_posicion_final)

           #Notifica un error
           except ValueError:
               #notifica el error en consola
               print(ValueError)
               #Condicion donde se compara si se ingresaron datos en los entry anteriores
               if self.entry_tiempo.get()=="" or self.entry_posicion.get()=="" or self.entry_velocidad_i.get()=="" or self.entry_aceleracion.get()=="":
                    #Si es verdadero se notifica que se ingrese valores cabiando el texto por medio de .config
                    self.label_error.config(text="! Ingrese todos los valores requeridos ¡")
               else:
                    #Si es falso se notifica que se ingrese valores numericos cabiando el texto por medio de .config
                    self.label_error.config(text="! Ingrese solamente datos numéricos ¡")
                    pass
               
    #Creacion del grafico x(t)
    def grafico1(self, ax,tiempo,xi,vi,a,lista_posicion_final,variable_tiempo):
                #Capturado todos los datos y creada el espacio donde va el grafico
                #Creamos el grafico
                #Creamos un rango de 0 al tiempo que brindo el usuario por entry (no existe tiempo -)
                #sirve para definir el eje x del grafico donde estar tiempo ya que es variable independiente
                #Creamos los decimales para generar un rango mas detallado ti=(ti/10)
                #Creamos una lista que defina un rango desde 0 hasta el tiempo que ingreso el usuario
                #Multiplicado por 10 para extender el rango y poder tener el tiempo recorrido en cantidades de 0.1
                #Round redondea los decimales-- SINTAXIS: round(variable, numeros a mostrar)
                tiempo_usuario=[round(ti/10,2) for ti in range(0,(tiempo+1)*10)]#np.arange(0,tiempo+1,0.1)
                
                #Creamos un for que pase por todos los elementos que se crearon en lista tiempo_usuario
                for t in tiempo_usuario:
                    #Variable t toma el valor de tiempo_usuario y lo agregamos a lista variable_tiempo
                    #por medio de metodo de listas (.append(valor))
                    variable_tiempo.append(t)
                    #Imprimimos en consola t para ver los valores
                    print(t)

                #Creamos un for que pase por todos los elementos que se insertaron en lista variable_tiempo y los tranfiera a t_f
                for t_f in variable_tiempo:
                    #Variable t_f (tiempo final) toma los valores de la lista variable_tiempo 1x1
                    #y resuelve la formula de posicion final (p_f) con cada valor del tiempo y de los datos proporcionados al principio
                    p_f=xi+(vi*t_f)+(((1/2)*a)*(t_f**2))
                    
                    #Variable p_f (posicion final) recibe el valor para almacenarlos en lista posicion_final
                    #por medio de metodo de listas (.append(valor))
                    lista_posicion_final.append(round(p_f,2))
                    #Imprimimos en consola los elementos de la lista para verificacion
                    print(lista_posicion_final)

                #Una vez ingresado los datos en las listas correspondientes 
                #donde variable_tiempo = x, lista_posicion_final = y
                #Creamos el grafico mediante ax.plot(elementos de eje x, elementos de eje y, ...atributos)
                ax.plot(variable_tiempo, lista_posicion_final, label='Gráfico x(t)', color='red')
                #Damos titulo al grafico
                ax.set_title('Gráfico x(t)',)
                #Damos nombres a los ejes
                ax.set_xlabel('Tiempo (s)', fontsize=12)
                ax.set_ylabel('Posición (m)', fontsize=12)
                #Damos atributos al grafico: malla, tipo de linea, etc
                ax.grid(True, linestyle='--', alpha=0.5)

                ax.set_xscale( "linear")
                ax.xaxis.set_minor_locator(MultipleLocator(0.5))   # X: separación cada 0.5 unidades
                ax.xaxis.grid(which='minor', linestyle='dashed', color='gray')
                ax.xaxis.set_minor_formatter('{x:.1f}')
                ax.tick_params(axis='x', which='minor', labelsize=8, labelcolor='gray')
                
                ax.set_yscale("linear")
                ax.yaxis.set_minor_locator(MultipleLocator(1))  # Y: separación cada 1 unidades
                ax.yaxis.grid(which='minor', linestyle='dashed', color='lightskyblue')
                ax.yaxis.set_minor_formatter('{x:.0f}')  
                ax.tick_params(axis='y', which='minor', labelsize=5, labelcolor='lightskyblue')

                ax.legend()

    #Creacion del grafico v(t)
    def grafico2(self, ax,vi,a,lista_velocidad_final,variable_tiempo):
                #Capturado todos los datos y creada el espacio donde va el grafico
                #Creamos el grafico
                
                #Creamos un for que pase por todos los elementos que se insertaron en lista variable_tiempo y los tranfiera a t_f
                for t_f in variable_tiempo:
                    #Variable t_f (tiempo final) toma los valores de la lista variable_tiempo 1x1
                    #y resuelve la formula de velocidad final (v_f) con cada valor del tiempo y de los datos proporcionados al principio
                    v_f=vi+a*t_f
                    
                    #Variable v_f (velocidad final) recibe el valor para almacenarlos en lista velocidad_final
                    #por medio de metodo de listas (.append(valor))
                    lista_velocidad_final.append(round(v_f,2))
                    #Imprimimos en consola los elementos de la lista para verificacion
                    print(lista_velocidad_final)

                #Una vez ingresado los datos en las listas correspondientes 
                #donde variable_tiempo = x, lista_velocidad_final = y
                #Creamos el grafico mediante ax.plot(elementos de eje x, elementos de eje y, ...atributos)
                ax.plot(variable_tiempo, lista_velocidad_final, label='Gráfico v(t)', color='red')
                #Damos titulo al grafico
                ax.set_title('Gráfico v(t)',)
                #Damos nombres a los ejes
                ax.set_xlabel('Tiempo (s)', fontsize=12)
                ax.set_ylabel('Velocidad (m/s)', fontsize=12)
                #Damos atributos al grafico: malla, tipo de linea, etc
                ax.grid(True, linestyle='--', alpha=0.5)

                ax.set_xscale( "linear")
                ax.xaxis.set_minor_locator(MultipleLocator(0.5))   # X: separación cada 0.5 unidades
                ax.xaxis.grid(which='minor', linestyle='dashed', color='gray')
                ax.xaxis.set_minor_formatter('{x:.1f}')
                ax.tick_params(axis='x', which='minor', labelsize=8, labelcolor='gray')
                
                ax.set_yscale("linear")
                ax.yaxis.set_minor_locator(MultipleLocator(1))  # Y: separación cada 1 unidades
                ax.yaxis.grid(which='minor', linestyle='dashed', color='lightskyblue')
                ax.yaxis.set_minor_formatter('{x:.0f}')  
                ax.tick_params(axis='y', which='minor', labelsize=5, labelcolor='lightskyblue')

                ax.legend()


    #Accion del boton NUEVO GRAFICO
    def nuevo_grafico(self):
        #Habilitamos los entry de datos y boton graficar para ingresar nuevos datos para grficar
        print(self.l_p_f,self.v_t)
        self.entry_tiempo.config(state="normal")
        self.entry_posicion.config(state="normal")
        self.entry_velocidad_i.config(state="normal")
        self.entry_aceleracion.config(state="normal")
        #Cambiamos el color de boton nuevo grafico a desactivado
        self.b_nuevo_g.config(state="disabled", bg=COLOR_BOTON_DES)
        #Cambiamos el color de boton graficar a activado
        self.b_graficar.config(state="normal", bg=COLOR_BOTON_ACT)
        #Vaciamos los entry mediante metodo(.delete(posicion_inicial,posicion_final))
        self.entry_tiempo.delete(0, 5)
        self.entry_posicion.delete(0, 5)
        self.entry_velocidad_i.delete(0, 5)
        self.entry_aceleracion.delete(0, 5)
                
        #Eliminamos los datos de la lista de los elemento tiempo, posicion y velocidad
        #para poder ingresar nuevos datos, mediante metodo (.clear())
        self.l_p_f.clear()
        self.v_t.clear()
        self.l_v_f.clear()
        #Imprimimos por consola los elementos de las listas para verificar eliminacion
        print(self.l_p_f,self.v_t,self.l_v_f)
        
        #Limpiamos el espacio que se dio para la figura mediante metodo (.destroy())
        #es decir destruimos el frame que esta dentro del lienzo principal que contiene a los graficos
        self.p_grafica1.destroy()
        
        #Imprimimos mediante consola para visualizar que datos reciben los entry al presionar boton nuevo grafco
        print(self.entry_tiempo.get(),self.entry_posicion.get(),self.entry_velocidad_i.get(),self.entry_aceleracion.get() )
        #Insertamos en entry el valor de "0" para que mande datos en 0
        self.entry_tiempo.insert(0, "0")
        self.entry_posicion.insert(0, "0")
        self.entry_velocidad_i.insert(0, "0")
        self.entry_aceleracion.insert(0, "0")
        #Imprimimos mediante consola para verificar el valor insertado de los entry anteriormente
        print(self.entry_tiempo.get(),self.entry_posicion.get(),self.entry_velocidad_i.get(),self.entry_aceleracion.get() )
        
        #Mediante metodo AFTER (.after(tiempo,funcion)) llamamos desde el panel padre p_grafica
        #a la funcion crear_frame_grafica para que vuelva a crear el frame p_grafica1 destruido anteriormente
        #y asi poder volver a generar otros graficos
        self.lienzo_principal.after(1000,self.crear_frame_grafica)
        '''