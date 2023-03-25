import numpy as np

def biseccion(func,x_L,x_U,tol):
    #Verificar que se cumplan las condiciones para el método de bisección
    if(func(x_L)*func(x_U)>0):
        print('No hay raíces dentro de los límites dados.')
        return None
    num_iteraciones = 0
    x_R = x_L
    #Iterar hasta converger
    while(1):
        x_R = (x_L + x_U)/2
        if(func(x_R) == 0 or (np.abs(x_U-x_L)/2)<tol):
            break
        num_iteraciones += 1
        if(func(x_R)*func(x_L)<0):
            x_U = x_R
        else:
            x_L = x_R
    return x_R,num_iteraciones

#Definir la función
def func(x):
    return x**3-x-1

#Definir los límites
x_L = 1
x_U = 2

#La tolerancia
tol = 1e-5

#Imprimir la raíz encontrada
print('La raíz encontrada es: ', biseccion(func,x_L,x_U,tol)[0])
