from tkinter import *
from tkinter.ttk import *
import math

# Definir variables
pendulo_longitud = 50
pendulo_ancho = 10
pendulo_x = 250
pendulo_y = 50
t = 0
angulo = lambda t, A, L : A*math.sin(math.sqrt(9810/L)*t) #Expresamos la gravedad a escala, según los pixeles por segundo al cuadrado
w = round(math.sqrt(9.81*1000/pendulo_longitud), 3)

# Crear ventana
ventana = Tk()
canvas = Canvas(ventana, bg='#000050', width = 500, height = 500)
canvas.pack()

# Dibujar el péndulo
pendulo = canvas.create_line(pendulo_x, pendulo_y, pendulo_x + pendulo_longitud *
                             math.sin(angulo(t, 0.105, pendulo_longitud)),
                             pendulo_y + pendulo_longitud *
                             math.cos(angulo(t, 0.105, pendulo_longitud)),
                             width = pendulo_ancho, fill="#E1E250")

def plus():
    global pendulo_longitud
    if pendulo_longitud==500.0:
        pass
    else:
        pendulo_longitud = pendulo_longitud + 10
        pendulo_longitud = pendulo_longitud

def minus():
    global pendulo_longitud
    if pendulo_longitud==50.0:
        pass
    else:
        pendulo_longitud = pendulo_longitud - 10
        pendulo_longitud = pendulo_longitud
    
button1 = Button(text='+1cm', command=plus)
canvas.create_window(90, 200, window=button1)

button2 = Button(text='-1cm', command=minus)
canvas.create_window(90, 250, window=button2)


# Función para actualizar el péndulo
def actualizar():
    global t
    t += 0.1
    canvas.coords(pendulo, pendulo_x, pendulo_y, pendulo_x +
                  pendulo_longitud * math.sin(angulo(t, 0.105, pendulo_longitud)),
                  pendulo_y + pendulo_longitud * math.cos(angulo(t, 0.105, pendulo_longitud)))
    label_frame = LabelFrame(canvas, text='Frecuencia angular: '+str(w)+' Hz')
    label = Label(label_frame, text="Longitud: "+str(pendulo_longitud/1000)+' m')
    label.pack()
    canvas.create_window(50, 100, window=label_frame, anchor='w')
    ventana.after(50, actualizar)

# Ejecutar
actualizar()
ventana.mainloop()
