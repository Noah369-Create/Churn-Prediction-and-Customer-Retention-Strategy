import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

scaler = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    if prediction == 0:
        output = "an Active"
    elif prediction ==1:
        output = "a Churn" 


    return render_template('index.html', prediction_text='Customer would most probably  {} customer.'.format(output))


if __name__ == "__main__":
    app.run(debug=True)