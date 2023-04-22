import tkinter as tk
import random

# configurar la ventana
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Simulación de Partículas")
canvas = tk.Canvas(ventana, bg="black", width=500, height=500)
canvas.pack()

# modificar los parámetros aquí
num_particulas = 100
tamaño_particula = 10

# crear las partículas
particulas = []
for i in range(num_particulas):
    # generar coordenadas aleatorias para cada partícula
    x = random.randint(20, 480)
    y = random.randint(20, 480)
    # generar velocidades aleatorias para cada partícula
    vx = random.randint(-5, 5)
    vy = random.randint(-5, 5)
    # crear la partícula
    particulas.append([x, y, vx, vy])

# actualizar el canvas
def actualizar():
    # mover las partículas
    for p in particulas:
        p[0] += p[2]
        p[1] += p[3]
        # comprobar si la partícula sale de los límites
        if p[0] > 480 or p[0] < 20:
            p[2] *= -1
        if p[1] > 480 or p[1] < 20:
            p[3] *= -1
    # borrar el canvas
    canvas.delete("all")
    # dibujar las partículas
    for p in particulas:
        canvas.create_oval(p[0], p[1], p[0] + tamaño_particula, p[1] + tamaño_particula, fill="green")
    # llamar recursivamente a la función para actualizar el canvas
    ventana.after(10, actualizar)

# llamada para inicializar el canvas
actualizar()

# iniciar la ventana
ventana.mainloop()
