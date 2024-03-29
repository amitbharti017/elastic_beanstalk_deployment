import joblib
import numpy as np 
from flask import Flask, request, Response
import json

app = Flask(__name__)
@app.route('/')
def home_endpoint():
    return "Home Page"

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    test_data = request.get_json()
    test_data = np.array(test_data)
    predictions = model.predict(test_data)
    response = json.dumps(predictions.tolist())
    return Response(response,status=200,mimetype="application/json")


if __name__ == "__main__":
    model = joblib.load('models/rf_clf.joblib')
    app.run(host='0.0.0.0',port=8080)