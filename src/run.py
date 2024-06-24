from flask import Flask, jsonify, request, make_response
from config import Config, db
from data_manager import DataManager
from models.user import User
import uuid
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()  # Create tables for our models

data_manager = DataManager(use_database=app.config['USE_DATABASE'])

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'GET':
        users = data_manager.get_all('users')
        return jsonify([user.to_dict() for user in users]) if app.config['USE_DATABASE'] else jsonify(users)

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'email' not in data or 'first_name' not in data or 'last_name' not in data:
            return make_response(jsonify({'error': 'Missing required fields'}), 400)
        data['id'] = str(uuid.uuid4())
        data['created_at'] = data['updated_at'] = datetime.now().isoformat()
        data_manager.save('users', data['id'], data)
        return make_response(jsonify(data), 201)

if __name__ == '__main__':
    app.run(debug=True)