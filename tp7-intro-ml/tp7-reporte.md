2.4 Exercises

### 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

- #### (a) The sample size n is extremely large, and the number of predictors p is small.
En este caso nos conviene mas un metodo **flexible**, ya que puede capturar la complejidad de la verdadera relación entre los predictores.

- #### (b) The number of predictors p is extremely large, and the number of observations n is small.
En este caso nos conviene mas un modelo mas **inflexible** ya que la interpretación de los 
predictores sera mucho mas simple de entender.

- #### (c) The relationship between the predictors and response is highly non-linear.
Un modelo mas **flexible** nos podria dar una mejor estimacion de la relacion entre predictores y respuestas

- #### (d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.
Un modelo **inflexible** seria mejor, ya que uno flexible podria hacer overfitting agregando errores y ruido.

### 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.
Quantitativos: varibles numericas (regresion)
Qualitativos: categoricos (clasification)
- (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors affect CEO salary.
**Regresión**
Interes: **Inferencia**

n = 500
p = 4

- (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.
**Clasificación**
Interes: **Predicción**

n = 20
p = 14

- (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.
**Regresión**
Interes: **Predicción**

n = 52
p = 4

### 5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

**Ventajas de un enfoque altamente flexible:**
- Mayor capacidad para capturar patrones complejos: Los modelos altamente flexibles pueden adaptarse a relaciones no lineales o complicadas en los datos. Pueden ajustarse mejor a conjuntos de datos con estructuras complejas y no lineales.

- Ajuste más preciso: En situaciones donde los datos tienen una relación intrincada y complicada, los modelos más flexibles pueden proporcionar predicciones más precisas y ajustarse mejor a los datos de entrenamiento.

- Menor sesgo: Los modelos más flexibles tienden a tener un sesgo más bajo, lo que significa que se ajustan más a los datos, especialmente cuando la verdadera relación entre las características y la variable objetivo es complicada y no lineal.

Un enfoque mas **flexible** podria preferirse en situaciones donde tenemos conjuntos de datos mas complejos, y donde se trata de buscar una presicion mas alta (sin caer en overfitting)

Un enfoque **menos flexible** podría preferirse en situaciones donde el conjuntos de datos es pequeños, ya que los modelos más flexibles pueden sobreajustarse fácilmente. En tales casos, modelos menos flexibles con menor capacidad para sobreajustar podrían ser más adecuados. Y cuando la interpretación es importante o tan importante como la precision.

### 6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or  classification (as opposed to a nonparametric approach)? What are its disadvantages?

Los métodos paramétricos implican un enfoque de dos pasos basado en el modelo. Primero, hacemos una suposición sobre la forma funcional, o estructura, de *f*. Después de seleccionar un modelo, necesitamos un procedimiento que utilice los datos de entrenamiento para ajustar o entrenar el modelo.

Reduce el problema de estimar *f* a uno de estimar un conjunto de parámetros. Suponer una forma paramétrica para *f* simplifica el problema de estimar *f* porque generalmente es mucho más fácil estimar un conjunto de parámetros en el modelo lineal, que ajustar una función completamente arbitraria *f*. Si el modelo elegido está muy alejado del verdadero *f*, entonces nuestra estimación será deficiente.

**Desventaja** de un enfoque paramétrico es que el modelo que elegimos generalmente no coincidirá con la verdadera forma desconocida de *f*.

----
Los métodos no paramétricos no hacen suposiciones explícitas sobre la forma funcional de *f*. En su lugar, buscan una estimación de *f* que se acerque lo más posible a los puntos de datos sin ser demasiado áspera o zigzagueante.

Al evitar la suposición de una forma funcional particular para *f*, tienen el potencial de ajustar con precisión una gama más amplia de formas posibles para *f*..

**Desventaja:** dado que no reducen el problema de estimar *f* a un número pequeño de parámetros, se requiere un número muy grande de observaciones (mucho más de lo que normalmente se necesita para un enfoque paramétrico) para obtener una estimación precisa de *f*.

### 7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

| Obs | X1 | X2 | X3 | Y|
|-----|----|----|----|--|
|1    |0   |3   |0   |Red|
|2    |2   |0   |0   |Red|
|3    |0   |1   |3   |Red|
|4    |0   |1   |2   |Gren|
|5    |-1  |0   |1   |Gren|
|6    |1   |1   |1   |Red|

Suppose we wish to use this data set to make a prediction for Y when 
X1 = X2 = X3 = 0 using K-nearest neighbors.
- (a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.

| Obs. | X1 | X2 | X3 | d(x, x0)            |
|------|----|----|----|---------------------|
| 1    | 0  | 3  | 0  | 3                   |
| 2    | 2  | 0  | 0  | 2                   |
| 3    | 0  | 1  | 3  | $\sqrt{10} = 3.162$ |
| 4    | 0  | 1  | 2  | $\sqrt{5} = 2.236$  |
| 5    | -1 | 0  | 1  | $\sqrt{2} = 1.414$  |
| 6    | 1  | 1  | 1  | $\sqrt{3} = 1.732$  |


- (b) What is our prediction with K = 1? Why?
La predicción con K = 1 es **Green**, ya que la *observación 5* tiene la distacia mas cercana y tiene el valor de la respuesta **Green**.

- (c) What is our prediction with K = 3? Why?
La predicción con K = 3 es **Red**, ya que las *observación 2,5,6* tiene la distacia mas cercana y tiene el valor de la respuesta **Red,Green,Red** respectivamente, porque lo que se elige **Red** por tener mayor presencia.

- (d) If the Bayes decision boundary in this problem is highly nonlinear, then would we expect the best value for K to be large or small? Why?

Si la frontera de decisión de Bayes es altamente no lineal, se espera que un valor óptimo para K sea pequeño. Ya que permitiran capturar mejor la complejidad y la relacion de los datos. Adapta mejor el modelo.

Si tenemos un K grande, habria que considerar mas vecinos, suavizaria la frontera de decision y no se podria ajustar bien a la verdader forma.
