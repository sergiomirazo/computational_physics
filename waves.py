import tkinter as tk 
from tkinter import ttk
from math import sin, pi

# Canvas
canvas_width = 500
canvas_height = 250
color_green = "#476042"

master = tk.Tk()
master.configure(bg=color_green)
canvas = tk.Canvas(master, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

# Variables
amplitud = 100
n_ondas = 3
longitud_onda = canvas_width / (n_ondas + 1)
frecuencia = 2
velocidad = 1
Yi = 0

titulo = tk.Label(master, bg=color_green, fg='orange', text='Simulación de ondas en osciloscopio', font = ("sansserif", 16, "bold"))
titulo.pack(fill='x')

# Sliders
slider_frecuencia = ttk.Scale(master, from_=0.1, to=4.0,
                              value=frecuencia, orient=tk.HORIZONTAL,
                              length=300, command=lambda v: set_frecuencia(float(v)))
label1 = tk.Label(master, bg=color_green, fg='white', text='Frecuencia', font = ("sansserif", 10, "bold"))
label1.pack(fill='x')
slider_frecuencia.pack()

slider_velocidad = ttk.Scale(master, from_=0.1, to=20.0, value=velocidad,
                             orient=tk.HORIZONTAL, length=300,
                             command=lambda v: set_velocidad(float(v)))
label2 = tk.Label(master, bg=color_green, fg='white', text='Velocidad', font = ("sansserif", 10, "bold"))
label2.pack(fill='x')
slider_velocidad.pack()

label3 = tk.Label(master, bg=color_green, fg='white', text='Amplitud', font = ("sansserif", 10, "bold"))
label3.pack(fill='x')
slider_amplitud = ttk.Scale(master, from_=0.1, to=100.0, value=velocidad,
                             orient=tk.HORIZONTAL, length=300,
                             command=lambda v: set_amplitud(float(v)))
slider_amplitud.pack()

label4 = tk.Label(master, bg=color_green, fg='white', text='Posición Y', font = ("sansserif", 10, "bold"))
label4.pack(fill='x')
slider_amplitud = ttk.Scale(master, from_=0.0, to=100.0, value=velocidad,
                             orient=tk.HORIZONTAL, length=300,
                             command=lambda v: set_altura(float(v)))
slider_amplitud.pack()

label5 = tk.Label(master, bg=color_green, fg='white', text='ARJÉ Club de Ciencias | By Sergio Mirazo', font = ("Helvetica", 10))
label5.pack(fill='x')

# Funciones
def set_frecuencia(v):
    global frecuencia
    frecuencia = v

def set_velocidad(v):
    global velocidad
    velocidad = v

def set_amplitud(v):
    global amplitud
    amplitud = v

def set_altura(v):
    global Yi
    Yi = v

def onda(x):
    return amplitud * sin(2 * pi * frecuencia * (x / longitud_onda) - velocidad * t)

# Animación
t = 0
while True:
    t += 0.033
    x = 0
    while x < canvas_width:
        y =Yi + onda(x)
        canvas.create_line(x, y + amplitud, x, amplitud * 2, fill='#00FF00')
        x += 1
    canvas.update()
    canvas.after(33)
    canvas.delete("all")

master.mainloop()
import tkinter as tk 
from tkinter import ttk
from math import sin, pi

# Canvas
canvas_width = 500
canvas_height = 250
color_green = "#476042"

master = tk.Tk()
canvas = tk.Canvas(master, width=canvas_width, height=canvas_height, bg=color_green)
canvas.pack()

# Variables
amplitud = 100
n_ondas = 3
longitud_onda = canvas_width / (n_ondas + 1)
frecuencia = 2
velocidad = 1

titulo = tk.Label(master, bg=color_green, fg='orange', width=100, text='Simulación de ondas', font = ("sansserif", 16, "bold"))
titulo.pack()

# Sliders
slider_frecuencia = ttk.Scale(master, from_=0.1, to=4.0,
                              value=frecuencia, orient=tk.HORIZONTAL,
                              length=300, command=lambda v: set_frecuencia(float(v)))
label1 = tk.Label(master, bg=color_green, fg='white', width=100, text='Frecuencia', font = ("sansserif", 10, "bold"))
label1.pack()
slider_frecuencia.pack()

slider_velocidad = ttk.Scale(master, from_=0.1, to=4.0, value=velocidad,
                             orient=tk.HORIZONTAL, length=300,
                             command=lambda v: set_velocidad(float(v)))
label2 = tk.Label(master, bg=color_green, fg='white', width=100, text='Velocidad', font = ("sansserif", 10, "bold"))
label2.pack()
slider_velocidad.pack()

# Funciones
def set_frecuencia(v):
    global frecuencia
    frecuencia = v

def set_velocidad(v):
    global velocidad
    velocidad = v

def onda(x):
    return amplitud * sin(2 * pi * frecuencia * (x / longitud_onda) - velocidad * t)

# Animación
t = 0
while True:
    t += 0.033
    x = 0
    while x < canvas_width:
        y = onda(x)
        canvas.create_line(x, y + amplitud, x, amplitud * 2, fill="white")
        x += 1
    canvas.update()
    canvas.after(33)
    canvas.delete("all")

master.mainloop()
