import util
from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/hello')
def get_location_names():
    response = jsonify({
        'locations' : util.get_loaction_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response
    

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    responaw =jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })



if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()