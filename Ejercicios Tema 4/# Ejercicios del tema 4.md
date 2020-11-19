
## Ejercicio 1

> Haced los dos primeros pasos antes de pasar al tercero.

Voy a agregar Travis CI al repositorio, como lo tenía configurado de antes no se muestra el mensaje de bienvenida.

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%202/20.png)

## Ejercicio 2

Para agregar tests en Spring sólo haría falta añadir los archivos en la carpeta de ```test```.

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%202/11.png)

Se han hecho dos test, uno que da error.

![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%202/14.png)

Se liga el repositorio en la plataforma de TravisCI y una vez agregado el archivo ```.travis.yaml``` al proyecto con la configuración.

```yaml
language: java
jdk:
  - oraclejdk15
```

Se ejecutarán los test en las siguientes subidas de código.

Por último, se han arreglado y ahora se muestran los test arreglados que pasan.



![](https://raw.githubusercontent.com/Guillergood/Ejercicios_20-21_CC/main/Ejercicios%20Tema%202/18.png)

