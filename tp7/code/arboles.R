suppressMessages(library(rpart))
suppressMessages(library(caret))
suppressMessages(library(readr))
suppressMessages(library(dplyr))
suppressMessages(library(ranger))
#suppressMessages(library(randomForest))
suppressMessages(library(ROSE))

data_train <- readr::read_csv("./data/arbolado-mza-dataset.csv/arbolado-mza-dataset.csv",
                              col_types = cols(
                                id = col_integer(),
                                especie = col_character(),
                                ultima_modificacion = col_character(),
                                altura = col_character(),
                                circ_tronco_cm = col_double(),
                                diametro_tronco = col_character(),
                                long = col_double(),
                                lat = col_double(),
                                seccion = col_integer(),
                                nombre_seccion = col_character(),
                                area_seccion = col_double(),
                                inclinacion_peligrosa = col_integer()
                              ))

data_test <-  readr::read_csv("./data/arbolado-mza-dataset-test.csv/arbolado-mza-dataset-test.csv",col_types = cols(
  id = col_integer(),
  especie = col_character(),
  ultima_modificacion = col_character(),
  altura = col_character(),
  circ_tronco_cm = col_double(),
  diametro_tronco = col_character(),
  long = col_double(),
  lat = col_double(),
  seccion = col_integer(),
  nombre_seccion = col_character(),
  area_seccion = col_double()
))

data_train<-data_train %>% mutate(inclinacion_peligrosa=ifelse(inclinacion_peligrosa=='1','si','no'))
data_train$inclinacion_peligrosa <-as.factor(data_train$inclinacion_peligrosa)

#Eliminamos columnas
data_train <- subset(data_train, select = -c(ultima_modificacion, id))
dim(data_train)

set.seed(123)  # Establecer una semilla para reproducibilidad
indices <- sample(1:nrow(data_train), 0.35 * nrow(data_train))  # 35% para entrenamiento, en vez de hacer undersampling
train_dataNew <- data_train[indices, ]
test_dataNew <- data_train[-indices, ]

dim(train_dataNew)

# Entrenar el modelo de Random Forest
formula <- inclinacion_peligrosa ~ circ_tronco_cm + lat + long + altura + especie + seccion + diametro_tronco + area_seccion
rf_model <- ranger( formula = formula, data = train_dataNew, num.trees = 600, mtry = 3, local.importance = TRUE, probability = TRUE)

# Hacer predicciones con el modelo entrenado
predictions <- predict(rf_model, data = test_dataNew)$predictions
head(predictions)

# Calcular la precisión del modelo
accuracy <- mean(predictions == test_dataNew$inclinacion_peligrosa)
print(paste("Precisión del modelo:", accuracy))


# --------------------------------- Probar sobre test cheto ---------------- #


predictions <- predict(rf_model, data = data_test)$predictions
head(predictions)
submission<-data.frame(id=data_test$id,inclinacion_peligrosa=predictions[,"si"])
head(submission)
readr::write_csv(submission,"./arbolado-mza-dataset-envio-ejemplo-rforest15.csv")
head(submission)


