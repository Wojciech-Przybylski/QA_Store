from application import db, app
from application.models import Items, Basket, BasketItem, Orders, Types

with app.app_context():
    
    db.drop_all()
    db.create_all()
    
    testtype1 = Types(type='Fruit')
    testtype2 = Types(type='Vegetable')
    testtype3 = Types(type='Dairy')
    db.session.add(testtype1)
    db.session.add(testtype2)
    db.session.add(testtype3)
    db.session.commit()
    
    testitem1 = Items(name='Pepper', stock=50, price=1, type_id=2)
    testitem2 = Items(name='Apple', stock=50, price=0.75, type_id=1)
    testitem3 = Items(name='Banana', stock=50, price=0.95, type_id=1)
    testitem4 = Items(name='Watermelon', stock=50, price=2.10, type_id=1)
    testitem5 = Items(name='Garlic', stock=50, price=0.50, type_id=2)
    testitem6 = Items(name='Tomato', stock=50, price=0.45, type_id=2)
    testitem7 = Items(name='Broccoli', stock=50, price=1.10, type_id=2)
    testitem8 = Items(name='Milk', stock=50, price=1.75, type_id=3)
    testitem9 = Items(name='Cheese', stock=50, price=3.55, type_id=3)
    testitem10 = Items(name='Cream', stock=50, price=2.45, type_id=3)
    db.session.add(testitem1)
    db.session.add(testitem2)
    db.session.add(testitem3)
    db.session.add(testitem4)
    db.session.add(testitem5)
    db.session.add(testitem6)
    db.session.add(testitem7)
    db.session.add(testitem8)
    db.session.add(testitem9)
    db.session.add(testitem10)
    db.session.commit()
    
    