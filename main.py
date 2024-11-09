import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2

model = load_model('pneumonia_cnn_model.h5')

img_path = 'test/NORMAL-9092354-0001.jpeg'
img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = cv2.cvtColor(img_array.astype('uint8'), cv2.COLOR_RGB2GRAY)
img_array = np.expand_dims(img_array, axis=-1)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

print("\n")

prediction = model.predict(img_array)

if prediction >= 0.5:
    print(f"Prediction: Pneumonia (probability: {100*prediction[0][0]:.2f}%)")
else:
    print(f"Prediction: Normal (probability: {100 - 100*prediction[0][0]:.2f}%)")