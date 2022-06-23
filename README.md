# proyecto1

Antes de empezar se debe verificar que Docker se encuentra funcionando correctamente.


Los archivos necesarios se encuentran dentro de la carpeta "proyecto1", 
las carpetas que no se necesitan deben especificarse en el archivo ".dockerignore" (por ejemplo la carpeta ".git")


Se debe ejecutar el Dockerfile usando el comando: --> $ sudo docker build -t imagen1 . 

Luego se debe ejecutar la imagen con: --> $  sudo docker run imagen1


Para extraer el "output1.txt" se puede usar: --> " docker cp  ID_CONTAINER:SRC_PATH DEST_PATH "

en este caso usaremos: --> $ sudo docker cp c9ed44f7966c:/home/f1/output1.txt /home/ms/pyprojects1/proyecto1 

