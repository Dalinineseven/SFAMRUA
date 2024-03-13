from PIL import ImageTk, Image
import os, sys
# Creamos funcion que redimencione imagenes con libreria PIL
# Requerimos path="ruta", y un size="tamaño"
# Retornamos imagen redimencionada = "resize"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

def leer_imagen (path, size):

    return ImageTk.PhotoImage(Image.open(resource_path(path)).resize(size))
