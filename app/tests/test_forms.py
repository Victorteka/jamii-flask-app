import unittest
from app.forms.forms import LoginForm, RegisterForm, BusinessesForm

class TestForm(unittest.TestCase):
    def setUp(self):
        self.login = LoginForm()
        self.register = RegisterForm()
        self.business = BusinessesForm()

