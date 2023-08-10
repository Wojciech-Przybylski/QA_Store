

# @app.route('/add')
# def add():
#     new_game = Games(name="New Game"
#     db.session.add(new_game)
#     db.session.commit()
#     return "Added new game to database"

# @app.route('/read')
# def read():
#     all_games = Games.query.all()
#     games_string = ""
#     for game in all_games:
#         games_string += "<br>"+ game.name
#     return games_string

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
    # return first_game.name


from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')