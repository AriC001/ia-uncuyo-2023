# Parte A
## 7



El código (en un bloque de código) de las funciones create_folds() y cross_validation()
```R

create_folds <- function(dataframe, num_folds) {
  indices <- createDataPartition(y = 1:nrow(dataframe), times = num_folds, list = TRUE)
  return(indices)
}
```
---
Una tabla con los resultados (media y desviación estándar de las métricas seleccionadas) de aplicar el clasificador un árbol de decisión en los distintos conjuntos
```R
cross_validation <- function(dataframe, num_folds) {
  # Crear los folds
  folds <- createFolds(dataframe$inclinacion_peligrosa, k = num_folds, returnTrain = TRUE)
  
  # Función para calcular las métricas
  calculate_metrics <- function(train_indices, test_indices) {
    # Datos de entrenamiento y test para este fold
    train_data <- dataframe[train_indices, ]
    test_data <- dataframe[test_indices, ]
    
    # Entrenar el modelo de árbol de decisión
    model <- rpart(inclinacion_peligrosa ~ ., data = train_data)
    
    # Predecir con el modelo en datos de test
    predictions <- predict(model, test_data, type = "class")
    
    # Calcular las métricas
    confusion_matrix <- confusionMatrix(predictions, test_data$inclinacion_peligrosa)
    metrics <- c(
      accuracy = confusion_matrix$overall["Accuracy"],
      precision = confusion_matrix$byClass["Precision"],
      sensitivity = confusion_matrix$byClass["Sensitivity"],
      specificity = confusion_matrix$byClass["Specificity"]
    )
    
    return(metrics)
  }
  
  # Aplicar la función para cada fold y guardar las métricas
  metrics_list <- map(folds, ~ calculate_metrics(train_indices = .x, test_indices = setdiff(seq_len(nrow(dataframe)), .x)))
  
  # Calcular la media y desviación estándar de las métricas
  metrics_mean <- colMeans(do.call(rbind, metrics_list))
  metrics_sd <- apply(do.call(rbind, metrics_list), 2, sd)
  
  # Devolver media y desviación estándar de las métricas
  return(list(mean = metrics_mean, sd = metrics_sd))
} 
```
---

Mean
|Accuracy |  Precision | Sensitivity | Specificity |
|---------|-----------|----------|-----------|
|  0.8873747 |  0.8873747 |  1.0000000  | 0.0000000| 

SD
|   Accuracy |  Precision| Sensitivity |Specificity |
|----------|-------------|------------|--------------|
|0.004733353 |0.004733353 |0.000000000 |0.000000000 |