import tensorflow.keras as keras
import numpy as np
import os
from flask import Flask, jsonify, request, send_from_directory

def predict(model, data):

    data = np.array([data], dtype=float)

    prediction = 1 if model.predict(data)>0.5 else 0

    return {'result':prediction}


model = keras.models.load_model('diabetes.h5')

app = Flask(__name__)

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                           'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/predict', methods=['POST'])
def load_preddict():

    data = request.get_json(force=True)
    print('\n', data,'\n')
    prediction = predict(model, data['input'])
   
    return jsonify(prediction)

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':

    port = os.environ.get("PORT", 5000)
    app.run(debug=True, host="0.0.0.0", port=port) #, host='0.0.0.0', port=os.getenv('PORT'))