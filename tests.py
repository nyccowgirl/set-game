from unittest import TestCase
from model import connect_to_db, db, example_data
from server import app
# from flask import session


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """To do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()  # TO DO: Create either in model.py or sep file

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    # def test_departments_list(self):
    #     """Test departments page."""

    #     result = self.client.get("/departments")
    #     self.assertIn("Legal", result.data)

    # def test_departments_details(self):
    #     """Test departments page."""

    #     result = self.client.get("/department/fin")
    #     self.assertIn("Phone: 555-1000", result.data)

    # def test_login(self):
    #     """Test login page."""

    #     result = self.client.post("/login",
    #                               data={"user_id": "rachel", "password": "123"},
    #                               follow_redirects=True)
    #     self.assertIn("You are a valued user", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()
