from selenium import webdriver
from django.test import TestCase
import time

DELAY = 2

class HomePageTests(TestCase):

    # Gavin goes to www.gavmac.com
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000')

    def tearDown(self):
        self.driver.close()

    # Gavin expects to see Home in title
    def test_home_in_title_of_default_route(self):
        self.assertIn("Home", self.driver.title)

    # Gavin expects to see a username and password box with Login button
    def test_login_form_exists_on_page(self):
        self.driver.find_element_by_id('username')
        self.driver.find_element_by_id('password')
        self.driver.find_element_by_id('submit')
    
    # Gavin expects to be able to enter username and password
    def test_able_to_enter_username_and_password(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('Gavin')
        password = self.driver.find_element_by_id('password')
        password.send_keys('TestPass')
        time.sleep(DELAY)

    def test_message_shown_if_username_AND_password_empty_when_login_button_clicked(self):
        username = self.driver.find_element_by_id('username')
        password = self.driver.find_element_by_id('password')
        username.clear()
        password.clear()
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        message = self.driver.find_element_by_class_name('warning')
        self.assertEqual(message.text, 'Missing fields for username, password')

    def test_message_shown_if_username_field_is_empty_when_login_button_clicked(self):
        username = self.driver.find_element_by_id('username')
        username.clear()
        password = self.driver.find_element_by_id('password')
        password.send_keys('TestPass')
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        message = self.driver.find_element_by_class_name('warning')
        self.assertEqual(message.text, 'Missing fields for username')
    
    def test_message_shown_if_password_field_is_empty_when_login_button_clicked(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('Gavin')
        password = self.driver.find_element_by_id('password')
        password.clear()
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        message = self.driver.find_element_by_class_name('warning')
        self.assertEqual(message.text, 'Missing fields for password')