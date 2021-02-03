from flask import Flask

def init_app():
    app  = Flask(__name__)
    app.config['SECRET_KEY']="kbfvizrguzourgu"
    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        return app