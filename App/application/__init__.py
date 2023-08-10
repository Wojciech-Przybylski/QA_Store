from flask import Blueprint, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)



def create_app():
    
    app.template_folder = 'templates'
    
    main_bp = Blueprint('main', __name__)

    @app.route('/', methods=['GET','POST'])
        
    def home():
        from application import models

        
        items = models.Items.query.all()
        baseUrl = '/static/'
        
        return render_template("home.html", items=items, baseUrl=baseUrl) 
    
    app.register_blueprint(main_bp)


    # bcrypt = Bcrypt(app)
    
    return app





