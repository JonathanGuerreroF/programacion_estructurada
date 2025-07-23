# Funciones Calificaciones

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n\t\U0001F501 ...Oprima cualquier tecla para continuar... \U0001F501")
  input()  
  
def menuPrincipal():
     print("\n\t\t \U0001F4DD ..::: Sistema de Gestión de Calificaciones :::... \U0001F4DD \n")
     print("\t\t \u0031\uFE0F\u20E3  Agregar Calificaciones \U0001F4DD\n\t\t \u0032\uFE0F\u20E3  Mostrar Calificaciones \U0001F50D\n\t\t \u0033\uFE0F\u20E3  Calcular Promedio \U0001F4BE\n\t\t 4.-Buscar Calificaciones \u0035\uFE0F\u20E3  SALIR \U0001F6AA")
     opcion=input("\n\t\tElige una opción: ").upper()
     return opcion

def agregarCalificaciones(lista):
    borrarPantalla()
    print("\U0001F4BE ..::Agregar Calificaciones::.. \U0001F4BE ")
    nombre=input("\U0001F464 Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"\U0001F4DD Calificacion {i}: "))
                if (cal>=0) and (cal<11):
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\u26A0 Ingresa un número valido \u26A0")
            except ValueError:
                print("\u26A0 Ingresa un valor numerico \u26A0")                
    lista.append([nombre]+calificaciones)
    print("\u2705 ..::Accion Realizada con Exito!::..\u2705 ")

def mostrarCalificaciones(lista):
     borrarPantalla()
     print("\U0001F50D \U0001F4CA .:: Mostrar Calificaciones ::. \U0001F4CA \U0001F50D  \n " )  
     print(f" \U0001F464 {'Nombre':<15}{' \U0001F4DA Cal1':<10}{' \U0001F4DA Cal2':<10}{' \U0001F4DA  Cal3':<10}")
     print(f"{'-'*42}")
     if len(lista)>0:
        for fila in lista:
            print(F"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print(f"{'-'*42}")
            cuantos=len(lista)
            print(f"Son {cuantos} alumnos")
     else:
        print("\u274C No hay calificaciones registradas en el sistema \u274C ")
         
def promedios(lista):
    borrarPantalla()
    print("\U0001F4DD \u2797  ..::PROMEDIOS::.. \u2797 \U0001F4DD")
    if len(lista)>0:
        print(f"{' \U0001F464 Alumno':<15}{' \U0001F4D8 Promedio':<10}")
        print(f"{'-'*40}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            promedio=sum(fila[1:])/3
            print(f"\U0001F464 {nombre:<15} \U0001F4D8 {promedio:.2f}")
            promedio_grupal+=promedio
            print(f"{'-'*40}")       
        promedio_grupal=promedio_grupal/len(lista)              
        print(f"El promedio grupal es: {promedio_grupal}")
    else:
        print("\u274C No hay calificaciones en el sistema \u274C ")
        
def buscarCalificacion(lista):
    borrarPantalla()
    print("..:: BUSCAR CALIFICACIONES::..")
    nom=input("Ingrese el nombre del alumno a buscar: ").upper().strip()
    encontrado=False
    if len(lista)>0:
        for i in lista:
            if i[0] == nom:
                print(f"{'|'}{'-'*40}{'|'}")
                print(F"{'|'}{'Nombre':<10}{'Cali1':<10}{'Cali2':<10}{'Cali3':<10}{'|'}")
                print(f"{'|'}{'-'*40}{'|'}")
                print(f"{'|'}{i[0]:<10}{i[1]:<10}{i[2]:<10}{i[3]:<10}{'|'}")
                print(f"{'|'}{'-'*40}{'|'}")
                encontrado=True
    else:
        print("No hay calificaciones registradas")
    if not encontrado:
        print("No se encontró al alumno")
        
        
        
# def modificarCalificacion(lista):
    
    
# def borrarCalificacion(lista):        
            

                

















# def calcularPromedio(lista):
#     borrarPantalla()
#     print(" \U0001F4BE ..::Calcular Promedio::..")
#     if len(lista) == 0:
#         print(" \u274C No hay calificaciones agregadas \u274C ")
        
#     print(f" \U0001F468\u200D\U0001F393 {'Nombre':<15}{'\U0001F4DA Cal1':<10}{' \U0001F4DA Cal2':<10}{'\U0001F4DA  Cal3':<10}{' \U0001F4DA Promedio':<10}")
#     print(f"{'-'*42}")
#     for fila in lista:
#         nombre=fila[0]
#         cal1=fila[1]
#         cal2=fila[2]
#         cal3=fila[3]
#         promedio=(cal1+cal2+cal3) / 3
#         print(f" \U0001F468\u200D\U0001F393  {nombre:<15}{cal1:<10}{cal2:<10}{cal3:<10}{promedio:<10}")



#  def calcularPromedio(lista):
#      borrarPantalla()
#      print("\U0001F4BE  .:: Calcular Promedio de Calificaciones ::.\n")  # 💾
#      if len(lista) == 0:
#          print("\u274C No hay calificaciones registradas en el sistema.\n")  # ❌
#          return
#      print(f"{'Nombre':<15} {'Cal1':<6} {'Cal2':<6} {'Cal3':<6} {'Promedio':<10}")
#      print("-" * 50)
#      for alumno in lista:
#          nombre = alumno[0]
#          cal1 = alumno[1]
#          cal2 = alumno[2]
#          cal3 = alumno[3]
#          promedio = round((cal1 + cal2 + cal3) / 3, 2)
#          print(f"{nombre:<15} {cal1:<6} {cal2:<6} {cal3:<6} {promedio:<10}")
    
#     print("\n\u2705 Promedios calculados correctamente.")  # ✅
