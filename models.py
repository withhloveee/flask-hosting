from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AnimeList(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    char_name = db.Column(db.String(100),nullable=False)
    anime_name = db.Column(db.String(100),nullable=False)
    img_url = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text,nullable=False)
    
    #static info
    age = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    height = db.Column(db.String(50), nullable=True)
    birthday = db.Column(db.String(50), nullable=True) 