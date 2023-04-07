from fastapi import FastAPI
from tensorflow import keras
import numpy as np
import cv2

app = FastAPI()

encoder = keras.models.load_model('encoder')

def classify_images(face1, face2, threshold=1.3):
    tensor1 = encoder.predict(face1)
    tensor2 = encoder.predict(face2)
    
    distance = np.sum(np.square(tensor1-tensor2), axis=-1)
    prediction = np.where(distance<=threshold, 0, 1)
    return prediction

def read_img(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

@app.get("/")
async def root():
    img1 = read_img("image_uploaded\im2.jpg")
    img1 = np.expand_dims(img1, axis=0)
    img2 = read_img("list_anchor\im1.jpg")
    img2 = np.expand_dims(img2, axis=0)
    pred = classify_images(img1, img2)
    return {"message": str(pred)}