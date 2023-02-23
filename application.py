from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pandas as pd
#import pickle
import numpy as np
import sys
import pickle
model = pd.read_pickle('./LinearRegressionModel.pkl')
#model = pickle.load(open('LinearRegressionModel.pkl','rb'))
app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict',methods=['POST'])
@cross_origin()

def prediction():
        Name= request.form['Name']
        Engine_Type= request.form['Engine_Type']
        Transmission= request.form['Transmission']
        Color= request.form['Color']
        Assembly= request.form['Assembly']
        Body_Type= request.form['Body_Type']
        Mileage= request.form['Mileage']
        Model_Year= request.form['Model_Year']
        print(Name)
        input_query=np.array([Name,Engine_Type,Transmission,Color,Assembly,Body_Type,Mileage,Model_Year])
        print(input_query)
        try:
            #predicting the price of the car using the model and the input query
            predict=model.predict(pd.DataFrame([input_query],columns=['Name','Engine_Type','Transmission','Color','Assembly','Body_Type','Mileage', 'Model_Year']))
            print(predict)
            return jsonify({'Prediction':str(predict)})
        except:
             print(sys.exc_info()[0])

if __name__ == '__main__':
    app.run(debug=True)

