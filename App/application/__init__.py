from flask import Blueprint, Flask, render_template, request
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
    
    
    @app.route('/contact_us')
    def contact_us():
        from application import models

        baseUrl = '/static/'
        
        return render_template("contact_us.html", baseUrl=baseUrl) 
    
    
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

        
    @app.route('/add_to_cart', methods=['POST'])
    def add_to_cart():
        from application import models
        
        items = models.Items.query.all()

        baseUrl = '/static/'

        item_id = request.form.get('item_id')
        quantity = request.form.get('quantity')        
        
        print(f'request to add {item_id}=item_id and {quantity}=quantity')
        
        basket = models.Basket.query.filter_by(basket_status='Open').first()
        if basket == None:
            basket = models.Basket()
            db.session.add(basket)
            db.session.commit()
            
        # Check if the item is already in the cart
        basket_item = models.BasketItem.query.filter_by(basket_id=basket.id, item_id=item_id).first()
        if basket_item:
            print(f"adding {basket_item.item_id}=Item.id to {basket_item.basket_id}=Basket.id  and {basket_item.quantity}=Quantity")
            # Update the quantity
            basket_item.quantity += int(quantity)
        else:
            # Create a new basket item
            basket_item = models.BasketItem(basket_id=basket.id, item_id=item_id, quantity=quantity)
            db.session.add(basket_item)
        
        db.session.commit()
        return render_template("shop.html", items=items, baseUrl=baseUrl) 
    
    
    @app.route('/basket')
    def basket():
        from application import models

        baseUrl = '/static/'

        basket = models.Basket.query.filter_by(basket_status='Open').first() 
        if basket != None:
            basket_total = basket.calculate_total_basket_price()
            item_totals = basket.calculate_total_per_basket_item()
            print(item_totals)
        else:
            basket_total = ""
            item_totals = ""
              
        
        return render_template("basket.html", basket_total=basket_total, item_totals=item_totals,  baseUrl=baseUrl) 
    
    @app.route('/checkout')
    def checkout():
        from application import models

        baseUrl = '/static/'

        basket = models.Basket.query.filter_by(basket_status='Open').first() 
        if basket != None:
            basket_total = basket.calculate_total_basket_price()
            item_totals = basket.calculate_total_per_basket_item()
            print(item_totals)
              
        
        return render_template("checkout.html", basket_total=basket_total, item_totals=item_totals,  baseUrl=baseUrl) 
    
    @app.route('/place_order', methods=['POST'])
    def place_order():
        from application import models
        
        baseUrl = '/static/'
        
        orders = models.Orders.query.filter_by(order_status='Open')

        
        basket = models.Basket.query.filter_by(basket_status='Open').first() 
        if basket != None:
            full_name = request.form.get('full_name')
            email = request.form.get('email')
            address1 = request.form.get('address1')
            address2 = request.form.get('address2')
            city = request.form.get('city')
            post_code = request.form.get('post_code')
            basket_total = basket.calculate_total_basket_price()
            
            print(f'request to add {full_name}=full_name and {email}=email, and {address1}=addess1, and {address2}=addess2, and {city}=city, and {post_code}=post_code')
        
            order = models.Orders(basket_id=basket.id, 
                        total_price=basket_total.replace("£", ""), 
                        full_name=full_name,
                        email=email,
                        address1=address1,
                        address2=address2,
                        city=city,
                        post_code=post_code)
            db.session.add(order)
            basket.basket_status = 'Closed'
            db.session.add(basket)
            db.session.commit()
            
        return render_template("orders.html", orders=orders, baseUrl=baseUrl) 
     
    @app.route('/payment_view', methods=['POST'])
    def payment_view():
        from application import models

        baseUrl = '/static/'
        
        order_id = request.form.get('order_id') 
        print(f"Payment_view request to make order_id = {order_id}")              
        
        return render_template("payment.html", order_id=order_id, baseUrl=baseUrl) 
    
    @app.route('/pay', methods=['POST'])
    def pay():
        from application import models
        
        baseUrl = '/static/'
        
        order_id = request.form.get('order_id')
        
        print(f"Pay - request to make order_id = {order_id}")
        
        order = models.Orders.query.filter_by(id=order_id).first() 
        if order != None:
            full_name = request.form.get('full_name')
            card_number = request.form.get('card_number')
            expiry_date = request.form.get('expiry_date')
            cvv = request.form.get('cvv')
            
            
            print(f'request to add {full_name}=full_name and {card_number}=card_number, and {expiry_date}=addess1, and {cvv}=cvv')
        
            payment = models.Payment(order_id=order.id, 
                        full_name=full_name,
                        card_number=card_number,
                        expiry_date=expiry_date,
                        cvv=cvv)
            db.session.add(payment)
            order.order_status = 'Paid'
            db.session.add(order)
            
            db.session.commit()
        
        return render_template("home.html", baseUrl=baseUrl)  
        

    @app.route('/orders')
    def orders():
        from application import models

        baseUrl = '/static/'
        
        orders = models.Orders.query.filter_by(order_status='Open')
               
        
        return render_template("orders.html", orders=orders, baseUrl=baseUrl)
     
    
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





