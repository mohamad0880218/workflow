import unittest
from main import app, db, User

class TestApp(unittest.TestCase):

    def setUp(self):
        # Use a separate test database
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()

        # Initialize the app context and create the test database
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop the test database after the tests
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        response = self.app.post('/add_user', data={'username': 'test_user'})
        self.assertEqual(response.status_code, 302)  # Redirect status code

        # Ensure the user was added to the test database
        with app.app_context():
            users = User.query.all()
            self.assertEqual(len(users), 1)
            self.assertEqual(users[0].username, 'test_user')

if __name__ == '__main__':
    unittest.main()

