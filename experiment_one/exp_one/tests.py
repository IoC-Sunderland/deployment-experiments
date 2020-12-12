from selenium import webdriver
from django.test import TestCase

class AppInitialisationTests(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_home_in_title_of_default_route(self):
        self.driver.get('http://127.0.0.1:8000')
        self.assertIn("Home", self.driver.title)
