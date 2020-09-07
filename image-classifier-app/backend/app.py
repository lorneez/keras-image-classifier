import datetime
import os
import json
import math
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from keras.models import load_model
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
global model
model = load_model('./cifar.h5')



@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        print(request.files)
        file = request.files['files']
        filename = secure_filename(file.filename)
        absolute_path = os.path.abspath(UPLOAD_FOLDER)
        file.save(os.path.join(absolute_path, filename))
        print("added file")
        return redirect(url_for('prediction', filename=filename))
    return render_template('index.html')


@app.route('/prediction/<filename>')
def prediction(filename):
    my_image = plt.imread(os.path.join('./uploads', filename))
    my_image_re = resize(my_image, (32, 32, 3))
    print("getting prob")
    probabilities = model.predict(np.array([my_image_re, ]))[0, :]
    print(probabilities)
    number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    index = np.argsort(probabilities)
    predictions = {
        "class1": number_to_class[index[9]],
        "class2": number_to_class[index[8]],
        "class3": number_to_class[index[7]],
        "prob1": math.trunc(np.float64(probabilities[index[9]]) * 100),
        "prob2": math.trunc(np.float64(probabilities[index[8]]) * 100),
        "prob3": math.trunc(np.float64(probabilities[index[7]]) * 100),
    }
    return json.dumps(predictions)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
