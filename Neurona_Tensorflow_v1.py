import tensorflow.compat.v1 as tf

tf.disable_eager_execution()

# Definimos las entradas y las salidas esperadas de la neurona
entradas = tf.constant([[0.1, 0.2, 0.3]])
salida_esperada = tf.constant([[0.4]])

# Definimos los pesos y el bias de la neurona
pesos = tf.Variable([[0.1], [0.2], [0.3]])
bias = tf.Variable([0.4])

# Definimos la operación que realizará la neurona
salida_calculada = tf.matmul(entradas, pesos) + bias

# Definimos la función de pérdida (en este caso, el error cuadrático medio)
loss = tf.reduce_mean(tf.square(salida_calculada - salida_esperada))

# Definimos el optimizador que actualizará los pesos y el bias de la neurona
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)
train_step = optimizer.minimize(loss, var_list=[pesos, bias])

# Creamos una sesión de TensorFlow y ejecutamos el entrenamiento
sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer())
sess.run(tf.compat.v1.variables_initializer(optimizer.variables()))

# Realizamos 100 iteraciones de entrenamiento
for i in range(100):
    _, loss_value, output_value = sess.run([train_step, loss, salida_calculada])

    # Imprimimos el error y la salida de la neurona en cada iteración
    print("Iteración ", i, " Error: ", loss_value, " Salida: ", output_value)
