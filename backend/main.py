from flask import Flask, jsonify, request,g
from flask_cors import CORS
from models import db, User, Dish, State
import os
from flask_jwt_extended import JWTManager,create_access_token,jwt_required, get_jwt_identity,decode_token,get_jwt
import sqlite3
import datetime
from datetime import timezone,timedelta
from flask import jsonify, request , send_file
from sqlalchemy import func, distinct



app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
Database = os.path.join(BASE_DIR, 'Database.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'Database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Qfi-2.0@123'

db.init_app(app)

def get_db():
    db = getattr(g, '_database',None)
    if db is None:
        db = g._database = sqlite3.connect(Database)
    return db


# -------------------- STATES / REGIONS --------------------
@app.route("/api/states", methods=["GET"])
def get_states():
    states = State.query.all()
    print("States fetched from DB:", states)  # Debug
    return jsonify([{"id": s.id, "name": s.name} for s in states])



# -------------------- DISHES BY REGION --------------------
@app.route("/api/dishes", methods=["GET"])
def get_dishes():
    """Fetch first 10 dishes for a given state/region"""
    region_id = request.args.get("region_id")
    if not region_id:
        return jsonify({"error": "region_id is required"}), 400
    region_id = int(region_id)

    dishes = Dish.query.filter_by(state_id=region_id).all()
    dish_list = []
    for d in dishes:
        dish_list.append({
            "id": d.id,
            "name": d.name,
            "title": d.title,
            "description": d.description,
            "image_path": d.image_path,
            "video_link": d.video_link,
            "folk_song": d.folk_song,
            "fun_fact": d.fun_fact,
        })
        print(dish_list)
    return jsonify(dish_list)


# -------------------- SINGLE DISH --------------------
@app.route("/api/dish/<int:dish_id>", methods=["GET"])
def get_dish(dish_id):
    """Fetch single dish by id"""
    d = Dish.query.get_or_404(dish_id)
    return jsonify({
        "id": d.id,
        "name": d.name,
        "title": d.title,
        "description": d.description,
        "image_paths": d.image_paths,
        "video_link": d.video_link,
        "folk_song": d.folk_song,
        "fun_fact": d.fun_fact,
    })


# -------------------- USER LOGIN EXAMPLE --------------------
@app.route("/api/login", methods=["POST"])
def login():
    """Example JWT login"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or user.password != password:
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token})


# -------------------- RUN --------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # ensure tables exist
    app.run(debug=True)

