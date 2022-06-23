""" 1. Crear un codigo de python que:
-crea un archivo en el que escribe numeros del 0 al 100 separados por un salto de linea. x

2. Subir el codigo a un repositorio de github. <---

3. Clonar el repositorio en una nueva carpeta.

4. Crear un docker para el codigo creado en 1. El docker tiene que crear el archivo de python fuera del contendor.

5. Actualizar el repositorio, para subir el dockerfile al repositorio

6. Actualizar la carpeta donde se clono el repositorio """



#Este script escribe numeros del 1 al 100 en un archivo .txt, luego crea el archivo "prueba1.txt" en la carpeta donde se ejecuta

with open ("prueba1.txt","w") as file:
    print("script ejecutandose...")
    for n in range(1,101):
        file.write(str(n) + '\n')

print("listo :)")
    
    
    
    
    
    

