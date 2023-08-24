from flask_sqlalchemy import SQLAlchemy

degault_img = 'https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif'

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.Text, nullable=False, default="https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif")
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    db.app = app
    db.init_app(app)