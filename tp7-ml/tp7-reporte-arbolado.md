# Parte B
## Descripción del proceso de preprocesamiento:

Al ```data_train``` se le elimino las variables de **ID** y **Ultima Modificación**, despues se separo ```data_train``` en 2 ```train_dataNew``` con el 35% de los datos y ```test_dataNew``` con el 65% restante. 
Se ultilizo la siguiente formula:
```R
formula <- inclinacion_peligrosa ~ circ_tronco_cm + lat + long + altura + especie + seccion + diametro_tronco + area_seccion
rf_model <- ranger( formula = formula, data = train_dataNew, num.trees = 600, mtry = 3, local.importance = TRUE, probability = TRUE)
#Se opto por usar ranger ya que es una implemetación de Random Forest multihilo, lo que permitio pasar de 3 horas y 11.5GB de ram ocupados con la libreria randomForest, a 1 segundo con Ranger.
```
Despues con ```R predictions <- predict(rf_model, data = test_dataNew)$predictions``` se obtuvo una prediccion sobre los datos de testeo y se midio la accuracy = **0.8867**.
```R
accuracy <- mean(predictions == test_dataNew$inclinacion_peligrosa)
print(paste("Precisión del modelo:", accuracy))
```
Se probo el modelo sobre ```data_test``` y como los datos de prediccion estaban de la siguiente manera:
|    |no        | si        |
|----|----------|-----------|
|[1,]| 0.9232309| 0.07676906|
|[2,]| 0.9032104| 0.09678956|
|[3,]| 0.9809746| 0.01902540|
|[4,]| 0.9618990| 0.03810098|

Solo se tomó el valor de si, que indica la pertenencia a Inclinación Peligrosa, teniendo como resultado algo así:

|id | inclinacion_peligrosa |
|---|-----------------------|
|  1|            0.07676906 |
|  2|            0.09678956 |
|  4|            0.01902540 |
|  6|            0.03810098 |
|  9|            0.03444418 | 
| 13|            0.03039408 |

Obteniendo un Resuldato en Kaggle de: **0.74727**
