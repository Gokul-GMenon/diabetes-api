import keras
import numpy as np
from flask import Flask, jsonify, request

def predict(model, data):

    data = np.array([data], dtype=float)

    prediction = 1 if model.predict(data)>0.5 else 0

    return {'result':prediction}


model = keras.models.load_model('diabetes.h5')

app = Flask(__name__)

@app.route('/predict/', methods=['POST'])
def load_preddict():

    data = request.get_json(force=True)
    print('\n', data,'\n')
    prediction = predict(model, data['input'])
   
    return jsonify(prediction)

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
