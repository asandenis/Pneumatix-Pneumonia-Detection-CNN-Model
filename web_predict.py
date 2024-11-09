import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import cv2

def prediction(img_path, model):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = cv2.cvtColor(img_array.astype('uint8'), cv2.COLOR_RGB2GRAY)
    img_array = np.expand_dims(img_array, axis=-1)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    return float(prediction[0][0])