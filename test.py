import unittest
from main import app, db, User

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        response = self.app.post('/add_user', data={'username': 'test_user'})
        self.assertEqual(response.status_code, 302)  # Redirect status code

        users = User.query.all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, 'test_user')

if __name__ == '__main__':
    unittest.main()

