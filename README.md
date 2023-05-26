# Presentación
<p align="center"><img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png"width="200" height="200">
</img><br>
<i><b>Docente:</b></i> Camilo Rodriguez
<br>
<i><b>Asignatura:</b></i> Big Data
<br>
<i><b>Estudiante:</b></i> Edna Sofía Orjuela Puentes <br> Herlendy Alejandro Sánchez Gaitán
<br>
<i><b>Tema:</b></i> Tercer Parcial.
<br>
<i><b>Fecha:</b></i>24/05/23
<br>
</p>

# Objetivo
 Implementar un sistema de procesamiento y monitoreo de datos financieros utilizando tecnologías como PySpark, AWS Glue, AWS Kinesis y QuickSight. 
# Procedimiento
1.  Dibujar franjas de Bollinger con una ventana de 20 horas en Quick Sight para el proyecto del precio del dólar (posiblemente se necesite una consulta en athena).

    https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/bollinger-bands#:~:text=Bollinger%20Bands%20are%20envelopes%20plotted,Period%20and%20Standard%20Deviations%2C%20StdDev.

2.  Crear un pipeline de procesamiento para los datos de noticias del parcial 2 usandoPyspark ML. Se debe vectorizar usando TFxIDF. Implementar el pipeline en AWS GLUE o ejecutarlo en EMR con spark submit.
    Usar de guía:

    https://spark.apache.org/docs/latest/ml-pipeline.html

3. Implementar 2 productores que envíen datos de las acciones(como el ejemplo de clase) a un stream en AWS Kinesis. Implementar un consumidor que se encargue de tomar de la cola y muestre una alerta cada vez que el precio de alguna acción supera la franja superior de Bollingener. Implementar un segundo consumidor que se encargue de tomar de la cola y muestre una alerta cada vez que el  precio de alguna acción esté por debajo de la franja inferior de Bollingener. Cada uno de los productores y consumidores deben estar en una máquina EC2.


# Resultados
* **Primer punto:**

1. Se crea una vista para agregar una columna con la desviación estándar móvil: 

   *SELECT   date,close,STDDEV_POP(close) OVER (ORDER BY date ROWS BETWEEN 19
   PRECEDING AND CURRENT ROW) AS moving_std 
   FROM "AwsDataCatalog"."dolarparcial3"."parcial3_dolar";*

2. Se calcula la media y la desviación estándar mòvil:

   *Media movil: windowAvg(sum(close), [date ASC],19,0)*

   *std inferior: {media movil}-(2*sum({moving_std}))*

   *std superior: {media movil}+(2*sum({moving_std}))*

![image](https://github.com/edso2103/Parcial3-BigData/assets/65740725/47946118-fc4a-429a-a09e-f51c1c05574b)

Imagen creada en QuickSight

![image](https://github.com/edso2103/Parcial3-BigData/assets/65740725/cb9d4e95-fad0-473f-8ebb-f9552240dd7a)

Imagen creada por : https://www.banrep.gov.co/es/estadisticas/comportamiento-del-mercado-del-dolar-durante-el-dia-informacion-tiempo-real

El codigo realizado anteriormente para obtener la información usada, se puede consultar en: https://github.com/edso2103/SegundaParte_DespliegueContinuo.

Y los resultados obtenidos, se encuentran en la primera carpeta, donde además, están los resultados obtenidos de un csv generado con solo 20 datos de yahoo finance.

* **Segundo punto:**
  
 ![Captura desde 2023-05-24 15-05-29](https://github.com/edso2103/Parcial3-BigData/assets/65740725/74d8ff68-ba53-442a-85b4-b48b1c5aa9cd)
 ![Captura desde 2023-05-24 15-06-50](https://github.com/edso2103/Parcial3-BigData/assets/65740725/14371901-7510-4491-a962-29330bd4597d)

Para realizar este ejercicio se usó EMR y se importó PySpark para su correcta tokenización, el notebook se encuentra en la capeta segundoPunto.

* **Tercer punto:**

En este ejercicio se crean 2 productores y dos consumidores para generar una alerta cuando el dolar este por encima o por debajo de las franjas de bollinger.


![Captura desde 2023-05-25 22-18-49](https://github.com/edso2103/Parcial3-BigData/assets/65740725/9ccfd415-936a-4d6d-8691-798272333b7c)

![Captura desde 2023-05-25 22-19-32](https://github.com/edso2103/Parcial3-BigData/assets/65740725/a8e4e5cd-1163-4fba-8161-7c66fae0528a)

![Captura desde 2023-05-25 22-19-52](https://github.com/edso2103/Parcial3-BigData/assets/65740725/39c2c141-bbdd-4cc6-a411-add3216dda76)



