'''
import os
peliculas = []

def borrar_pantalla():
    os.system("cls")
    

def agregar_peliculas():
    nombre=print("Ingresa el nombre: ")
    peliculas.append(nombre)
    
def eliminar_pelicula():
    nombre=print("Ingresa el nombre: ")
    if nombre in peliculas:
        peliculas.remove(nombre)
    else:
        print("Pelicula no encontrada")

def modificar_pelicula():
    nameold=input("Ingresa el nombre de la pelicula")
    namenew=input("Ingresa el nuevo nombre de la pelicula")
    if nameold in peliculas:
        indice=peliculas.index(nameold) 
        peliculas[indice] = namenew
    else:
        print("pelicula no encontrada")
        
def consultar_pelicula():
    print(".:: Consultar Peliculas ::.")
    print(peliculas)
    
def buscar_pelicula():
    peli_buscar=input("Escriba la pelicula a buscar")
    for i in range(0, len (peliculas)):
        if peliculas[i]==peli_buscar:
            print("La pelicula si está")
        else:
            print("La pelicula no fue encontrada")
            
def esperar():
    input("Oprima cualquier tecla para continuar")

'''


import os

# Crear lista de peliculas
peliculas = []

def borrar_pantalla():
    os.system("cls")

def obtener_1_4(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor in [1,2,3,4]:
                return valor
            else:
                print("Selecciona un número del 1 al 4. Porfavor vuelva a intentar.")
        except ValueError:
            print("Asegurese de ingresar un número entero.")

def agregar_peliculas():
    opc = True
    while opc:
        pelicula = input("Ingresa la película que quieras agregar: ")
        global peliculas
        peliculas.append(pelicula)
        respuesta = input("¿Desea ingresar otra película? (SI/NO) ").upper().strip()
        if respuesta == "SI":
            opc = True
        elif respuesta == "NO":
            opc = False

def eliminar_peliculas():
    opc = True
    while opc:
        pelicula = input("Ingresa la película que quieras borrar: ")
        global peliculas
        if pelicula in peliculas:
            peliculas.remove(pelicula)
        respuesta = input("¿Desea borrar otra película? (SI/NO) ").upper().strip()
        if respuesta == "SI":
            opc = True
        elif respuesta == "NO":
            opc = False

def modificar_peliculas():
    opc = True
    while opc:
        global peliculas
        for i in range (0, len(peliculas)):
            print(f"{i}.- {peliculas[i]}")
        pelicula = input("Ingrese el número de la película que desea modificar: ")
        nueva_peli = input("Ingresa el nuevo nombre de la película: ")
        peliculas[pelicula]