from flask import Flask,render_template,request,redirect,url_for
from models import db,AnimeList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route('/')
def home():
    rows = AnimeList.query.all()
    if rows:
        return render_template('index.html',rows=rows)

@app.route('/character/<int:char_id>')
def character(char_id):
    character  = AnimeList.query.filter_by(id=char_id).first()
    if character :
        return render_template('character.html',character=character )
    else:
        return 'NOT FOUND! Page is in progress btw!'


if __name__ == "__main__":
    app.run()
