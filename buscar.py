import os
import subprocess

# Función para encontrar todos los archivos parecidos
def buscar_parecidos(nombre_archivo, ruta_carpeta):
    archivos_parecidos = []
    for ruta_actual, carpetas, archivos in os.walk(ruta_carpeta):
        for archivo in archivos:
            archivo_filtro = archivo.lower()
            # Buscamos que sean extensión de karaoke .cdg y no mp3
            if archivo_filtro.endswith(".cdg") and nombre_archivo in archivo_filtro:
                ruta_completa = os.path.join(ruta_actual, archivo)
                archivos_parecidos.append(ruta_completa)

    return archivos_parecidos

# Función para recortar el archivo y ponerlo como carpeta
def recortar_ultima_carpeta(ruta):
    ruta_sin_ultimo = os.path.dirname(ruta)
    return ruta_sin_ultimo


# Defino la ruta que voy a buscar
ruta_carpeta_buscar = "D:\Canciones"

#Inicio del programa
print("Bienvenida al buscador de canciones hecha por Pepe :D")
input_nombre_archivo_buscar = input("Ingrese el nombre del archivo a buscar por favor:")
# Quitamos los espacios iniciales y finales
limpiar_input_espacios = input_nombre_archivo_buscar.strip()
nombre_archivo_buscar =limpiar_input_espacios.lower()

# Inicio de busqueda
if nombre_archivo_buscar is not None:
    #Busco las rutas parecidas
    rutas_parecidas = buscar_parecidos(nombre_archivo_buscar,ruta_carpeta_buscar)
    contador = 1
    cantidad_rutas =len(rutas_parecidas)

    if cantidad_rutas > 1:
        print("Estas son las rutas que se encontraron con ese nombre:")
        for rutas in rutas_parecidas:
            print("  ",contador, "  ---->  ",rutas)
            contador+=1
        num_archivo_a_buscar = int(input("¿Cuál le gustaría abrir?, Ingresa el número del archivo:"))
        nombre_archivo_buscar_individual =rutas_parecidas[num_archivo_a_buscar-1]
    elif(cantidad_rutas ==1):
        nombre_archivo_buscar_individual =rutas_parecidas[0]
        print("Solo se encontró un archivo con ese nombre")
        print(f"Se encontró el archivo en: {nombre_archivo_buscar_individual}")
    else:
        print("No se encontró ningún archivo con ese nombre. No utilizar caracteres especiales para buscar, por ejemplo: '{}*_()-+%, etcétera.")
        input("Presione enter para salir")
        exit()

    # Finalmente abrimos el archivo
    input("Presione enter para abrir la carpeta")
    ruta_recortada = recortar_ultima_carpeta(nombre_archivo_buscar_individual)
    try:
        subprocess.run(['explorer', ruta_recortada], check=True)
    except subprocess.CalledProcessError as e:
        print("")   
        # print(f"No se pudo abrir la carpeta: {e}")
    # input("Listo, presione enter para cerrar el buscador :)")
else:
    print("No se encontraron carpetas con ese nombre. :(")
    input("Presione enter para cerrar") 

