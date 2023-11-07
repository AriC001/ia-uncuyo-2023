# Inteligencia Artificial aprende a jugar DOOM

# DOOM-Master

## Descripción: 

El proyecto tiene como objetivo diseñar un agente de inteligencia artificial (IA) capaz de aprender a jugar el videojuego DOOM utilizando técnicas de aprendizaje por refuerzo (Reinforcement Learning) y Eligibility Traces. Se utilizará una biblioteca de GitHub que proporciona entornos virtuales de DOOM, junto con la API de Gymnasium para aplicar filtros al entorno y así poder realizar la detección de objetos, como enemigos y paredes. El proyecto busca evaluar qué tan rápido y eficientemente el agente puede aprender a jugar el juego y lograr sus objetivos.

### Objetivos:

- Diseñar un agente de IA capaz de aprender a jugar DOOM utilizando Reinforcement Learning con y sin Eligibility Traces.
- Evaluar el rendimiento del agente en términos de tiempo de ejecución, la cantidad de veces que llega a un estado objetivo, la tasa de observaciones correctamente detectadas, entre otros.
- Validar la eficacia de la combinación de Reinforcement Learning y Eligibility Traces para mejorar el rendimiento del agente en un entorno de juego complejo como DOOM.

### Justificación: 
- Complejidad del problema: DOOM es un videojuego con un entorno virtual complejo y dinámico que presenta desafíos significativos para el aprendizaje de agentes. La toma de decisiones en tiempo real, la navegación, la detección de objetos y la interacción con el entorno requieren un enfoque avanzado.

- Eficiencia computacional: Los algoritmos de Deep RL, aunque poderosos, a menudo requieren una gran capacidad de procesamiento y recursos de hardware, como GPUs o TPUs, para un entrenamiento eficiente. En comparación, el uso de RL con Eligibility Traces suele ser más eficiente en términos de recursos computacionales, lo que lo hace más adecuado para máquinas de hogar con recursos limitados.

- Implementación más sencilla: Los algoritmos de RL con Eligibility Traces tienden a ser más simples de implementar en comparación con los complejos modelos de redes neuronales utilizados en Deep RL. Esto hace que la implementación sea más accesible y práctica.

### Alcance:
El proyecto se enfoca en el desarrollo de un agente de IA para jugar el videojuego DOOM utilizando las técnicas mencionadas. El alcance incluye la implementación de los algoritmos de Reinforcement Learning con y sin Eligibility Traces, así como la integración de la API de Gymnasium para la detección de objetos. Se llevarán a cabo experimentos para validar el rendimiento del agente y se analizarán los resultados.

### Limitaciones:

El proyecto se limita a la utilización de entornos virtuales de DOOM y no aborda otros videojuegos.
La evaluación del agente se centrará en métricas relacionadas con su rendimiento en DOOM y no se extenderá a aplicaciones en otros dominios.
Las actividades propuestas pueden estar sujetas a modificaciones y mejoras a medida que avance el proyecto.

### Forma de Evaluación (Métricas de Resultados):
##### Se evaluará el proyecto en función de las siguientes métricas:

- Tiempo de ejecución: Se medirá el tiempo que el agente necesita para aprender a jugar DOOM de manera efectiva.
- Cantidad de veces que llega a un estado objetivo: Se registrará la frecuencia con la que el agente alcanza los objetivos deseados en el juego.

- Rendimiento en términos de puntajes o logros dentro del juego: Se medirá el éxito del agente en comparación con otros métodos o agentes.

#### Actividades a Realizar:

Act 1. Recopilación de bibliografía y/o ejemplos del problema a resolver. [5 días]
Act 2. Puesta a punto de los entornos virtuales de DOOM con control del jugador de manera random. [2 días]
Act 3. Puesta a punto del código fuente para IA de RL. [4 días]
Act 4. Implementar la API de Gymnasium para poder aplicar herramientas de detección de objetos, con filtros en la imagen. [3 días]
Act 5. Implementar el código para detección de objetos (enemigos, paredes). [5 días]
Act 6. Implementación de Reinforcement Learning sin Eligibility Traces. [7 días]
Act 7. Implementación de Reinforcement Learning con Eligibility Traces. [5 días]
Act 8. Ejecución de los experimentos a fin de validar el objetivo y obtener resultados. [4 días]
Act 9. Análisis de los resultados. [4 días]
Act 10. Escritura de informe final. [5 días]
