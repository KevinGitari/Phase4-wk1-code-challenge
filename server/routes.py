from flask import Blueprint, jsonify, request
from models import db, Hero, Power, HeroPower
from app import app

bp = Blueprint('api', __name__)

@bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@bp.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

app.register_blueprint(bp, url_prefix='/api')
