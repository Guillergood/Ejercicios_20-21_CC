## Ejercicio 1
>Crear un pod con dos o más contenedores, de forma que se pueda  usar uno desde el otro. Uno de los contenedores contendrá la aplicación  que queramos desplegar.

Para instalar podman se realiza lo siguiente:

```
sudo apt update
sudo apt upgrade
sudo apt install podman
```

Una vez instalado se sigue el tutorial [composición de podman](https://developers.redhat.com/blog/2019/01/15/podman-managing-containers-pods/)


```
sudo podman run \
-d --restart=always --pod=el-contenedor \
-e MYSQL_ROOT_PASSWORD="myrootpass" \
-e MYSQL_DATABASE="wp" \
-e MYSQL_USER="wordpress" \
-e MYSQL_PASSWORD="w0rdpr3ss" \
--name=wptest-db mariadb
```

```
sudo podman run \
-d --restart=always --pod=el-contenedor \
-e WORDPRESS_DB_NAME="wp" \
-e WORDPRESS_DB_USER="wordpress" \
-e WORDPRESS_DB_PASSWORD="w0rdpr3ss" \
-e WORDPRESS_DB_HOST="127.0.0.1" \
--name wptest-web wordpress
```

```
guillermo@Portatil-Guille:~$ sudo podman pod ls
POD ID        NAME         		STATUS   CREATED         INFRA ID      # OF CONTAINERS
51b1611e0cd3  el-contenedor     Running  11 minutes ago  d890a33062ba  3
```

Y con esto ya se tendría en la dirección `localhost:8080` el container de Wordpress.


## Ejercicio 2
>Usar un miniframework REST para crear un servicio web y introducirlo en un contenedor, y componerlo con un cliente REST que sea el que finalmente se ejecuta y sirve como “frontend”.

Utilizando la aplicación de otros ejercicios con Flask, vamos a utilizarlo para componerlo:

```python
from flask import Flask, jsonify, request
import json
app = Flask(__name__)

def define_routes(app):
	@app.route('/')
	def home():
		cuidador = json.dumps({"name": "Alan"})
		animal = json.dumps({"name": "Okapi"})
		report = json.dumps({"name": "Report_1", "reporter": "Alan", "animal": "Okapi", "report": "Okapis are fine! They have eaten everything!"})

		return jsonify([cuidador, animal, report]), 200
		
	@app.route('/insert/cuidador', methods=['POST'])
	def insert_cuidador():
		data_string = request.get_data()
		data = json.loads(data_string)
		
		cuidador_name = data.get('name')


		if cuidador_name:
			return 'Ok', 200
		else:
			return 'Error', 400
		
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

Utilizamos el siguiente Dockerfile para componer el contenedor

```dockerfile
FROM python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
```

Para luego diseñar el `docker-compose.yml` y orquestar los servicios

```yaml
version: '2'
services:
    web:
        build: .
        ports:
            - "5000:5000"
        volumes:
            - .:/code
        depends_on:
            - redis
    redis:
        image: redis

```

Se definen dos servicios, `web` y `redis`. 

El servicio web se crea a partir del Dockerfile en el directorio actual que reenvía el puerto expuesto del contenedor (5000) al puerto 5000 en el host.
Monta el directorio del proyecto en el host en `/code` dentro del contenedor (lo que le permite modificar el código sin tener que reconstruir la imagen).
Y vincula el servicio web al servicio de Redis. El servicio redis utiliza la última imagen de Redis de Docker Hub.

Por último para utilizar la orquestación se usa `docker-compose up` y ya se estaría sirviendo el proyecto.