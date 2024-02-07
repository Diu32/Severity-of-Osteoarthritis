# -*- coding: utf-8 -*-
"""ResNet152 of Osteoarthritis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16tsXYcJcC9qo6PUAStqp6c8phf-RyYU5

#Accessing Data from Google Drive
"""

from google.colab import drive
drive.mount("/content/drive")

#copy the data from drive to colab. Copying a saved model from gdrive to colab.
!mkdir 'OA/'
!cp -r '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata' '/OA/'

"""#Data Preprocessing

"""

import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
image_size = (224, 224)
batch_size = 32
train_ds = image_dataset_from_directory(
    "/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I",
    labels = "inferred",
    label_mode = 'int',
    validation_split=0.2,
    subset="training",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)
val_ds =image_dataset_from_directory(
    "/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I",
    labels = "inferred",
    label_mode = 'int',
    validation_split=0.2,
    subset="validation",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
image_size = (224, 224)
batch_size = 32
enhanced_train_ds = image_dataset_from_directory(
    "/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/Clahe_Images",
    labels = "inferred",
    label_mode = 'int',
    validation_split=0.2,
    subset="training",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)
enhanced_val_ds =image_dataset_from_directory(
    "/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/Clahe_Images",
    labels = "inferred",
    label_mode = 'int',
    validation_split=0.2,
    subset="validation",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

"""#visualizing the data"""

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")

"""This function applies CLAHE (Contrast Limited Adaptive Histogram Equalization) to an input image using the OpenCV library in Python. CLAHE is a technique used to enhance the contrast of an image by redistributing the intensity levels in a way that limits the amplification of noise."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to apply CLAHE
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel = lab_image[:, :, 0]
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahe_l_channel = clahe.apply(l_channel)
    lab_image[:, :, 0] = clahe_l_channel
    return cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

# Load the X-ray image (replace 'your_image_path' with the actual path)
image_path = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/4Severe/SevereG4 (1).png'
xray_image = cv2.imread(image_path)

# Apply average filter to remove noise
filtered_image = apply_average_filter(xray_image, filter_size=16)

# Apply CLAHE to enhance contrast
enhanced_image = apply_clahe(xray_image)

# Plot the images using matplotlib.pyplot
plt.figure(figsize=(10, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(xray_image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Enhanced Image
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB))
plt.title('Enhanced Image')
plt.axis('off')

plt.show()

import os
import cv2
import numpy as np

# Function to apply CLAHE
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel = lab_image[:, :, 0]
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahe_l_channel = clahe.apply(l_channel)
    lab_image[:, :, 0] = clahe_l_channel
    return cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

# Input and Output folders
input_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/0Normal'
output_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/Clahe_Images/Normal_clahe'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image in the input folder
for image_filename in os.listdir(input_folder):
  if image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
     input_image_path = os.path.join(input_folder, image_filename)

    # Load the X-ray image
     xray_image = cv2.imread(input_image_path)

    # Apply CLAHE to enhance contrast
     enhanced_image = apply_clahe(xray_image)

    # Save the enhanced image to the output folder
     output_image_path = os.path.join(output_folder, image_filename)
     cv2.imwrite(output_image_path, enhanced_image)

print("Enhancement complete.")

import os
import cv2
import numpy as np

# Function to apply CLAHE
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel = lab_image[:, :, 0]
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahe_l_channel = clahe.apply(l_channel)
    lab_image[:, :, 0] = clahe_l_channel
    return cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

# Input and Output folders
input_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/1Doubtful'
output_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/Clahe_Images/Doubtful_clahe'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image in the input folder
for image_filename in os.listdir(input_folder):
  if image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
     input_image_path = os.path.join(input_folder, image_filename)

    # Load the X-ray image
     xray_image = cv2.imread(input_image_path)

    # Apply CLAHE to enhance contrast
     enhanced_image = apply_clahe(xray_image)

    # Save the enhanced image to the output folder
     output_image_path = os.path.join(output_folder, image_filename)
     cv2.imwrite(output_image_path, enhanced_image)

print("Enhancement complete.")

import os
import cv2
import numpy as np

# Function to apply CLAHE
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel = lab_image[:, :, 0]
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahe_l_channel = clahe.apply(l_channel)
    lab_image[:, :, 0] = clahe_l_channel
    return cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

# Input and Output folders
input_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/2Mild'
output_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/Clahe_Images/Mild_clahe'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image in the input folder
for image_filename in os.listdir(input_folder):
  if image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
     input_image_path = os.path.join(input_folder, image_filename)

    # Load the X-ray image
     xray_image = cv2.imread(input_image_path)

    # Apply CLAHE to enhance contrast
     enhanced_image = apply_clahe(xray_image)

    # Save the enhanced image to the output folder
     output_image_path = os.path.join(output_folder, image_filename)
     cv2.imwrite(output_image_path, enhanced_image)

print("Enhancement complete.")

import os
import cv2
import numpy as np

# Function to apply CLAHE
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel = lab_image[:, :, 0]
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahe_l_channel = clahe.apply(l_channel)
    lab_image[:, :, 0] = clahe_l_channel
    return cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

# Input and Output folders
input_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/3Moderate'
output_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/Clahe_Images/Moderate_clahe'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image in the input folder
for image_filename in os.listdir(input_folder):
  if image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
     input_image_path = os.path.join(input_folder, image_filename)

    # Load the X-ray image
     xray_image = cv2.imread(input_image_path)

    # Apply CLAHE to enhance contrast
     enhanced_image = apply_clahe(xray_image)

    # Save the enhanced image to the output folder
     output_image_path = os.path.join(output_folder, image_filename)
     cv2.imwrite(output_image_path, enhanced_image)

print("Enhancement complete.")

import os
import cv2
import numpy as np

# Function to apply CLAHE
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel = lab_image[:, :, 0]
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahe_l_channel = clahe.apply(l_channel)
    lab_image[:, :, 0] = clahe_l_channel
    return cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

# Input and Output folders
input_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/4Severe'
output_folder = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/Clahe_Images/Severe_clahe'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image in the input folder
for image_filename in os.listdir(input_folder):
  if image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
     input_image_path = os.path.join(input_folder, image_filename)

    # Load the X-ray image
     xray_image = cv2.imread(input_image_path)

    # Apply CLAHE to enhance contrast
     enhanced_image = apply_clahe(xray_image)

    # Save the enhanced image to the output folder
     output_image_path = os.path.join(output_folder, image_filename)
     cv2.imwrite(output_image_path, enhanced_image)

print("Enhancement complete.")

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet152
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define input shape and number of classes (KL grades)
input_shape = (224, 224, 3)
num_classes = 5  # Assuming 5 KL grades

# Create a ResNet-152 base model
base_model = ResNet152(weights='imagenet', include_top=False, input_shape=input_shape)

# Freeze the layers of the pre-trained ResNet
for layer in base_model.layers:
    layer.trainable = True

# Build the classification head on top of the ResNet features
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Print model summary
model.summary()


train_dir = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I'
validation_dir = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I'

# Use ImageDataGenerator for data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

validation_datagen = ImageDataGenerator(rescale=1./255)

# Set batch size
batch_size = 32

# Create generators for training and validation datasets
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='sparse'  # Assuming labels are integers
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='sparse'
)

# Train the model
history = model.fit(
    train_ds,
    epochs=30,  # Adjust the number of epochs as needed
    validation_data=val_ds
)

import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

# Predict labels for the validation set
y_true = []
y_pred = []

for images, labels in val_ds:
    predictions = model.predict(images)
    predicted_labels = np.argmax(predictions, axis=1)

    y_true.extend(labels)
    y_pred.extend(predicted_labels)

# Convert lists to NumPy arrays
y_true = np.array(y_true)
y_pred = np.array(y_pred)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# Display the confusion matrix
print("Confusion Matrix:")
print(conf_matrix)

# Print classification report
print("\nClassification Report:")
print(classification_report(y_true, y_pred, target_names=[str(i) for i in range(num_classes)]))

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

# ... (Previous code)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# Display the confusion matrix as a heatmap using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=[str(i) for i in range(num_classes)], yticklabels=[str(i) for i in range(num_classes)])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Print classification report
print("\nClassification Report:")
print(classification_report(y_true, y_pred, target_names=[str(i) for i in range(num_classes)]))

model.save("my_model.h5", include_optimizer=True)

model.save_weights("model.h5")

print("Saved model to disk")

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Load and preprocess the image
img_path = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/3Moderate/ModerateG3 (10).png'  # Replace with the path to your image file
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Use your trained model to make predictions
predictions = ffnn_model.predict(img_array)

# Interpret the prediction result
class_index = np.argmax(predictions)
class_label = class_index  # Replace with your class labels if needed

print(f"The predicted class is: {class_label}")

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

# Load the trained model
#model = load_model('your_model_path')

# Preprocess the image
img_path = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/4Severe/SevereG4 (105).png'  # Replace with the path to your image file
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Make predictions
predictions = model.predict(img_array)

# If predictions are logits, apply softmax
predicted_probs = tf.nn.softmax(predictions)
predicted_class = np.argmax(predicted_probs, axis=1)[0]

# Map the predicted class to KL grade
kl_grade_labels = ['KL0', 'KL1', 'KL2', 'KL3', 'KL4']
predicted_kl_grade = kl_grade_labels[predicted_class]

print(f'Predicted KL Grade: {predicted_kl_grade}')

import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

# Load and preprocess the image
img_path = '/content/drive/MyDrive/EDI_A3_OA/Datasets/INDIANdata/MedicalExpert-I/0Normal/NormalG0 (105).png'
img = image.load_img(img_path, target_size=(224, 224))
#img = apply_clahe(img)
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Make predictions
predictions = model.predict(img_array)
predicted_probs = tf.nn.softmax(predictions)
predicted_class = np.argmax(predicted_probs, axis=1)[0]
predicted_kl_grade = kl_grade_labels[predicted_class]

# Display the image with the predicted KL grade
plt.imshow(img)
plt.title(f'Predicted KL Grade: {predicted_kl_grade}')
plt.axis('off')
plt.show()
