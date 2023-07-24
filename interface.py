from flask import Flask, render_template, request, jsonify
from utils import HousePricePrediction

hpp = HousePricePrediction()

app = Flask(__name__)

################ Root API ########################################
@app.route('/')
def index():
   return render_template('home.html')


################# Location Name API ################################
@app.route('/get_location_names')
def get_location_names():
    locations =  hpp.get_location_names()  
    return jsonify({"locations":locations})


@app.route('/predict_home_price', methods = ['POST','GET'])
def predict_home_price():
    if request.method == 'POST':
        total_sqft = eval(request.form['total_sqft'])
        bhk = eval(request.form['bhk'])
        bath = eval(request.form['bath'])
        location = request.form['loc']
        print('location, sqft, bath, bhk',location, total_sqft, bath, bhk)
        price = hpp.get_house_price(location, total_sqft, bath, bhk)
        return render_template('home.html', prediction_text = price)
    
    if request.method == 'GET':
        total_sqft = int(request.args.get('total_sqft'))
        bhk = int(request.args.get('bhk'))
        bath = int(request.args.get('bath'))
        location = request.args.get('location')
        print('location, sqft, bath, bhk',location, total_sqft, bath, bhk)
        price = hpp.get_house_price(location, total_sqft, bath, bhk)
        return render_template('home.html', prediction_text = price)

if __name__ == "__main__":
    app.run(debug=True)