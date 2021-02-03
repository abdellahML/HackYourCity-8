from flask import Flask, render_template, flash, url_for, redirect, request
from form import LoginForm

from datetime import datetime
import random, os

'''With wtforms, we have to configure a secret_key, here we just hard code it but normaly we shouldn't'''
app = Flask(__name__)
app.config['SECRET_KEY']="kbfvizrguzourgu"

@app.route('/')
#@app.route('/home')
def index():
    '''Here we configure the url path, and with we return a html, it's the same with other functions'''

    return render_template('index.html', message="Hello !")

@app.route('/status')   #get
def status():
    return render_template('status.html')

@app.route('/login', methods=['GET', 'POST'])    #post and get
def login():
    '''On this function we have post request so we post the information that we got from the field, and if it's valid
    we will redirect to the home page with a little message that give the username and the length of the password'''

    form = LoginForm()

    if form.validate_on_submit():
        flash("Login success for user {} with password of length: {} !".format(form.username.data, len(form.password.data)), 'success')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/predict', methods=['GET', 'POST'])    #get
def predict():
    '''Here the function will just display month, custumor visiting website, seller available and a prediction between
    2000 and 5000'''

    mydate = datetime.now()
    month = mydate.strftime("%B")

    custumors = 100

    sellers = 12

    predict = random.randint(2000, 5000)

    return render_template('predict.html', month=month, custumor_visiting_website= custumors, seller_available=sellers, prediction=predict)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)