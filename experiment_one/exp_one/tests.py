from selenium import webdriver
from django.test import TestCase

class HomePageTests(TestCase):

    # User goes to www.gavmac.com
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000')

    def tearDown(self):
        self.driver.close()

    # User expects to see Home in title
    def test_home_in_title_of_default_route(self):
        self.assertIn("Home", self.driver.title)

    # User expects to see a username and password box with Login button
    def test_login_form_exists_on_page(self):
        self.driver.find_element_by_class_name('container')

