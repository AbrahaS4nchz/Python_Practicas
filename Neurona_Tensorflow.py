import tensorflow as tf

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
optimizer = tf.optimizers.SGD(learning_rate=0.5)
#train_step = optimizer.minimize(loss, var_list=[pesos, bias])

# Creamos una sesión de TensorFlow y ejecutamos el entrenamiento
#with tf.Session() as sess:
with tf.compat.v1.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Realizamos 100 iteraciones de entrenamiento
    for i in range(100):
        #_, loss_value, output_value = sess.run([train_step, loss, salida_calculada])
        # se agrego a "tf.compat.v1.get_default_session().run()" para ejecutar en cada interacion del bucle
        #_, loss_value, output_value = tf.compat.v1.get_default_session().run([train_step, loss, salida_calculada])
        with tf.GradientTape() as tape:
            # calculamos la función de pérdida
            loss_value = tf.reduce_mean(tf.square(salida_calculada - salida_esperada))

        # Obtenemos los gradientes de la función de pérdida con respecto a los pesos y el bias
        grads = tape.gradient(loss_value, [pesos, bias])

        # Actualizamos los pesos y el bias utilizando el optimizador y los gradientes
        optimizer.apply_gradients(zip(grads, [pesos, bias]))

        # Obtenemos la salida de la neurona
        output_value = sess.run(salida_calculada)

        # Imprimimos el error y la salida de la neurona en cada iteración
        print("Iteración ", i, " Error: ", loss_value, " Salida: ", output_value)
