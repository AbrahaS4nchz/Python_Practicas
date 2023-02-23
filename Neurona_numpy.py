# Neurona.py
# Librería que importa funciones para operar con matrices y vectores.
import numpy as np
# Entradas del conjunto de entrenamiento para la Red Neuronal
training_set_inputs = np.array([[1, 0, 1], [1, 0, 1], [1, 1, 1], [1, 1, 0]])
# Salidas del conjunto de entrenamiento para la Red Neuronal.
training_set_outputs = np.array([[0, 1, 1, 0]]).T


class NeuralNetwork():
    def __init__(self):
        # Generador de números aleatorios, con la misma raiz para generar siempre los mismos.
        np.random.seed(1)
        # le damos pesos aleatorios entre -1 y 1 a las diferentes entradas, como tenemos tres entradas y una neurona, sera una matriz 3x1
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    # Defino la funcion sigmoid en forma de S y dado x que me devuelva f(x). Se pasan la sumaponderada de las entradas a través de esta función para normalizarlos entre 0 y 1.
    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # La derivada de la función Sigmoid, el gradiente, que indica la confianza que tenemos en el paso siquiente
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Pasa las entradas a través de nuestra red neuronal (una neurona), multiplicando inputs por sus pesos.
    def think(self, inputs):
        return self.__sigmoid(np.dot(inputs, self.synaptic_weights))
        # Entrenamos a la red neuronal a través de un proceso de prueba y error
        # Se realiza un ajuste de los pesos sinápticos cada vez.

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        # Tantas iteraciones como se quiera con cuidado de no sobrentrenar.
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)
            # Calcular el error entre lo real y lo esperado. Función pérdida.
            error = training_set_outputs - output

        # Multiplica el error por la entrada y nuevamente por el gradiente de la curva Sigmoid
        # Esto significa que los pesos menos confiables se están ajustando más
        # Esto significa que las entradas que son cero, no causan cambios en los pesos.
        adjustment = np.dot(training_set_inputs.T, error *
                            self.__sigmoid_derivative(output))
        # Ajuste de los pesos
        self.synaptic_weights += adjustment

if __name__ == "__main__":  # llamada para inicializar el propio programa
    # Iniciar una red neuronal de una neurona
    neural_network = NeuralNetwork()
    print("Random starting synaptic weights: ")
    print(neural_network.synaptic_weights)
    # El conjunto de pruebas. Tenemos cuatro ejemplos, cada uno consiste en 3 valores de entrada
    # y un valor de salida.
    training_set_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = np.array([[0, 1, 1, 0]]).T
    # Entrenar la red neuronal utilizando el conjunto de entrenamiento.
    # Realizar 10000 veces y realizar un ajuste más pequeño cada vez.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)
    print("New synaptic weights after training: ")
    print(neural_network.synaptic_weights)
    # Prueba la red neuronal con una nueva situación
    print("Considering new situation [1, 0, 0] -> ?: ")
    print(neural_network.think(np.array([1, 0, 0])))
