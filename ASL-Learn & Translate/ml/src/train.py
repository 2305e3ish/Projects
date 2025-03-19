import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import layers, models

# Define input shape explicitly
input_shape = (224, 224, 3)
inputs = tf.keras.Input(shape=input_shape)

# Load feature extractor from TensorFlow Hub
feature_extractor_layer = hub.KerasLayer(
    "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4",
    input_shape=input_shape, trainable=False
)

# Ensure the input tensor is compatible with KerasLayer
x = feature_extractor_layer(inputs, training=False)

# Add a dense classification head
x = layers.Dense(128, activation='relu')(x)
x = layers.Dense(36, activation='softmax')(x)  # Adjust based on the number of classes

# Create the model
model = models.Model(inputs=inputs, outputs=x)

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Print model summary
model.summary()
