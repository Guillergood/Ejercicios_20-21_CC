# Ejercicios del tema 2

## Ejercicio 1

> Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).

Para instalar ```nvm``` se deben seguir los siguientes pasos:
Se descarga el script para instalarlo
```bash
curl -sL https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh -o install_nvm.sh
```
Se instala
```bash
bash install_nvm.sh
```
Se refresca el archivo profile para usar ```nvm```
```bash
source ~/.profile
```
Se listan las versiones con:
```bash
nvm ls-remote
```
Se descarga la versión impar más reciente (v14.13.0) y la minor más reciente (v4.9.1):
```bash
nvm install v4.9.1
nvm install v14.13.0
```

## Ejercicio 2

> Crear una descripción del módulo usando package.json. En caso de que se trate de otro lenguaje, usar el método correspondiente.

Para crear un módulo voy a usar el gestor de paquetes ```npm```

```bash
sudo apt install npm
```
Para generar el archivo ```package.json``` hay que ejecutar:
```bash
npm init
```
Y para instalar una dependencia:
```bash
npm install docco grunt-docco --save-dev
```

## Ejercicio 3

> Descargar el repositorio de ejemplo anterior, instalar las herramientas necesarias (principalmente Scala y sbt) y ejecutar el ejemplo desde sbt. Alternativamente, buscar otros marcos para REST en Scala tales como Finatra o Scalatra y probar los ejemplos que se incluyan en el repositorio.

Antes de seguir las instrucciones del [repositorio](https://github.com/JJ/spray-test) , se instala el jdk de java, scala y sbt, siguiendo las siguientes [instrucciones](https://www.scala-sbt.org/release/docs/Installing-sbt-on-Linux.html):
```bash
sudo apt-get install openjdk-8-jdk
```
```bash
sudo apt install scala
```
```bash
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
sudo apt-get update
sudo apt-get install sbt
```

Se clona el repositorio:
```bash
git clone https://github.com/JJ/spray-test
```

Se intenta ejecutar el proyecto, pero no funciona de esta manera. 

Se instalan las dependencias con ```brew```

```sbt
sbt compile
> test
```

```sbt
> re-start
```


```sbt
curl http://localhost:8080
curl -X PUT http://localhost:8080/0/0/Test1 
curl -X PUT http://localhost:8080/0/5/Test1                                  
curl -X PUT http://localhost:8080/5/21/Test8000
curl http://localhost:8080/Test8000    
```

## Ejercicio 4
> Para la aplicación que se está haciendo, escribir una serie de aserciones y probar que efectivamente no fallan. Añadir tests para una nueva funcionalidad, probar que falla y escribir el código para que no lo haga. A continuación, ejecutarlos desde mocha (u otro módulo de test de alto nivel), usando descripciones del test y del grupo de test de forma correcta. Si hasta ahora no has subido el código que has venido realizando a GitHub, es el momento de hacerlo, porque lo vamos a necesitar un poco más adelante.

Para agregar tests en Spring sólo haría falta añadir los archivos en la carpeta de ```test```.

Se han hecho dos test, uno que da error.



Después se agrega



## Ejercicio 5

> Haced los dos primeros pasos antes de pasar al tercero.

Voy a agregar Travis CI al repositorio, como lo tenía configurado de antes no se muestra el mensaje de bienvenida.

Se liga el repositorio y una vez agregado el archivo ```.travis.yaml``` 

```yaml
language: java
jdk:
  - oraclejdk15
```

Se ejecutan los test.

Se muestra los test iniciales que fallan.

Por último, se han arreglado y ahora se muestran los test arreglados.