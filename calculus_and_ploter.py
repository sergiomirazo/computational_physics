"""
    program: calculus_and_ploter.py
    author: Sergio Mirazo
    description: This basic program may calculate derivative, integral and plot a function,
    using symbolic calculus (sympy) and gnuplot (pygnuplot). This program is used by my students
    of ARJE Club de Ciencias, in my physics and math courses. Gnuplot must be installed in your pc:
    (http://www.gnuplot.info/download.html)
    version: 1.0.0
    date: APR/15/2023
"""

import tkinter as tk
import sympy as sp
from pygnuplot import gnuplot

root= tk.Tk()

window = tk.Canvas(root, width=500, height=500, relief='raised', bg='#57E0C0')
window.pack()

label1 = tk.Label(root, text='Calculus and plots', bg='#57E0C0', fg='#3210AF')
label1.config(font=('helvetica', 16))
window.create_window(250, 125, window=label1)

label2 = tk.Label(root, text='Enter the function [Use python format]:')
label2.config(bg='#57E0C0', fg='#3210AF', font=('helvetica', 12))
window.create_window(250, 200, window=label2)

label3 = tk.Label(root, text=' ',
                      font=('helvetica', 12), bg='#57E0C0', fg='#3210AF')
window.create_window(250, 350, window=label3)
label4 = tk.Label(root, text=' ', bg='#57E0C0', fg='#3210AF', font=('helvetica', 12,
                                                       'bold'))
window.create_window(250, 380, window=label4)

entry1 = tk.Entry(root) 
window.create_window(250, 240, window=entry1)


def derivar():
    global label3
    global label4
    label3.destroy()
    label4.destroy()
    fun = entry1.get()
    print(fun)
    label3 = tk.Label(root, text='The derivate of ' + fun + ' is: ',
                      font=('helvetica', 12))
    window.create_window(250, 350, window=label3)
    der = sp.diff(fun, 'x')
    label4 = tk.Label(root, text=der, font=('helvetica', 12,
                                                       'bold'))
    window.create_window(250, 380, window=label4)

def integrar():
    global label3
    global label4
    label3.destroy()
    label4.destroy()
    fun = entry1.get()
    x = sp.Symbol('x')
    print(fun)
    label3 = tk.Label(root, text='The integral of ' + fun + ' is: ',
                      font=('helvetica', 12))
    window.create_window(250, 350, window=label3)
    integral = sp.integrate(fun, x)
    label4 = tk.Label(root, text=str(integral)+' + C', font=('helvetica', 12,
                                                       'bold'))
    window.create_window(250, 380, window=label4)

def graficar():
    global label3
    global label4
    label3.destroy()
    label4.destroy()
    fun = entry1.get()
    label3 = tk.Label(root, text='Plotting ' + fun,
                      font=('helvetica', 12))
    window.create_window(250, 350, window=label3)
    from PyGnuplot import gp
    figure1 = gp()    
    figure1.a("plot "+fun)
    
button1 = tk.Button(text='Derivate',
                    command=derivar, bg='#0E0F4D',
                    fg='white', font=('helvetica', 12, 'bold'))
window.create_window(150, 300, window=button1)

button2 = tk.Button(text='Integrate',
                    command=integrar, bg='#0E530D',
                    fg='white', font=('helvetica', 12, 'bold'))
window.create_window(250, 300, window=button2)

button3 = tk.Button(text='Plot',
                    command=graficar, bg='#4C0F0D',
                    fg='white', font=('helvetica', 12, 'bold'))
window.create_window(350, 300, window=button3)

root.mainloop()
