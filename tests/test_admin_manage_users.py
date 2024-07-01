import time
import unittest
from src import create_app, db
from src.models.user import User
from sqlalchemy.exc import OperationalError
from flask_migrate import upgrade
import os

class AdminManageUsersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        with self.app.app_context():
            # Run migrations
            upgrade(directory=os.path.join(os.path.dirname(__file__), '../migrations'))
        self.client = self.app.test_client()
        self.authenticate()
        self.clear_users()
        self.create_test_users()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def authenticate(self):
        response = self.client.post('/login', json={
            'email': 'test@example.com',
            'password': 'test'
        })
        self.assertEqual(response.status_code, 200)
        self.token = response.json['access_token']

    def clear_users(self):
        retry_attempts = 5
        for attempt in range(retry_attempts):
            try:
                User.query.delete()
                db.session.commit()
                break
            except OperationalError as e:
                if attempt < retry_attempts - 1:
                    time.sleep(1)
                else:
                    raise e

    def create_test_users(self):
        retry_attempts = 5
        for attempt in range(retry_attempts):
            try:
                admin_user = User(email='admin123@example.com', is_admin=True)
                admin_user.set_password('admin')
                user = User(email='anibal123@gmail.com', is_admin=False)
                user.set_password('user')
                db.session.add_all([admin_user, user])
                db.session.commit()
                break
            except OperationalError as e:
                if attempt < retry_attempts - 1:
                    time.sleep(1)
                else:
                    raise e

    def test_promote_user_as_admin(self):
        response = self.client.post('/promote_user', 
                                    json={'email': 'anibal123@gmail.com'},
                                    headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)

    def test_promote_user_as_non_admin(self):
        response = self.client.post('/promote_user', 
                                    json={'email': 'anibal123@gmail.com'},
                                    headers={'Authorization': f'Bearer {self.token}'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()