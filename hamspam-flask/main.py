import numpy as np
from flask import Flask, request, jsonify, render_template
from Prediction import Prediction

app = Flask(__name__)
model=Prediction()

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text_input= [str(x) for x in request.form.values()][0]


    output=model.predict(text_input)

    return render_template('index.html', prediction_text='The text is {}!!'.format(output))


if __name__ == "__main__":
    app.run(debug=True)