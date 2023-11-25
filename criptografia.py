import pandas as pd

def codificar_mensaje(mensaje, matriz_codificadora):
    mensaje_codificado = ""
    
    for letra in mensaje:
        if letra in matriz_codificadora:
            mensaje_codificado += matriz_codificadora[letra]
        else:
            mensaje_codificado += letra
    
    return mensaje_codificado

def decodificar_mensaje(mensaje_codificado, matriz_decodificadora):
    mensaje_decodificado = ""
    
    for letra in mensaje_codificado:
        if letra in matriz_decodificadora:
            mensaje_decodificado += matriz_decodificadora[letra]
        else:
            mensaje_decodificado += letra
    
    return mensaje_decodificado

matriz_codificadora = {
    'A': 'Q',
    'B': 'W',
    'C': 'E',
    'D': 'R',
    'E': 'T',
    #...
    #Agrega aquí el resto de las letras y sus correspondientes codificaciones
}

matriz_decodificadora = {v: k for k, v in matriz_codificadora.items()}

mensaje = "HOLA MUNDO"

mensaje_codificado = codificar_mensaje(mensaje, matriz_codificadora)
print("Mensaje codificado:", mensaje_codificado)

mensaje_decodificado = decodificar_mensaje(mensaje_codificado, matriz_decodificadora)
print("Mensaje decodificado:", mensaje_decodificado)import pandas as pd

def codificar_mensaje(mensaje, matriz_codificadora):
    mensaje_codificado = ""
    
    for letra in mensaje:
        if letra in matriz_codificadora:
            mensaje_codificado += matriz_codificadora[letra]
        else:
            mensaje_codificado += letra
    
    return mensaje_codificado

def decodificar_mensaje(mensaje_codificado, matriz_decodificadora):
    mensaje_decodificado = ""
    
    for letra in mensaje_codificado:
        if letra in matriz_decodificadora:
            mensaje_decodificado += matriz_decodificadora[letra]
        else:
            mensaje_decodificado += letra
    
    return mensaje_decodificado

matriz_codificadora = {
    'A': 'Q',
    'B': 'W',
    'C': 'E',
    'D': 'R',
    'E': 'T',
    #...
    #Agrega aquí el resto de las letras y sus correspondientes codificaciones
}

matriz_decodificadora = {v: k for k, v in matriz_codificadora.items()}

mensaje = "HOLA MUNDO"

mensaje_codificado = codificar_mensaje(mensaje, matriz_codificadora)
print("Mensaje codificado:", mensaje_codificado)

mensaje_decodificado = decodificar_mensaje(mensaje_codificado, matriz_decodificadora)
print("Mensaje decodificado:", mensaje_decodificado)
