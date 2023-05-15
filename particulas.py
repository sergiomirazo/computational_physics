import tkinter as tk
import random

window = tk.Tk()
window.geometry("500x500")
window.title("Particles simulation")
canvas = tk.Canvas(window, bg="black", width=500, height=500)
canvas.pack()

num_particles = 100
size_particle = 10

particles = []
for i in range(num_particles):
    x = random.randint(20, 480)
    y = random.randint(20, 480)
    vx = random.randint(-5, 5)
    vy = random.randint(-5, 5)
    particles.append([x, y, vx, vy])

def refresh():
    for p in particles:
        p[0] += p[2]
        p[1] += p[3]
        if p[0] > 480 or p[0] < 20:
            p[2] *= -1
        if p[1] > 480 or p[1] < 20:
            p[3] *= -1
    canvas.delete("all")
    for p in particles:
        canvas.create_oval(p[0], p[1], p[0] + size_particle, p[1] + size_particle, fill="green")
    window.after(10, refresh)

refresh()

window.mainloop()
