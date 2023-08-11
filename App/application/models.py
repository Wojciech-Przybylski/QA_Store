from application import db
import datetime

class Customers(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    address = db.Column(db.String(50))
    
class Types(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    type = db.Column(db.String(15), nullable=False)
    
class Items(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    type_id = db.Column(db.String(15), db.ForeignKey('types.id'), nullable=False)

    
class Basket(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    basket_status = db.Column(db.Boolean, default=True, nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    #expiry_time = db.Column(db.DateTime, nullable=False)

class BasketItem(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Orders(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    order_status = db.Column(db.Boolean, default=True, nullable=False)
