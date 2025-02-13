from flask import Blueprint, jsonify

root_bp = Blueprint('root', __name__)

@root_bp.route('/', methods=['GET'])
def get_root_data():
    data = {
    'name': 'Verônica Alves', 
    'email': "veagalves@gmail.com", 
    'linkedin': 'https://www.linkedin.com/in/vealves/'
    }

    return jsonify(data), 200