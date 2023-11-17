from flask import Blueprint, request, jsonify
from db import db

service_bp = Blueprint('service', __name__)

@service_bp.route('/service/api', methods=['GET'])
def get_service():
    service_data = {
        'service_name': 'SIMPLE API',
        'description': 'This is a sample service description.'
    }
    return jsonify(service_data)

@service_bp.route('/service', methods=['GET'])
def get_all_services():
    service_list = list(db['service'].find())
    return jsonify({'result': service_list}), 200

@service_bp.route('/service', methods=['POST'])
def create_service():
    data = request.json
    if data:
        item_id = str(db['service'].insert_one(data).inserted_id)
        return jsonify({'id': item_id}), 201
    else:
        return jsonify({'error': 'Data not provided'}), 400