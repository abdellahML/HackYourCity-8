from flask import Flask, render_template, flash, url_for, redirect, request
from flask import current_app as app
from app.form import LoginForm,RegistrationForm
from app.user import User

from datetime import datetime
import random, os


@app.route('/')
@app.route('/home')
def index():
    message = "Hello !"
    return render_template('index.html', message=message)

@app.route('/user_pref/', methods=['GET','POST'])
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
    

@app.route('/user_pref/<what>', methods=['GET','POST'])
def user_pref_to_do(what):
    '''
    Recup le deuxième choix de l'user, 
    redirige vers /user_pref/<what>/<location>
    '''
    if request.method == 'POST':
        print('Dans deuxième choix')
        print(len(list(request.form.items())))
        for keys, val in request.form.items():
            print(keys,val)
            #what = {keys:val}
            location = val
            print(f"location = {location}")
            return redirect(url_for("user_pref_location",what = what, location=location))

    print(f"In user_pref {what}")
    message = "Où?"
    
    return render_template('user_pref_to_do.html', message=message, what=what)

@app.route('/user_pref/<what>/<location>', methods=['GET', 'POST'])
def user_pref_location(what,location):
    '''
    Recup le deuxième choix de l'user, 
    redirige vers /user_pref/<what>/<location>
    '''

    message = "Animation?"

    if request.method == 'POST':
        print('Dans troisième choix')
        print(len(list(request.form.items())))
        for keys, val in request.form.items():
            print(keys,val)
            #what = {keys:val}
            animation = val
            print(f"animation = {animation}")
            user = User(id_=random.randint(0,2500),what=what,location=location,animation=animation)
            return redirect(url_for("resultat",what = what, location=location, animation=animation,user=user))

    return render_template('user_pref_location.html', message=message,what=what,location=location)


@app.route('/user_pref/<what>/<location>/<animation>/<user>', methods=['GET', 'POST'])
def resultat(what,location, animation,user):
    '''
    Recup le deuxième choix de l'user, 
    redirige vers /user_pref/<what>/<location>/<animation>
    '''

    message = "Voyons voir ce qu'on pourrait vous proposer..."
    
    return render_template('resultat.html', message=message,what=what,location=location, animation=animation,user=user)



@app.route('/login', methods=['GET', 'POST'])    #post and get
def login():
    '''On this function we have post request so we post the information that we got from the field, and if it's valid
    we will redirect to the home page with a little message that give the username and the length of the password'''

    form = LoginForm()

    if form.validate_on_submit():
        flash("Login success for user {} with password of length: {} !".format(form.username.data, len(form.password.data)), 'success')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


##
@app.route('/valid')
def valid():
    "Renvoie sur la page de validation avec possible map"
    #return render_template(folium object > check doc folium)
    return render_template ("valid.html")
