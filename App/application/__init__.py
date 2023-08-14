from flask import Blueprint, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)



def create_app():
    
    app.template_folder = 'templates'
    
    main_bp = Blueprint('main', __name__)

    @app.route('/')
    def home():
        from application import models

        baseUrl = '/static/'
        
        return render_template("home.html", baseUrl=baseUrl) 
    
    @app.route('/about')
    def about():
        from application import models

        baseUrl = '/static/'
        
        return render_template("about.html", baseUrl=baseUrl) 
    
    @app.route('/shop', methods=['GET','POST'])
    def shop():
        from application import models

        
        items = models.Items.query.all()
        baseUrl = '/static/'
        
        return render_template("shop.html", items=items, baseUrl=baseUrl) 
    
    @app.route('/orders')
    def orders():
        from application import models

        baseUrl = '/static/'
        
        return render_template("orders.html", baseUrl=baseUrl) 
    
    @app.route('/categories')
    def categories():
        from application import models
    
        items = models.Types.query.filter_by(type=models.Types.type)

        baseUrl = '/static/'
        
        return render_template("categories.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Fruit')
    def fruit():
        from application import models
    
        items = models.Items.query.filter_by(type_id='1').all()

        baseUrl = '/static/'
        
        return render_template("Fruit.html", baseUrl=baseUrl, items=items)
     
    @app.route('/Vegetable')
    def vegetable():
        from application import models
    
        items = models.Items.query.filter_by(type_id='2').all()

        baseUrl = '/static/'
        
        return render_template("Vegetable.html", baseUrl=baseUrl, items=items)
     
    @app.route('/Dairy')
    def dairy():
        from application import models
    
        items = models.Items.query.filter_by(type_id='3').all()

        baseUrl = '/static/'
        
        return render_template("Dairy.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Apple')
    def apple():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/apple.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Banana')
    def banana():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/banana.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Broccoli')
    def broccoli():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/broccoli.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Cheese')
    def cheese():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/cheese.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Cream')
    def cream():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/cream.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Garlic')
    def garlic():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/garlic.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Milk')
    def milk():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/milk.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Pepper')
    def pepper():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/pepper.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Tomato')
    def tomato():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/tomato.html", baseUrl=baseUrl, items=items) 
    
    @app.route('/Watermelon')
    def watermelon():
        from application import models
    
        items = models.Items.query.all()

        baseUrl = '/static/'
        
        return render_template("indiv_items/watermelon.html", baseUrl=baseUrl, items=items) 
    
    app.register_blueprint(main_bp)


    # bcrypt = Bcrypt(app)
    
    return app





