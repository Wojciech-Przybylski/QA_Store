from application import db
import datetime

class Types(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    type = db.Column(db.String(15), nullable=False)
    
class Items(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    type_id = db.Column(db.String(15), db.ForeignKey(Types.id), nullable=False)

    
class Basket(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    basket_status = db.Column(db.String, default='Open', nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    #expiry_time = db.Column(db.DateTime, nullable=False)
    
    basket_items = db.orm.relationship('BasketItem')
    
    def calculate_total_basket_price(self):
        total = 0
        for basket_item in self.basket_items:
            total += basket_item.item_total
        return f'£{total:.2f}'
    
    def calculate_total_per_basket_item(self):
        item_list = []
        for basketItem in self.basket_items:
            item_list.append({"Item_Name":basketItem.item_name,"Total_Price":f"£{basketItem.item_total:.2f}","Quantity":basketItem.quantity,"Price":f"£{basketItem.item_price:.2f}"})
        return item_list
           
class BasketItem(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey(Basket.id), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey(Items.id), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    items = db.orm.relationship('Items')
    
    @property
    def item_total(self):
        return self.quantity * self.items.price
    
    @property
    def item_name(self):
        return self.items.name
    
    @property
    def item_price(self):
        return self.items.price
    
class Orders(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey(Basket.id), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    order_status = db.Column(db.String, default='Open', nullable=False)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address1 = db.Column(db.String, nullable=False)
    address2 = db.Column(db.String)
    city = db.Column(db.String, nullable=False)
    post_code = db.Column(db.String, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(Orders.id), nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    payment_status = db.Column(db.String, default='Pending', nullable=False)
    full_name = db.Column(db.String, nullable=False)
    card_number = db.Column(db.String, nullable=False)
    expiry_date = db.Column(db.String, nullable=False)
    cvv = db.Column(db.Integer)

