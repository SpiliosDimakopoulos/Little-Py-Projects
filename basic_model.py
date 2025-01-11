import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

np.random.seed(42)
X_train = np.random.rand(2000, 2)
y_train = np.random.randint(0, 4, 2000)

model = Sequential([
    Dense(25, activation='relu', input_shape=(2,)),
    Dense(15, activation='relu'),
    Dense(4, activation='softmax')
])

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001),
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=10)

predictions = model.predict(X_train)

print("Predictions shape:", predictions.shape)
