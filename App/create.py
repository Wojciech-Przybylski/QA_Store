# from application import db, app
# from application.models import Customers, Items, Basket, BasketItem, Orders

# with app.app_context():
    
#     db.drop_all()
#     db.create_all()
    
#     testcustomer = Customers(username='wojtasek58', password='password', first_name="Wojciech", last_name="Przybylski", address="CF10 8DF" )
#     db.session.add(testcustomer)
#     db.session.commit()
    
#     testitem = Items(name='Pepper', stock=50, price=1.55, type="vegetable")
#     db.session.add(testitem)
#     db.session.commit()
    
#     testbasket = Basket(user_id=1)
#     db.session.add(testbasket)
#     db.session.commit()
    
#     testbasketitem = BasketItem(basket_id=1, item_id=1, quantity=10)
#     db.session.add(testbasketitem)
#     db.session.commit()
    
#     testbasketitem = Orders(basket_id=1, total_price=15.50)
#     db.session.add(testbasketitem)
#     db.session.commit()
    