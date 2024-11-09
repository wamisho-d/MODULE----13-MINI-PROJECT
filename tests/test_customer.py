import unittest
from app import app, db
from models.customer import Customer

class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_create_customer(self):
        response = self.app.post('/customer', json={
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '123-456-7890'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_customer(self):
        customer = Customer(name="Jane Doe", email="jane.doe@example.com", phone_number="098-765-4321")
        db.session.add(customer)
        db.session.commit()
        
        response = self.app.get(f'/customer/{customer.id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], "Jane Doe")

if __name__ == '__main__':
    unittest.main()
