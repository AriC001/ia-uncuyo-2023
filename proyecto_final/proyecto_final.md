<p style="text-align: center;font-size: 24px;">Proyecto Final </p>
<p style="text-align: center;font-weight: bold;font-size: 32px;">Inteligencia Artificial </p>
<p style="text-align: center;font-weight: bold;font-size: 32px;"> DOOM Master </p>




### Introducción 

El proyecto tiene como objetivo comparar distintas tecnicas de Reinforcment Learning para aprender a jugar el videojuego DOOM, con el fin de evaluar la velocidad y eficiencia con la que el agente puede aprender y maximizar su puntaje. Se abordardó el uso de técnicas como Q-Learning y PPO (Proximal Policy Optimization) A2C. AAlgunos de los desafíos encontrados se deben a la complejidad inherente de un videojuego, lo que también complejizó la creación de entornos de juego, compatibles con algoritmos de aprendizaje. Dada esta complejidad y el hecho de que el agente debe tomar decisiones en tiempo real, navegar por el entorno y reconocer objetos, se justifica la aplicación de técnicas de inteligencia artificial para resolver este problema.

Para llevar a cabo este proyecto, se utilizó una biblioteca disponible en GitHub que proporciona entornos virtuales de DOOM. Se combinó con la API de Gymnasium y se emplearon librerías como cv2 para aplicar filtros de color a la imagen. El objetivo principal del proyecto es evaluar la velocidad y eficiencia con la que el agente puede aprender a jugar el juego y alcanzar sus objetivos.

----

### Marco teórico

#### Entornos Virtuales de DOOM

En esta sección, se brindará una descripción teórica general del funcionamiento de los algoritmos de Reinforcement Learning seleccionados: Q-Learning y PPO (Proximal Policy Optimization). Se explicarán sus principales elementos y la razón detrás de la elección de cada algoritmo para abordar el problema planteado.

Para la creación de los entornos virtuales de DOOM se utilizo la libreria "ViZDoom", creada y pensanda para desarrollar agentes de Inteligencia Artificial utilizando unicamente la información visual. Esta libreria contiene entornos de entrenamiento con ciertas pautas, para enseñar al agente distintas cosas en cada uno. 



<u>Los entornos que se utilizaron fueron:</u>

- <p style="font-size: 20px;"><b>Basic: (Entrenamiento)</b></p> Este entorno cuenta con un escenerio cuadrado, con un solo enemigo posicionado de manera aleatoria sobre el entorno, y al agente posicionado en el medio de escenario. La idea de este entorno es enseñar al agente a identificar al enemigo, y dispararle lo mas rapido posible.   
    - En este escenario las posibles acciones son, <u><b>Moverse Izquierda, Moverse Derecha, Disparar. </b></u>
    - Los incentivos en este escenario son:
        - -1.2 por cada accion que realiza el agente, 
        - -5 por cada disparo, 
        - +106 por matar al enemigo. 

    Ademas este escenario fue modificado para cuando el enemigo apareciera muy cercano al centro, el escenario se reiniciara hasta que el enemigo estuviera mas alejado.

    **Esquema del mapa:**

    <p align="center">
  <img src="./pics/basic.png" width="500">
    <p align="center">(El agente en verde, y en el cuadrado rojo el enemigo)</p> 
</p> 

<p style="font-weight: bold">Renderizado del juego:
    <p align="center">
  <img src="./pics/screenBuffer_Basic.png" width="500"></p>
    <p align="center"></p> 
</p> 

<p style="font-weight: bold">Renderizado que se envia al agente:
    <p align="center">
  <img src="./pics/grayBuffer_Basic.png" width="500"></p>
    <p align="center">Se envia como un variable Box de dimensiones (120,160,1) (altura, ancho, canales o dimensiones)</p> 
</p> 

<p style="font-weight: bold">Comparación entre el renderizado del juego y el renederizado que se envia al agente:
    <p align="center">
  <img src="./pics/screenBufferVSgrayBuffer_Basic.png" width="500"></p>
    <p align="center">Se escala la imagen a una resolución mucho menor para que el procesamiento sea mas rapido y facil.</p> 
</p> 

- <p style="font-size: 20px;"><b>Defend the Line: (Entrenamiento)</b></p> Este escenario cuenta con 3 enemigos que se acercan al agente que se encuentra inmovil, cada vez que un enemigo muere, reaparece con mas vida despues de unos segundos. Este entorno tiene como objetivo enseñar al agente a mantenerse vivo lo maximo posible, ya que el agente cuenta con balas infinitas. 
    - Las posibles acciones son, <u><b>Rotar Izquierda, Rotar Derecha, Disparar. </b></u>
    - Los incentivos en este escenario son:
        - -9 por cada disparo que no acierta sonbre un enemigo.
        - +10 por matar a un enemigo.

    Este entorno tambien fue modificado para ajustarse al objetivo de aprendizaje.
    
    **Esquema del mapa:**

<p align="center">
  <img src="./pics/defend_the_line.png" width="500">
    <p align="center">(El agente en verde, y en los cuadrados rojos los enemigos que se acercan al agente)</p> 
</p> 
<p style="font-weight: bold">Renderizado del juego:
    <p align="center">
  <img src="./pics/screenBuffer_Line.png" width="500"></p>
    <p align="center"></p> 
</p> 

<p style="font-weight: bold">Renderizado que se envia al agente:
    <p align="center">
  <img src="./pics/grayBuffer_Line.png" width="500"></p>
    <p align="center">Se envia como un variable Box de dimensiones (120,160,1) (altura, ancho, canales o dimensiones)</p> 
</p> 

<p style="font-weight: bold">Comparación entre el renderizado del juego y el renederizado que se envia al agente:
    <p align="center">
  <img src="./pics/screenBufferVSgrayBuffer_Line.png" width="500"></p>
    <p align="center">Se escala la imagen a una resolución mucho menor para que el procesamiento sea mas rapido y facil.</p> 
</p> 

- <p style="font-size: 20px;"><b>Defend the Center:</b></p> Este escenario cuenta con un entorno circular, donde los enemigos se acercan al agente desde 4 direcciones, de las cuales el agente solo puede ver 1 si se queda quieto. El objetivo de este escenario es evaluar que tan bien ha aprendido el agente en los escenarios anterioires.  
    - Las posibles acciones son, <u><b>Rotar Izquierda, Rotar Derecha, Disparar. </b></u>
    - Los incentivos en este escenario son:
        - +1 por matar a un enemigo. 
        - -1 por morir.

    **Esquema del mapa:**
<p align="center">
  <img src="./pics/defend_the_center.png" width="500">
    <p align="center">(En el centro el agente, y en los cuadrados rojos los enemigos que se    acercan al agente)</p> 
</p>  

<p style="font-weight: bold">Renderizado del juego:
    <p align="center">
  <img src="./pics/screenBuffer_Center.png" width="500"></p>
    <p align="center"></p> 
</p> 

<p style="font-weight: bold">Renderizado que se envia al agente:
    <p align="center">
  <img src="./pics/grayBuffer_Center.png" width="500"></p>
    <p align="center">Se envia como un variable Box de dimensiones (120,160,1) (altura, ancho, canales o dimensiones)</p> 
</p> 

<p style="font-weight: bold">Comparación entre el renderizado del juego y el renederizado que se envia al agente:
    <p align="center">
  <img src="./pics/screenBufferVSgrayBuffer_Center.png" width="500"></p>
    <p align="center">Se escala la imagen a una resolución mucho menor para que el procesamiento sea mas rapido y facil.</p> 
</p> 

#### Algoritmos Utilizados


#### Q-Learning:

Q-Learning es un algoritmo de aprendizaje por refuerzo que se basa en la idea de aprender valores de calidad (Q-values) para cada par estado-acción. La idea fundamental es que el agente toma decisiones óptimas seleccionando la acción con el valor Q más alto para un estado dado. Al principio el algoritmo tiene un gran porcentaje de acciones random, o tambien conocido como etapa de exploración, donde se empieza a armar los Q-values.

La fórmula fundamental para actualizar estos valores \(Q\) se expresa de la siguiente manera:

\[
Q(s, a) \leftarrow (1 - \alpha) \cdot Q(s, a) + \alpha \cdot \left( r + \gamma \cdot \max_{a'} Q(s', a') \right)
\]

Donde:

- \(Q(s, a)\) representa el valor de calidad (Q-value) para el estado \(s\) y la acción \(a\).
- \(\alpha\) es la tasa de aprendizaje que controla la rapidez con la que el agente actualiza sus estimaciones.
- \(r\) es la recompensa obtenida al realizar la acción \(a\) en el estado \(s\).
- \(\gamma\) es el factor de descuento que pondera la importancia de las recompensas futuras.
- \(s'\) es el siguiente estado después de tomar la acción \(a\) en el estado \(s\).
- \(a'\) es la acción óptima en el siguiente estado \(s'\).

La actualización de \(Q(s, a)\) se basa en la diferencia entre la recompensa inmediata (\(r\)) y la recompensa esperada en el próximo estado ponderada por \(\gamma\), que a su vez se maximiza con respecto a todas las posibles acciones \(a'\) en el próximo estado \(s'\). Este proceso de actualización se repite a lo largo de las interacciones del agente con el entorno, permitiéndole mejorar progresivamente sus estimaciones de los valores \(Q\) para tomar decisiones más informadas y maximizar las recompensas esperadas.

En el contexto de DOOM, el agente estaría en un estado particular del juego, representado como array de (160x160x1) height, weigth, channel o dimmension, de la imagen capturada de la pantalla del juego en ese instante. Q-Learning actualizaría los valores Q para cada par estado-acción en función de las recompensas obtenidas al realizar acciones en ese estado.

**Justificación de la Elección:**

Q-Learning es elegido como un algoritmo de referencia para comparación debido a su simplicidad, pero dado que el entorno donde se encuentra es muy complejo se espera que no obtenga muy buenos resultados.

#### PPO (Proximal Policy Optimization)

**Descripción Teórica:**

El algoritmo Proximal Policy Optimization (PPO) es un método de aprendizaje por refuerzo que pertenece a la categoría de algoritmos basados en políticas. Se utiliza para entrenar agentes en entornos de toma de decisiones bajo incertidumbre. Su enfoque radica en mejorar de manera gradual y controlada una política de acción existente.

Una de las características clave de PPO es su estrategia para restringir los cambios entre las políticas antiguas y nuevas, lo que contribuye a garantizar la estabilidad durante el proceso de entrenamiento. Este algoritmo utiliza una versión mejorada de la función objetivo para actualizar la política de manera más segura y eficiente.

En el contexto de DOOM, PPO utiliza redes neuronales convolucionales (CNN) para procesar las imágenes del juego y aprender una política que optimice la secuencia de acciones para maximizar las recompensas.

Las Redes Neuronales Convolucionales (CNN) son un tipo de red neuronal especialmente diseñada para procesar datos con una estructura en forma de cuadrícula, como imágenes. Utilizan capas convolucionales para aprender automáticamente patrones y características en los datos de entrada.

Las capas convolucionales aplican filtros a regiones locales de los datos de entrada para extraer características significativas. Durante el proceso de convolución, los filtros aprenden a reconocer patrones y características simples, como bordes, texturas o formas, en regiones específicas de la entrada. A medida que se agregan más capas convolucionales, la red neuronal puede capturar características más abstractas y complejas.

**Justificación de la Elección:**

PPO es seleccionado por su capacidad para trabajar con espacios de acciones continuos y grandes espacios de observación. A través de su naturaleza de actualización local y su enfoque en la estabilidad, se adapta bien a entornos complejos como DOOM, donde las observaciones son imágenes.

Implementación tomada de la libreria de Stable Baselines 3


#### A2C (Advantage Actor-Critic) o DQN (Deep Q-Network)


---

### Diseño Experimental


1 **las métricas** consideradas a fin de establecer el alcance y rendimiento del algoritmo sobre el problema dado. 

2 **las herramientas utilizadas** para la implementación  como así también para medir el rendimiento del algoritmo. (frameworks, simuladores, etc.). 

3 En aquellos casos en donde resulte adecuado, se deberá indicar todo el proceso realizado para la obtención y adecuación del conjunto de datos.

4 Un **detalle y justificación** de los experimentos realizados a fin de determinar los resultados. Este deberá incluir tablas y/o gráficos que resuman los resultados.

La forma en que se evaluo y analizaron los resultados fueron las siguientes:

Cada algoritmo se corrio por al menos **100.000** iteraciones sobre cada entorno de entrenamiento (basic y defend the line), en el cual se guardo un estado del aprendizaje cada **20.000** iteraciones.
Una vez entrenado cada algoritmo se evaluo su puntaje medio en 30 episodios en los 3 escenarios, en cada etapa (20,40,60,80,100) a fin de evaluar que tan bien aprendio cada algoritmo, alrededor de cuantas iteraciones le tomo aprender lo que se le queria enseñar en el escenario y su resultado sobre el escenario de evaluación.

Las metricas son <u>Promedio de rewards</u> sobre las 30 iteraciones, <u>Desviacion estandar de las rewards</u>, <u>Promedio duracion episodio</u> hasta que se corta, muere o cumple el objetivo, <u>Desviacion estandar duracion episodio</u>


#### Q-Learning

**Basic**
| Iteraciones de entrenamiento | Promedio rewards | Desviacion estandar rewards | Promedio duracion episodio | Desviacion estandar duracion episodio |
|------------------------------|------------------|-----------------------------|---------------------------|---------------------------------------|
| 20k              | -161.27          | 117.33       | 40.0     | 14.29   |
| 40k              | -299.67          | 10.33        | 48.33    | 1.67    |
| 60k              | -179.57          | 155.83       | 36.53    | 18.32   |
| 80k              | -51.79           | 127.36       | 23.9     | 16.76   |
| 100k             | -176.88          | 152.83       | 36.73    | 18.08   |

**Defend the Line**
 Iteraciones de entrenamiento| Promedio rewards | Desviacion estandar rewards | Promedio duracion episodio | Desviacion estandar duracion episodio |
|----------------------------|------------------|-----------------------------|-------------------|---------------------------------------|
|20.000|
|40.000|
|60.000| | | | |
|80.000| |  |  | |
|100.000| |  |  | |
- 20k
- 40k
- 60k
- 80k
- 100k

**Defend the Center**
 Iteraciones de entrenamiento| Promedio rewards | Desviacion estandar rewards | Promedio duracion episodio | Desviacion estandar duracion episodio |
|----------------------------|------------------|-----------------------------|-------------------|---------------------------------------|
|20.000|
|40.000|
|60.000| | | | |
|80.000| |  |  | |
|100.000| |  |  | |
- 20k
- 40k
- 60k
- 80k
- 100k

#### PPO

**Basic**
 Iteraciones de entrenamiento| Promedio rewards | Desviacion estandar rewards | Promedio duracion episodio | Desviacion estandar duracion episodio |
|----------------------------|------------------|-----------------------------|-------------------|---------------------------------------|
|20.000|-164.16| 118.60|158.0| 62.10|
|40.000|33.74|82.46|44.3|43.24|
|60.000|50.07|36.25|36.3|23.67|
|80.000|63.6| 8.47|26.8 |6.3|
|100.000|63.99|11.07 | 27.2|7.79|



**Defend the Line**
| Iteraciones de entrenamiento | Promedio rewards | Desviacion estandar rewards | Promedio duracion episodio | Desviacion estandar duracion episodio |
|------------------------------|------------------|-----------------------------|---------------------------|---------------------------------------|
| 20k                          | 117.36           | 34.34      | 463.53  | 130.40  |
| 40k                          | 281.02           | 59.46      | 997.83  | 239.71  |
| 60k                          | 270.69           | 53.62      | 942.97  | 212.03  |
| 80k                          | 348.68           | 50.58      | 1165.13 | 201.40  |
| 100k                         | 344.68           | 55.47      | 1181.23 | 229.91  |


**Defend the Center**
| Iteraciones de entrenamiento | Promedio rewards | Desviacion estandar rewards | Promedio duracion episodio | Desviacion estandar duracion episodio |
|------------------------------|------------------|-----------------------------|---------------------------|---------------------------------------|
| 20k                          | 4.13             | 3.53          | 272.0   | 120.23  |
| 40k                          | 1.37             | 1.59          | 163.6   | 53.01   |
| 60k                          | 2.27             | 2.37          | 196.7   | 70.79   |
| 80k                          | 3.27             | 2.63          | 228.57  | 83.22   |
| 100k                         | 2.13             | 1.43          | 197.73  | 38.67   |
| 140k                         | 0.63             | 1.09          | 157.6   | 35.30   |



#### Promedio de Rewards con entrenamiento de 100.000 iteraciones
|Algoritmo | Basic | Defend the Line | Defend the Center|
|----------|-------|-----------------|------------------|
|Q-Learning| -176.88  | | |
|PPO       | 63.99 | 344.68 | 2.13|
|A2C o DQN      | | | |

----

### Análisis y discusión de resultados

En esta sección se deberá realizar un mínimo análisis sobre los resultados obtenidos. El objetivo es tratar de razonar sobre las causas de los resultados obtenidos en la fase experimental a fin de proveer una posible justificación. Aquí se incluyen posibles limitaciones en los algoritmos elegidos, en la simulación planteada, los datos, etc.

#### PPO
A partir de los resultados obtenidos en Basic, se puede observar la gran eficiencia de este algoritmo, que en 40.000 iteraciones pudo identificar al enemigo


En base a los resultados obtenidos del algoritmo en el escenario de testeo (Defend the Center), se puede observar que a mayor entrenamiento en Defend the Line, peores resultados obtenia. Esto puede deberse a que en Defend the Line se prioriza apuntar a lo primero que se ve y a lo más cercano. Una vez que ese enemigo muere, pasa al siguiente. En cambio en Defend the Center, los enemigos empiezan muy lejos, lo que dificulta el apuntado, y con 1 solo enemigo en el campo de vision del agente. Además, en el escenario hay enemigos más rápidos que otros, por lo que si el agente se queda apuntando a un enemigo lejano que es más lento, los demás enemigos más rápidos empezarán a dañar al agente. Este comportamiento se ve más pronunciado mientras más se entrenó al agente sobre Defend the Line.

#### Q-Learning
En base a los resultados y a una observación del comportamiento del agente en el escenario Basic, se observó que el algoritmo encontró el rango donde con mas frecuencia se encuentra el enemigo. En la iteracion 100.000 el agente se mueve en un rango de izquierda a derecha bastante amplio pero en ningun caso llega al final del escenario, y dispara mientras se mueve, por lo que podemos deducir que aprendio el rango con mayor probabilidad de aparacion del enemigo, el problema es que al disparar constantemente mientras se mueve pierde mucho puntaje. En conclusion el algoritmo fue incapaz de detectar el enemigo en 100.000 iteraciones.

(Falta entrenamiento sobre Defend the Line y resultados finales)


--- 

### Conclusiones finales

Debido a una falta de tiempo, de conocimientos y de complejidad del proyecto, no se pudo realizar la comparación de algoritmos con y sin Eligibility Traces. La adaptacion de estos algoritmos a un entorno tan comlejo y personalizado se dificultó demasiado. La idea era poder observar si esta caracteristica de actualización de la política es beneficiosa en apliaciones de entrenamiento de agentes para aprender a jugar videojugos o apliaciones similares. 

Algunos experimetos que se podria haber probado, sin mucha modificacion sobre lo ya implemtado son:

Se podria haber experimentado mas con Q-Learning, dando una ventana de exploración mas amplia, y dejandolo correr por mas iteraciones, para observar si el algoritmo es capaz de aprender a identificar al enemigo o no.

Una alternativa sería plantear una modificación sobre el segundo escenario, Defend the Line, para priorizar el apuntado, penalizando más si se falla al disparar, para observar si el comportamiento sobre el ultimo escenario es mejor o no, buscando que priorice enemigos mas cercanos donde el apuntado es más facil.

En conclusion, aunque se podria seguir experimentando, agregando mas algoritmos o realizando modificaciones a los ya implementados, se puede observar una clara ventaja de los algoritmos de Deep Reinforcement Learning como PPO sobre un algoritmo mas simple como Q-Learning. Donde PPO identificó al enemigo de manera muy rapida, alrededor de 40.000 iteraciones, Q-Learning en 100.000 iteraciones no pudo.


Observaciones finales sobre el tema y es muy importante indicar aquellas tareas o experimentos que quedaron sin realizar, pero que eventualmente podrían realizarse en el futuro.

---

### Bibliografía
Incluir la bibliografía utilizada para el trabajo. Es importante referenciar en el cuerpo del trabajo las diferentes fuentes utilizadas.

