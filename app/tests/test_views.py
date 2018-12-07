import unittest
from app import app


class TestViews(unittest.TestCase):

    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)

    #ensures login page behaves correctly
    def test_login(self):
        tester = app.test_client(self)
        resp = tester.get('/login', content_type ='html/text')
        self.assertEqual(resp.status_code, 200)

    #ensure register page behaves correctly
    def test_register(self):
        tester = app.test_client(self)
        resp = tester.get('/register', content_type ='html/text')
        self.assertTrue(b'Register for an Account' in resp.data)

    #ensures home page display right content
    def test_home_page_display_correct_content(self):
        tester = app.test_client(self)
        resp = tester.get('/', content_type ='html/text')
        self.assertTrue(b'Welcome to Jamii website' in resp.data)
    
    #ensures that you are logged in before accessing register business route
    def test_register_business_route_require_login(self):
        tester = app.test_client(self)
        resp = tester.get('/businesses', follow_redirects = True)
        self.assertEqual(resp.status_code, 200)

    #ensures to logout you must have logged in first
    def test_logout_require_login(self):
        tester = app.test_client(self)
        resp = tester.get('/logout', follow_redirects = True)
        self.assertEqual(resp.status_code, 200)     