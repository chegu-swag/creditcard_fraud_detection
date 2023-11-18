from flask import Flask,render_template, request
import joblib

app=Flask(__name__)

# code business logic


@app.route('/')
def base():
    return render_template('home.html')

@app.route('/predict', methods=['post'])
def predict():
    # load the model
    model=joblib.load('cc_fraud_detection.pkl')

    amount=request.form.get('Amount')
    category=request.form.get('Category')
    merchant=request.form.get('Merchant')
    age=request.form.get('Age')
    city_population=request.form.get('city_pop')
    
    
    print(amount,category,merchant,age,city_population)
    
    out=model.predict([[amount,category,merchant,age,city_population]])[0]
    print(out)
    
    if out==1:
        data="FRAUD"
    else:
        data="NOT A FRAUD"

    return render_template('predict.html',data=data)
if __name__=="__main__":
    app.run(debug=True)
