from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np

def pokemon_classifier(img, weights_file):
    model = keras.models.load_model(weights_file)


    data = np.ndarray(shape=(1,128,128,3), dtype=np.float32)
    image = img
    size = (128,128,3)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32)/127.0)-1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    return np.argmax(prediction)


