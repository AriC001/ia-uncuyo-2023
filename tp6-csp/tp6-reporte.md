## 1. Describir en detalle una formulación CSP para el Sudoku.

Componentes de un CSP:
 - X conjunto de variables {X1,X2,...,Xn} 
 - D conjunto de dominios {D1,...,Dn}
 - C conjunto de restricciones que especifican las combinaciones permitidas de valores

Cada dominio Di consiste en un conjunto de valores permitidos {v1,...,vk} para la variable Xi.
Cada restricción Ci consiste en un par <scope, rel>, donde *scope* es una tupla de variables que participan en la restriccion y *rel* es una relacion que define los valores que pueden tomar esas variables.

En el Sudoku tenemos un tablero de 9x9 el cual esta dividido en 9 cuadrados de 3x3.
 - X = {X11, X12,...,X99} ``` # X11 significa que esa varible tomara la posición en la fila 1 columna 1 ```
 - D = {D11,D12,...,D99}
 - C = {C1,...,C27}
    - 9 filas con restricciones de tipo ```< (Xi1,Xi2,Xi3,Xi4,Xi5,Xi6,Xi7,Xi8,Xi9), Xi1 != Xi2 != Xi3 .... != Xi9 >```
    - 9 columnas con restricciones de tipo ```< (X1i,X2i,X3i,X4i,X5i,X6i,X7i,X8i,X9i), X1i != X2i != X3i .... != X9i >```
    - 9 cuadrados de 3x3 con restricciones de tipo ``` < (X11,X12,X13,X21,X22,X23,X31,X32,X33) X11 != X12 != X13 != X21 != ... != X33 > (Xij con i=[(1,2,3),(4,5,6),(7,8,9)] Y j=[(1,2,3),(4,5,6),(7,8,9)])```


## 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).


!["Australia map"](./pics/Australia%20map.png)

- Variables: {WA, NT, Q, NSW, V, SA, T}

- Dominios:
    - WA = {red}
    - NT = {red, green, blue}
    - Q = {red, green, blue}
    - NSW = {red, green, blue}
    - V = {blue}
    - SA = {red, green, blue}
    - T = {red, green, blue}

- Restricciones: Dos estados adyacentes no pueden tener el mismo color.

### Primera iteración:
Se toma la cola de restricciones y se observa (WA,SA)
- Dominios:
    - WA = {red}
    - NT = {red, green, blue}
    - Q = {red, green, blue}
    - NSW = {red, green, blue}
    - V = {blue}
    - SA = { green, blue}
    - T = {red, green, blue}

### Segunda iteración:
Se toma la cola de restricciones y se observa (WA,NT)
- Dominios:
    - WA = {red}
    - NT = {green, blue}
    - Q = {red, green, blue}
    - NSW = {red, green, blue}
    - V = {blue}
    - SA = { green, blue}
    - T = {red, green, blue}

### Tercera iteración:
Se toma la cola de restricciones y se observa (V,SA)
- Dominios:
    - WA = {red}
    - NT = {green, blue}
    - Q = {red, green, blue}
    - NSW = {red, green, blue}
    - V = {blue}
    - SA = { green}
    - T = {red, green, blue}

## Cuarta Iteración
Se toma la cola de restricciones y se observa (V,NSW)
- Dominios:
    - WA = {red}
    - NT = {green, blue}
    - Q = {red, green, blue}
    - NSW = {red, green}
    - V = {blue}
    - SA = {green}
    - T = {red, green, blue}

## Quinta Iteración
Se toma la cola de restricciones y se observa (SA,NT)
- Dominios:
    - WA = {red}
    - NT = {blue}
    - Q = {red, green, blue}
    - NSW = {red, green}
    - V = {blue}
    - SA = {green}
    - T = {red, green, blue}

## Sexta Iteración
Se toma la cola de restricciones y se observa (NT,Q)
- Dominios:
    - WA = {red}
    - NT = {blue}
    - Q = {red, green}
    - NSW = {red, green}
    - V = {blue}
    - SA = {green}
    - T = {red, green, blue}

## Septima Iteración
Se toma la cola de restricciones y se observa (SA,Q)
- Dominios:
    - WA = {red}
    - NT = {blue}
    - Q = {red}
    - NSW = {red, green}
    - V = {blue}
    - SA = {green}
    - T = {red, green, blue}

## Octava Iteración
Se toma la cola de restricciones y se observa (Q,NSW)
- Dominios:
    - WA = {red}
    - NT = {blue}
    - Q = {red}
    - NSW = {green}
    - V = {blue}
    - SA = {green}
    - T = {red, green, blue}

## Novena Iteración
Se toma la cola de restricciones y se observa (SA,NSW)
- Dominios:
    - WA = {red}
    - NT = {blue}
    - Q = {red}
    - NSW = {}
    - V = {blue}
    - SA = {green}
    - T = {red, green, blue}

Aca se puede observar como NSW se queda sin posibles valores. Por ende la asignación parcial {WA=red, V=blue} no es consistente.

## 3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

Cada Variable esta relacionada con cada otra variable por a lo sumo 1 camino, es decir que todas las variables estan interconectadas. Por ende habra que recorrer el arbol en toda su extension en cada iteracion que se asigne un valor a una varible (nodo) del arbol. Ya que si asignamos un valor a una variable verificamos las restricciones a nodos adyacentes, actualizamos sus dominios, ahi verificamos que en caso de quedar un unico valor en sus dominios debemos actualizar los nodos adyacentes a ese y asi sucesivamente. Por lo que el pero caso seria de que a cada iteración donde asiganmos un valor tengamos que actualizar todos los nodos del grafo y a eso multiplicarlo por la cantidad de valores posibles en cada variable = O(n*d^2)
- n = cantidad de nodos
- d = dominios de cada variable


## 4. AC-3 coloca de nuevo en la cola todo arco ( Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por  cada arco ( Xk,Xi)  se puede llevar la cuenta del número de valores restantes de Xi que sean consistentes con cada valor de Xk . Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n2d2 )

Se puede utilizar una matriz donde las filas representaran los valores de Xk (Dominio de Xk) y las columnas el Dominio de Xi.

Entonces cuando eliminamos un valor Z de Xi actualizamos la matriz en la columna que representa el valor Z de Xi observamos que valores de Xk eran consistentes y se eliminan del Dominio de Xk. Asi mantenemos los valores del arco (Xk,Xi) posibles que sean consistentes.

En el peor de los casos se debera iterar sobre cada par de posibles variables (n^2) y cada valor posible de sus dominios (d^2), por lo que tenemos una complejidad de O(n^2 d^2)


## 5. Demostrar la correctitud del algoritmo CSP para  árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar: 
 - Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)
 - Argumentar por qué lo demostrado en a. es suficiente. 

Supongamos que tenemos un CSP donde su grafo de restricciones se puede representar como un árbol y tenemos una 2-consistencia. Que significa que para cada par de variables (Xi,Xj), donde Xi es adyacente a Xj, todos los valores del Dominio de Xi son consistentes con al menos 1 valor del Dominio de Xj. Esta consistencia se extiende a cada par de variables en el camino.
Por lo tanto cada variable termina siendo consistente con cada variable del arbol/grafo, por lo que obtenemos una n-consistencia.

Es suficiente, ya que cada variable esta interconectada por un camino a las demas variables, y que esta garantizado la 2-consistencia de cada par, por lo que terminamos obteniendo que cada variable sea consistente con cada variable.

## Ejercicio 6: 
#### Implementar una solución al problema de las n-reinas utilizando una formulación CSP. 
A. Implementar una solución utilizando backtracking.
B. Implementar una solución utilizando encadenamiento hacia adelante.
C. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas. 
D. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8, 10, 12 y 15 reinas. 
E. Realizar un gráfico de cajas para los puntos C y D.

| Tamaño | Algoritmo       | Sol Found | AVG Time    | STD Time    | AVG States | STD States |
|--------|-----------------|-----------|-------------|-------------|------------|------------|
| 4      | Backtracking    | 60        | 0.0001668   | 0.0049344   | 62.0       | 35.2136    |
| 4      | Forward Checking| 60        | 0.0005338   | 0.0157529   | 62.0       | 35.2136    |
| 8      | Backtracking    | 2760      | 0.0674277   | 1.9888389   | 124.0      | 70.4273    |
| 8      | Forward Checking| 50        | 0.0021687   | 0.0639767   | 230.9333   | 121.7388   |
| 10     | Backtracking    | 21720     | 1.4737879   | 43.4705     | 155.0      | 88.0341    |
| 10     | Forward Checking| 36        | 0.0060386   | 0.1781     | 365.0      | 213.0849   |
| 12     | Backtracking    | 426000    | 43.6867254  | 1288.5733   | 186.0      | 105.6409   |
| 12     | Forward Checking| 38        | 0.0108429   | 0.3199     | 482.0      | 237.9029   |


1. **Soluciones Encontradas:** Los algoritmos Backtracking encuentran significativamente más soluciones en todos los casos en comparación con Forward Checking.

2. **Tiempo Promedio (AVG Time):** Backtracking tiende a ser más lento que Forward Checking en todos los tamaños. La diferencia en el tiempo promedio es más notable a medida que aumenta el tamaño del problema.

3. **Estados Promedio (AVG States) y Desviación Estándar de Estados (STD States):** En la mayoría de los casos, Backtracking requiere menos estados para encontrar soluciones y tiene una menor variabilidad en comparación con Forward Checking.

En resumen, Backtracking encuentra más soluciones, pero para problemas grandes se puede volver muy lento para encontrar todas las soluciones, una alternativa seria una vez encontrado un resultado terminar la ejecución.


### C - Tiempos de Ejecución

**Tabla de Comparación de Tiempos de Ejecución:**

| Tamaño | Backtracking (AVG Time) | Forward Checking (AVG Time) |
|--------|-------------------------|-----------------------------|
| 4      | 0.0001668               | 0.0005338                   |
| 8      | 0.0674277               | 0.0021687                   |
| 10     | 1.4737879               | 0.0060386                   |
| 12     | 43.6867254              | 0.0108429                   |

![Back_Times.png.png](./pics/Back_Times.png)
![Forw_Times.png.png](./pics/Forw_Times.png)
**Para Tamaño 10:**
![time_10.png](./pics/time_10.png)

**Para Tamaño 12:**
![time_12.png](./pics/time_12.png)

### D - Estados Recorridos

**Tabla de Comparación de Cantidad de Estados Recorridos:**

| Tamaño | Backtracking (AVG States) | Forward Checking (AVG States) |
|--------|---------------------------|-------------------------------|
| 4      | 62.0                      | 62.0                          |
| 8      | 124.0                     | 230.9333                      |
| 10     | 155.0                     | 365.0                         |
| 12     | 186.0                     | 482.0                         |


![Back_States.png.png](./pics/Back_States.png)
![Forw_States.png.png](./pics/Forw_States.png)