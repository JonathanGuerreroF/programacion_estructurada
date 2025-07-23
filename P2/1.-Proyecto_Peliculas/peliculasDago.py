peliculas=[]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  peliculas.append(input("Ingresa el nombre: ").upper().strip())
  input("\n\t..:::: La operacion se realizo con exito::::..")

def consultarPeliculas():
  borrarPantalla()
  print("\n\t.:: Consultar Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
      print(f"{i+1}: {peliculas[i]}")
  else:
    print("No hay peliculas en el sistema")
    
def vaciarPeliculas():
    borrarPantalla()
    print("\n\t..:::Borrar o Eliminar Todas las peliculas::..")
    resp=input("Deseas quitar o borrar todas las peliculas del sistema? SI/NO ").upper()
    if resp=="SI":
        peliculas.clear()
        input("\n\t..:::: La operacion se realizo con exito::::..")
    else:
        input("\n\t..:::: Volviendo atras::::..")
        
def buscarPeliculas():
    borrarPantalla()
    print("\n\t..:: Buscar peliculas::..")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\t\t..::No se encontró la pelicula a buscar")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i+1}")
                encontro+=1
        if encontro>0:
            print(f"Tenemos {encontro} peliculas con este titulo")
            input("\n\t..:::: La operacion se realizo con exito::::..")
            
def eliminarPeliculas():
    borrarPantalla()
    print("\n\t..:: Borrar peliculas::..")
    pelicula_borrar=input("Ingrese el nombre de la pelicula que desea borrar: ").upper().strip()
    found=0
    if not(pelicula_borrar in peliculas):
        print("No se encontro ninguna pelicula con ese nombre")
    else: 
        respuesta="SI"
        while pelicula_borrar in peliculas and respuesta=="SI":
            respuesta=input("¿Deseas quitar o borrar la pelicula del sistema? SI/NO ").upper()
            if respuesta=="SI":
                posicion=peliculas.index(pelicula_borrar)
                print(f"La pelicula que se borró fue {pelicula_borrar} y estaba en la casilla {posicion+1}")
                peliculas.remove(pelicula_borrar)
                found+=1
                input("\n\t...:: La operacion se realizó con exito::..")
        print(f"Se borro {found} pelicula(s) con este titulo")        

def modificarPelicula():
   borrarPantalla()
   print("\n\t.:: Modificar Películas ::. \n")
   pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
   encontro=0
   if not(pelicula_buscar in peliculas): 
      print("\n\t\t ¡No se encuentra la película a buscar!")   
   else:   
      for i in range(0,len(peliculas)):
        if pelicula_buscar==peliculas[i]:
          resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
          if resp=="si":
             peliculas[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
             encontro+=1
             print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      
      print(f"\nSe modifico {encontro} pelicula(s) con este titulo")
