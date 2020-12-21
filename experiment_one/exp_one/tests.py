from selenium import webdriver
from django.test import TestCase
import time

DELAY = 2

class HomePageTests(TestCase):

    # Gavin goes to www.gavmac.com
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5000')

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

    # Gavin expects to be able to re-enter a username and password if both fields are empty 
    # when Login button clicked
    def test_message_shown_if_username_AND_password_empty_when_login_button_clicked(self):
        username = self.driver.find_element_by_id('username')
        password = self.driver.find_element_by_id('password')
        username.clear()
        password.clear()
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        message = self.driver.find_element_by_class_name('warning')
        self.assertEqual(message.text, 'Missing fields for username, password')

    # Gavin expects to be able to re-enter a username if field was empty 
    # when Login button clicked
    def test_message_shown_if_username_field_is_empty_when_login_button_clicked(self):
        username = self.driver.find_element_by_id('username')
        username.clear()
        password = self.driver.find_element_by_id('password')
        password.send_keys('TestPass')
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        message = self.driver.find_element_by_class_name('warning')
        self.assertEqual(message.text, 'Missing fields for username')
    
    # Gavin expects to be able to re-enter a password if field was empty 
    # when Login button clicked
    def test_message_shown_if_password_field_is_empty_when_login_button_clicked(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('Gavin')
        password = self.driver.find_element_by_id('password')
        password.clear()
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        message = self.driver.find_element_by_class_name('warning')
        self.assertEqual(message.text, 'Missing fields for password')

    
    # Given a valid username and password are provided then 
    # Gavin expects to see the Welcome page when the Login button is clicked
    # Welcome page includes bespoke message welcoming Gavin
    def test_welcome_page_displayed_when_login_details_valid(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('Gavin')
        password = self.driver.find_element_by_id('password')
        password.send_keys('TestPass')
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        time.sleep(DELAY)
        welcome_message = self.driver.find_element_by_id('welcomeMessage')
        self.assertEqual(welcome_message.text, 'Welcome, Gavin!')

    # Gavin provides correct username but incorrect password and expects to be 
    # able to re-enter credentials to enable login
    def test_message_shown_if_credentials_are_not_authenticated_when_login_button_clicked(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('Gavin')
        password = self.driver.find_element_by_id('password')
        password.send_keys('InvalidPassword')
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        invalid_credentials_message = self.driver.find_element_by_class_name('warning')
        self.assertEqual(invalid_credentials_message.text, \
            'Invalid Credentials')
    

    # Susan is a new user to www.gavmac.com and expects to a 'Invalid Credentials'
    # message when she trys to login. She then expects to see a sign up page when she clicks
    # "Sign Up" button.
    # After entering ddetails she expects to see a Welcome page after clicking "Sign Up" button.
    def test_error_page_displayed_when_login_details_invalid(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('Susan')
        password = self.driver.find_element_by_id('password')
        password.send_keys('SusanTestPass')
        login_button = self.driver.find_element_by_id('submit')
        login_button.click()
        time.sleep(DELAY)
        invalid_credentials_message = self.driver.find_element_by_class_name('warning')
        self.assertEqual(invalid_credentials_message.text, \
            'Invalid Credentials')
        username = self.driver.find_element_by_id('username')
        username.clear()
        password = self.driver.find_element_by_id('password')
        password.clear()
        signup_button = self.driver.find_element_by_id('signup')
        signup_button.click()
        time.sleep(DELAY)
        self.assertIn("Sign Up", self.driver.title)
        username = self.driver.find_element_by_id('username')
        username.clear()
        email = self.driver.find_element_by_id('email')
        email.clear()
        password = self.driver.find_element_by_id('password')
        password.clear()
        username.send_keys('Susan')
        email.send_keys('susan@susan.com')
        password.send_keys('SusanTestPass')
        time.sleep(DELAY)
        signup_button = self.driver.find_element_by_id('signup')
        signup_button.click()
        welcome_message = self.driver.find_element_by_id('welcomeMessage')
        self.assertEqual(welcome_message.text, 'Welcome, Susan!')
         
        

    # Susan expects to be able to see a sign up page after she clicks on 'Sign Up;
    # button
    def test_sign_up_button_renders_sign_up_pages(self):
        username = self.driver.find_element_by_id('username')
        username.clear()
        password = self.driver.find_element_by_id('password')
        password.clear()
        signup_button = self.driver.find_element_by_id('signup')
        signup_button.click()
        time.sleep(DELAY)
        self.assertIn("Sign Up", self.driver.title)

        