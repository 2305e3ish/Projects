import tensorflow as tf
import tensorflow_hub as hub
import os

# Set dataset paths
train_dir = "../dataset/train"
validation_dir = "../dataset/val"  # Updated path

# Load training dataset
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    train_dir,
    image_size=(224, 224),
    batch_size=32
)

# Load validation dataset
validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    validation_dir,
    image_size=(224, 224),
    batch_size=32
)

# ✅ Fixed TensorFlow Hub Model URL
feature_extractor_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"


feature_layer = hub.KerasLayer(feature_extractor_url, input_shape=(224, 224, 3), trainable=False)

# Build model
model = tf.keras.Sequential([
    feature_layer,
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(train_dataset.class_names), activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=10
)
