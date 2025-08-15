from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    # Relationship to food items
    dishes = db.relationship('Dish', backref='state', lazy=True)

    def __repr__(self):
        return f"<State {self.name}>"

# Table for food items
class Dish(db.Model):
    __tablename__ = 'dishes'
    id = db.Column(db.Integer, primary_key=True)
    
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    
    name = db.Column(db.String(150), nullable=False)            # Name of the dish
    title = db.Column(db.String(200), nullable=True)           # Short title or heading
    description = db.Column(db.Text, nullable=True)            # Description of the dish
    image_path = db.Column(db.String(300), nullable=True)      # Path to image stored locally
    video_link = db.Column(db.String(300), nullable=True)      # YouTube video link
    folk_song = db.Column(db.String(300), nullable=True)       # Folk song name or file path
    fun_fact = db.Column(db.Text, nullable=True) 
    status = db.Column(db.Text, nullable=True)               # Fun fact about the dish

    def __repr__(self):
        return f"<Dish {self.name} from {self.state.name}>"
    
class Treasure(db.Model):
    __tablename__ = 'treasure'
    id = db.Column(db.Integer, primary_key=True)
    treasure =  db.Column(db.Text, nullable=True)    

with app.app_context():
    db.create_all()
    print(" Database and all tables created successfully.")
