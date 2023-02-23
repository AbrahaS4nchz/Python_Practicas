#Neurona_Keras.py
# se importan las neuronas numpy, keras, sequential y dense
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Datos de entrada y salida se definen:
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([0, 0, 0, 1])

# Definir la arquitectura de la red neuronal modelo secuencial
model = Sequential()
# se agrega una capa densa con una sola neurona ocupa la funcion de ativacion sigmoidal.
model.add(Dense(1, input_dim=2, activation='sigmoid'))

# Compilar la red neuronal
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar la red neuronal
model.fit(inputs, outputs, epochs=1000, batch_size=1)

# Probar la red neuronal
predictions = model.predict(inputs)
print(predictions)
