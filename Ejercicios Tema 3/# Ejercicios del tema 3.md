# Ejercicios del tema 3

## Ejercicio 1

> Buscar alguna demo interesante de Docker y ejecutarla localmente, o en su defecto, ejecutar la imagen anterior y ver cómo funciona y los procesos que se llevan a cabo la primera vez que se ejecuta y las siguientes ocasiones.

Después de instalar ```Docker``` se ejecuta el anterior ejemplo de esta guía:

```bash
docker run --rm jjmerelo/docker-daleksay -f smiling-octopus JELOUDA
```

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%203/1.png)

Como se aprecia en la imagen, al no tenerlo localmente docker lo busca en el `docker hub` y se lo descarga. Al ejecutarlo una segunda vez, no salen más mensajes y aparece directamente la salida del programa.

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%203/2.png)

## Ejercicio 2

> Tomar algún programa simple, “Hola mundo” impreso desde el intérprete de línea de órdenes, y comparar el tamaño de las imágenes de diferentes sistemas operativos base, Fedora, CentOS y Alpine, por ejemplo.

Después de descargar las diferentes imagenes que se piden, ejecutando:

`bash
docker pull fedora
docker pull alpine
docker pull centos
`

Para ver el tamaño de cada uno con el comando ```docker images``` dá el siguiente resultado:


```
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
fedora              latest              eb17aa5c154f        11 days ago         175MB
alpine              latest              d6e46aa2470d        2 weeks ago         5.57MB
centos              latest              0d120b6ccaa8        2 months ago        215MB
```
Claramente, la imagen `alpine` es la que tiene menos tamaño.

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%203/3.png)

## Ejercicio 3

> Crear a partir del contenedor anterior una imagen persistente con *commit*.

Para realizar el commit se va a utilizar la imagen de `alpine`.

Con el comando `sudo docker ps -a` se ve podrá ver el ID del contenedor para hacer el commit:

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%203/4.png)

Para después ejecutar `sudo docker commit d02b9959ffbc test-ejercicio-3` para que guarde el estado actual del contenedor.

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%203/5.png)

## Ejercicio 4

> Examinar la estructura de capas que se forma al crear imágenes nuevas a partir de contenedores que se hayan estado ejecutando.

Hay dos formas de verlo, con el comando `docker history` y con un comando interesante, ya que proporciona más información que es `dive`

Siguiendo las instrucciones para [instalar](https://github.com/wagoodman/dive) en Ubuntu :

`bash
wget https://github.com/wagoodman/dive/releases/download/v0.9.2/dive_0.9.2_linux_amd64.deb
sudo apt install ./dive_0.9.2_linux_amd64.deb
`
Después se ejecuta `dive alpine` y esta es la imagen que sale:

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%203/6.png)

## Ejercicio 5

> Crear un volumen y usarlo, por ejemplo, para escribir la salida de un programa determinado.

Se crea el volumen:

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%203/7.png)

Se escribe un ejemplo en `bash` para imprima en pantalla algo:

```bash
#!/bin/bash
echo "Hello World"
```

Para hacer que el volumen ejecute este programa hay que especificarlo en un archivo llamado Dockerfile
```bash
FROM fedora:latest

WORKDIR /home/guillermo

ADD . /elDestino

COPY bash.sh ./

CMD ["bash", "./bash.sh"]
```
Añadimos una carpeta de destino con ```ADD . /elDestino```

Después se utiliza para construirlo usando el siguiente comando:

`docker build --no-cache -t fedora_test -f Dockerfile .` 

Por último se montar con el comando:

`docker run --mount source=esteEsMiVolumen,destination=/elDestino fedora_test`

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%203/8.png)




