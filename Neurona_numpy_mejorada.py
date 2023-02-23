# Neurona_numpy_mejorada.py
# El método train debería incluir una condición de parada, de lo contrario, podría seguir entrenando indefinidamente. Por ejemplo, podría incluir un umbral de error, donde si el error es menor que el umbral, se detiene el entrenamiento.
# El método think podría aceptar varias entradas a la vez, en lugar de solo una. Esto sería más útil en situaciones reales donde se pueden recibir múltiples entradas simultáneamente.
# En lugar de tener una clase separada NeuralNetwork, se podría crear una función que tome los parámetros necesarios y devuelva los resultados. Esto hace que el código sea más simple y fácil de entender.
# La impresión de los resultados debería ser más clara, para que el usuario entienda fácilmente lo que está sucediendo. Por ejemplo, podría imprimirse la precisión de la red neuronal en la etapa de prueba.
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def train_neural_network(inputs, outputs, iterations=10000, learning_rate=0.1, error_threshold=0.01):
    np.random.seed(1)
    weights = 2 * np.random.random((inputs.shape[1], 1)) - 1
    print("Random starting synaptic weights: ", weights)
    for iteration in range(iterations):

        output = sigmoid(np.dot(inputs, weights))
        error = outputs - output
        print("Iteración", iteration, " Error: ", error)
        if np.mean(np.abs(error)) < error_threshold:
            break

        adjustment = learning_rate * \
            np.dot(inputs.T, error * sigmoid_derivative(output))
        weights += adjustment

    return weights


if __name__ == "__main__":
    # los arreglos inputs y outputs son los datos de entrenamiento que se utilizarán para entrenar la red neuronal. inputs es una matriz de 4 filas y 3 columnas, donde cada fila representa una entrada y cada columna representa una característica de la entrada. outputs es una matriz de 4 filas y 1 columna, donde cada fila representa la salida correspondiente para la entrada correspondiente en inputs.
    inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    outputs = np.array([[0, 1, 1, 0]]).T

    weights = train_neural_network(inputs, outputs)

    print("Trained synaptic weights: ")
    print(weights)

    test_input = np.array([[1, 0, 0]])
    test_output = sigmoid(np.dot(test_input, weights))[0][0]
    print(f"Test output for input {test_input}: {test_output}")
