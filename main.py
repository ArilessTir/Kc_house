from flask import Flask, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model_registry/model.sav', 'rb'))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/prediction", methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        data = pd.read_json(request.data, orient='index').T
        predcition = model.predict(data)
        return str(predcition)
if __name__ == "__main__":
    app.run(host='0.0.0.0')