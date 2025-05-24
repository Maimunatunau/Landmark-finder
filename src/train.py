import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Paths to your training and validation data folders
train_dir = 'data/train'
val_dir = 'data/val'

# Data augmentation and preprocessing for training set
train_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
)

# Only rescaling for validation set
val_gen = ImageDataGenerator(rescale=1./255)

# Flow training images in batches
train_data = train_gen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=True
)

# Flow validation images in batches
val_data = val_gen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

# Load MobileNetV2 pre-trained on ImageNet, excluding top layers
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224,224,3))

# Freeze base model weights so they don’t get updated during initial training
base_model.trainable = False

# Add custom classification head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
output = Dense(train_data.num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model for 10 epochs
model.fit(train_data, validation_data=val_data, epochs=10)

# Save the trained model for later use
# model.save('lazy_landmark_model.h5')
# model.save('lazy_landmark_model_savedmodel', save_format='tf')
# model.save('lazy_landmark_model.keras')
# Save as TensorFlow SavedModel format (folder)
model.export('lazy_landmark_model_savedmodel')  # TensorFlow SavedModel export



print("Training complete. Model saved as 'lazy_landmark_model.h5'")
