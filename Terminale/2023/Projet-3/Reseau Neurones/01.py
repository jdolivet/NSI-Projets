import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.preprocessing import image
import numpy as np

nb_generations = 5

# On charge les données de MNIST, qui est une base de données de chiffres écrits à la main.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# On met les valeurs des pixels dans l'intervalle [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# On construit le reseau
reseau = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])
reseau.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# On entraine le reseau
reseau.fit(x_train, y_train, epochs=nb_generations)

# On donne une note au réseau
reseau.evaluate(x_test,  y_test, verbose=2)

# On charge l'image puis les manipulations nécessaires
img = image.load_img(f"images/7.png", color_mode = "grayscale", target_size=(28, 28))
img = image.img_to_array(img)
img = 255 - img
img /= 255.0
img = np.expand_dims(img, axis=0)

# On donne le résultat de l'image
predictions = reseau.predict(img)
classe = np.argmax(predictions)

print(f"L'image correspond au chiffre: {classe}")