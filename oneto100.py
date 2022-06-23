#Este script escribe numeros del 1 al 100 en un archivo .txt, luego crea el archivo "output1.txt" en la carpeta donde se ejecuta

with open ("output1.txt","w") as file:
    print("script ejecutandose...")
    for n in range(1,101):
        file.write(str(n) + '\n')

print("listo :)")
    
    
    
    
    
    

