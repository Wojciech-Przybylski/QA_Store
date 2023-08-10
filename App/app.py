from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')