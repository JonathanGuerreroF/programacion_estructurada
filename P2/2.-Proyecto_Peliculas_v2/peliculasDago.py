# peliculas=[]

#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero e idioma)

# peliculas={
#           "nombre":"",
#           "categoria":"",
#           "genero":"",
#           "idioma":""
  
pelicula={}


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n\t...Oprima cualquier tecla para continuar ...")
  input()  

def crearPeliculas():
  borrarPantalla()
  print("\U0001F4DD  .:: Alta de Películas ::. \n")  # 📝
  pelicula.update({"\U0001F4DD nombre":input("Ingresa el nombre: ").upper().strip()})
  pelicula.update({"\U0001F4DD categoria":input("Ingresa la categoria: ").upper().strip()})
  pelicula.update({"\U0001F4DD clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
  pelicula.update({"\U0001F4DD genero":input("Ingresa el genero: ").upper().strip()})
  pelicula.update({"\U0001F4DD idioma":input("Ingresa el idioma: ").upper().strip()})
  print("\n\t\U0001F389 ..:::: La operación se realizó con éxito :::..")  # 🎉

def mostrarPeliculas():
  borrarPantalla()
  print("\U0001F50D  .:: Consultar Película ::. \n")  # 🔍
  if len(pelicula) > 0:
    for i in pelicula:
      print(f"\t{(i)}: {pelicula[i]}")
  else:
    print("\t\u274C No hay películas en el sistema.")  # ❌


def borrarPeliculas():
  borrarPantalla()
  print("\U0001F4DB  .:: Borrar TODAS las Películas ::. \n")  # 📛
  resp = input("\u26A0 \u26A0 ¿Deseas borrar todas las películas del sistema? \u26A0 \u26A0 (SI/NO): ").upper()
  if resp == "SI":
    pelicula.clear()
    print("\n\t\u2705 Películas eliminadas correctamente.")  # ✅
  else:
    print("\n\t\u274C Operación cancelada.")  # ❌

    
def agregarCaracteristicaPeliculas():
  borrarPantalla()
  print(".:: Agregar Caracteristicas a Peliculas ::. \n")
  atributo= input("Ingresa la nueva caracteristica de la pelicula").lower().strip()
  valor=input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
  pelicula.update({atributo:valor})
  pelicula[atributo]=valor
  
def modificarCaracteristicaPeliculas():
   borrarPantalla()
   print("Modificar caracteristicas de peliculas")
   if len(pelicula)>0:
      print("Valores actuales")
      for i in pelicula:
         print(f"{(i)} : {pelicula[i]}")
         resp = input("Desea modificar una caracteristica?(Si/No)").lower().strip()
         if resp =="si":
          pelicula.update({i: input("El nuevo valor: ").upper().strip()})
          print("La operación se ha realizado con exito")
          esperarTecla()
         borrarPantalla()
   else:
      print("No hay peliculas en el sistema")
      esperarTecla()  

def borrarCaracteristicasPeliculas():
  borrarPantalla()
  print("\U0001F4DB .:: Borrar Características de la Película ::.\n")  # 📛
  if not pelicula:
    print("\t\u274C No hay películas registradas.")  # ❌
    return
  print("Características actuales:")
  for clave, valor in pelicula.items():
    print(f"\t{clave}: {valor}")
  clave_a_borrar = input("\n📝 Escribe exactamente el nombre de la característica que deseas borrar: ").strip()
  try:
    if clave_a_borrar in pelicula:
      del pelicula[clave_a_borrar]
      print("\n\t\u2705 ¡Característica borrada con éxito!")  # ✅
    else:
      raise KeyError
  except KeyError:
    print("\n\t\u274C Esa característica no existe. Intenta escribirla tal cual aparece.")






# def borrarCaracteristicasPeliculas():
  borrarPantalla()
  print(".:: Borrar Características de la Película ::.\n")
  if len(pelicula) == 0:
    print("\t..:: No hay películas registradas ::..")
    return
  print("Características actuales de la película:")
  for clave in pelicula:
    print(f"\t{clave}: {pelicula[clave]}")
  clave_a_borrar = input("\nEscribe el nombre de la característica que deseas borrar: ").lower().strip()
  if clave_a_borrar in pelicula:
    pelicula.pop(clave_a_borrar)
    print("\n\t..:::: ¡Característica borrada con éxito! ::::..")
  else:
    print("\n\t..:: Esa característica no existe ::..")



#MODIFICAR MIO
# def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print(".:: Modificar Caracteristicas de Peliculas ::. \n")
    if len(pelicula) > 0:
        atributo = input("¿Qué característica deseas modificar?: ").lower().strip()
        if atributo in pelicula:
            nuevo_valor = input(f"Ingresa el nuevo valor para {atributo}: ").upper().strip()
            pelicula[atributo] = nuevo_valor
            print("\n\t..:::: La operacion se realizo con exito::::..")
        else:
            print("\n\t..:::: La caracteristica no existe ::::..")
    else:
        print("\n\t..:::: No hay peliculas en el sistema ::::..")







# def consultarPeliculas():
#   borrarPantalla()
#   print("\n\t.:: Consultar Peliculas ::.")
#   if len(peliculas)>0:
#     for i in range(0,len(peliculas)):
#       print(f"{i+1}: {peliculas[i]}")
#   else:
#     print("No hay peliculas en el sistema")
    
# def vaciarPeliculas():
#     borrarPantalla()
#     print("\n\t..:::Borrar o Eliminar Todas las peliculas::..")
#     resp=input("Deseas quitar o borrar todas las peliculas del sistema? SI/NO ").upper()
#     if resp=="SI":
#         peliculas.clear()
#         input("\n\t..:::: La operacion se realizo con exito::::..")
#     else:
#         input("\n\t..:::: Volviendo atras::::..")
        
# def buscarPeliculas():
#     borrarPantalla()
#     print("\n\t..:: Buscar peliculas::..")
#     pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
#     encontro=0
#     if not(pelicula_buscar in peliculas):
#         print("\n\t\t..::No se encontró la pelicula a buscar")
#     else:
#         for i in range(0,len(peliculas)):
#             if pelicula_buscar==peliculas[i]:
#                 print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i+1}")
#                 encontro+=1
#         if encontro>0:
#             print(f"Tenemos {encontro} peliculas con este titulo")
#             input("\n\t..:::: La operacion se realizo con exito::::..")
            
# def eliminarPeliculas():
#     borrarPantalla()
#     print("\n\t..:: Borrar peliculas::..")
#     pelicula_borrar=input("Ingrese el nombre de la pelicula que desea borrar: ").upper().strip()
#     found=0
#     if not(pelicula_borrar in peliculas):
#         print("No se encontro ninguna pelicula con ese nombre")
#     else: 
#         respuesta="SI"
#         while pelicula_borrar in peliculas and respuesta=="SI":
#             respuesta=input("¿Deseas quitar o borrar la pelicula del sistema? SI/NO ").upper()
#             if respuesta=="SI":
#                 posicion=peliculas.index(pelicula_borrar)
#                 print(f"La pelicula que se borró fue {pelicula_borrar} y estaba en la casilla {posicion+1}")
#                 peliculas.remove(pelicula_borrar)
#                 found+=1
#                 input("\n\t...:: La operacion se realizó con exito::..")
#         print(f"Se borro {found} pelicula(s) con este titulo")        

# def modificarPelicula():
  #  borrarPantalla()
  #  print("\n\t.:: Modificar Películas ::. \n")
  #  pelicula_buscar=input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
  #  encontro=0
  #  if not(pelicula_buscar in peliculas): 
  #     print("\n\t\t ¡No se encuentra la película a buscar!")   
  #  else:   
  #     for i in range(0,len(peliculas)):
  #       if pelicula_buscar==peliculas[i]:
  #         resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
  #         if resp=="si":
  #            peliculas[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
  #            encontro+=1
  #            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      
  #     print(f"\nSe modifico {encontro} pelicula(s) con este titulo")
