from keras.models import load_model
from PIL import ImageGrab, Image
import numpy as np
import cv2

model = load_model('mnist.h5')
IMG_DIR = 'images/'


def predict_digit(img):
    # resize image to 28x28 pixels
    dim = (28, 28)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # convert rgb to grayscale

    resized = np.invert(np.array(resized))
    # reshaping to support our model input and normalizing
    # resized = resized.reshape(1, 28, 28, 1)
    # resized = resized / 255.0
    # predicting the class
    res = model.predict(resized)
    return np.argmax(res), max(res)


if __name__ == "__main__":
    image = cv2.imread(IMG_DIR + 'A.png')
    text = str(predict_digit(image))
    print(text)
