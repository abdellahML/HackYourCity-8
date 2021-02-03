from app import init_app
from flask import session

app = init_app()

if __name__ == "__main__":
    app.run(debug=True)
