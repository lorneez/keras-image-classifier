import matplotlib.pyplot as plt
import numpy as np

import datetime
import os
import json
import math

from flask import Flask, request, redirect, url_for, render_template
from flask_cors import CORS

from werkzeug.utils import secure_filename

from keras.models import load_model

from skimage.transform import resize


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads/'
global model
model = load_model('./cifar.h5')

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        file = request.files['image']
        image = saveAndResize(file)
        probabilities = model.predict(np.array([image, ]))[0, :]
        return json.dumps(generatePrediction(probabilities)), 200
    return render_template('index.html')

def generatePrediction(probabilities):
      number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
      for i in range(10):
              print(number_to_class[i], probabilities[i])
      index = np.argsort(probabilities)

      predictions = {
        "class1": number_to_class[index[9]],
        "prob1": math.trunc(np.float64(probabilities[index[9]]) * 100),
      }
      return predictions

def saveAndResize(file):
    filename = secure_filename(file.filename)
    absolute_path = os.path.abspath(UPLOAD_FOLDER)
    file.save(os.path.join(absolute_path, filename))
    my_image = plt.imread(os.path.join('./uploads', filename))
    my_image_re = resize(my_image, (32, 32, 3))
    my_image_re = my_image_re.astype('float32')
    my_image_re = my_image_re / 255
    return my_image_re

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
