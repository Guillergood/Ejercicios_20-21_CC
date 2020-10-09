## **Ejercicio 1.**

#### Buscar una aplicación de ejemplo, preferiblemente propia, y deducir qué patrón es el que usa. ¿Qué habría que hacer para evolucionar a un patrón tipo microservicios?

Para realizar este ejercicio he decidido mostrar una parte mi Trabajo Final de Grado, [Cognimobile Dashboard](https://github.com/Guillergood/CognimobileDashboard).

Se ha desarrollado bajo una arquitectura por capas, utilizando el framework Laravel. La aplicación tiene una capa de visualización, otra de lógica y una última de datos. Para hacer evolucionar la aplicación habría que separar las distintas entidades en diferentes microservicios y que se comunicasen entre ellos para dar un servicio. 