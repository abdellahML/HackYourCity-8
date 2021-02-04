from flask import Flask, render_template, flash, url_for, redirect, request
from flask import current_app as app
from app.form import LoginForm,RegistrationForm

from datetime import datetime
import random, os


@app.route('/')
@app.route('/home')
def index():
    message = "Hello !"
    return render_template('index.html', message=message)

@app.route('/user_pref/', methods=['GET', 'POST'])
def user_pref():
    '''
    Recup le premier choix de l'user, 
    redirige vers /user_pref/<what>
    '''
    if request.method == 'POST':
        print('Dans premier choix')
        for keys, val in request.form.items():
            #what = {keys:val}
            what = val
            print(f"What = {what}")
            return redirect(url_for("user_pref_to_do",what = what))

    message = "Quoi?"  
    return render_template('user_pref.html', message=message)
    

@app.route('/user_pref/<what>', methods=['GET', 'POST'])
def user_pref_to_do(what):
    '''
    Recup le deuxième choix de l'user, 
    redirige vers /user_pref/<what>/<location>
    '''
    if request.method == 'POST':
        print('Dans deuxième choix')
        for keys, val in request.form.items():
            #what = {keys:val}
            location = val
            print(f"location = {location}")
            return redirect(url_for("user_pref_location",what = what,location=location))

    print(f"In user_pref {what}")
    message = "Où?"
    
    return render_template('user_pref_to_do.html', message=message, what=what)

@app.route('/user_pref/<what>/<location>', methods=['GET', 'POST'])
def user_pref_location(what,location):
    '''Here we configure the url path, and with we return a html, it's the same with other functions'''

    message = "Animation?"

    return render_template('user_pref_animation.html', message=message)









    

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
    app.run(host='0.0.0.0', port=port, debug= True)