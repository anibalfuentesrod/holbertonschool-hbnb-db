import json
import os
from models.user import User
from config import db

class DataManager:
    def __init__(self, use_database=False):
        self.use_database = use_database
        self.storage_file = 'data/storage.json'
        if not os.path.exists('data'):
            os.makedirs('data')

    def save(self, entity_type, entity_id, entity_data):
        if self.use_database:
            if entity_type == 'users':
                user = User(**entity_data)
                db.session.add(user)
                db.session.commit()
        else:
            data = self.load_storage()
            if entity_type not in data:
                data[entity_type] = {}
            data[entity_type][entity_id] = entity_data
            self.save_storage(data)

    def get(self, entity_type, entity_id):
        if self.use_database:
            if entity_type == 'users':
                return User.query.get(entity_id)
        else:
            data = self.load_storage()
            return data.get(entity_type, {}).get(entity_id)

    def update(self, entity_type, entity_id, entity_data):
        if self.use_database:
            if entity_type == 'users':
                user = User.query.get(entity_id)
                if user:
                    for key, value in entity_data.items():
                        setattr(user, key, value)
                    db.session.commit()
        else:
            data = self.load_storage()
            if entity_type in data and entity_id in data[entity_type]:
                data[entity_type][entity_id] = entity_data
                self.save_storage(data)

    def delete(self, entity_type, entity_id):
        if self.use_database:
            if entity_type == 'users':
                user = User.query.get(entity_id)
                if user:
                    db.session.delete(user)
                    db.session.commit()
        else:
            data = self.load_storage()
            if entity_type in data and entity_id in data[entity_type]:
                del data[entity_type][entity_id]
                self.save_storage(data)

    def get_all(self, entity_type):
        if self.use_database:
            if entity_type == 'users':
                return User.query.all()
        else:
            data = self.load_storage()
            return list(data.get(entity_type, {}).values())

    def save_storage(self, data):
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=4)

    def load_storage(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        return {}

# Initialize DataManager instance
data_manager = DataManager(use_database=True)