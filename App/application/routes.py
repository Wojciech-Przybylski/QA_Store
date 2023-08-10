from application import app, db
from application import Customers, Items
from flask import Flask, render_template, request
from flask_bcrypt import bcrypt
from models import Customers




@app.route('/', methods=['GET','POST'])
def home():
    if request.form:
        person = Customers(name=request.form.get("name"), password=bcrypt.generate_password_hash(request.form.get("password")))
        db.session.add(person)
        db.session.commit()
    registrees = Customers.query.all()
    return render_template("home.html", registrees=registrees)


@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name