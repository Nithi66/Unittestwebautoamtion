# #########################################
# Test Case = Valid Submission Flow on Contact us page

# Objective: Ensure that the form accepts valid input and displays a success message..
# Main Steps:
# 1. Open the chrome browser
# 2. Navigate to https://www.qs.com/contact-us/
# 3. Fill all the mandatary fields.
# 4. Click on submit.
# 5. And capture the below success message using TestNG assertion mechanism.

######Remainining#####
# Click on 'Submit' cannot be performed as Captcha should be handled by Admin only and error is Occuring only
#Admins has the rights.
# Required Success message could not be captured as it dependent on Step 4

# Author: Asha M
# Date: June 15th, 2025
################################
#
# Copyright 2025 QS Quacquarelli Symonds,Bangalore
#
###############################

# #########################################
# Test Case = Valid Submission Flow on Contact us page

# Objective: Ensure that the form accepts valid input and displays a success message..
# Main Steps:
# 1. Open the Chrome browser
# 2. Navigate to https://www.qs.com/contact-us/
# 3. Fill all the mandatary fields.
# 4. Click on submit.
# 5. And capture the below success message using TestNG assertion mechanism.

######Remainining#####
# Click on 'Submit' button cannot be performed as Captcha should be handled by Admin only and error is Occuring only
#Admins has the rights.
# Required Success message could not be captured as it dependent on Step 4

# Author: Asha M
# Date: June 15th, 2025
################################
#
# Copyright 2025 QS Quacquarelli Symonds,Bangalore
#
###############################
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestQSContactUs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.maximize_window()
        cls.driver.get("https://www.qs.com/contact-us/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_accept_cookies(self):
        """Accept cookies on the QS website"""
        accept_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "hs-eu-confirmation-button")))

        self.driver.execute_script("arguments[0].scrollIntoView();", accept_button)
        self.driver.execute_script("arguments[0].click();", accept_button)
        iframe = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//iframe[starts-with"
                                                                       "(@id, 'hs-form-iframe')]")))

        self.driver.switch_to.frame(iframe)

    def test_fill_candidate_details(self):
        """Fill the details with the candidate"""
        self.driver.find_element(By.NAME, "firstname").send_keys("Asha")
        self.driver.find_element(By.NAME, "lastname").send_keys("M")
        dropdown = self.driver.find_element(By.NAME, "country")
        select = Select(dropdown)
        select.select_by_visible_text("India")
        self.driver.find_element(By.NAME, "email").send_keys("asham23keshav@QS.COM")
        self.driver.find_element(By.NAME, "jobtitle").send_keys("Software tester")
        self.driver.find_element(By.NAME, "company").send_keys("QS Organisation")

    def test_select_interests(self):
        """Select the interests"""
        self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='digital_innovation']").click()

    def test_agree_to_communications(self):
        """Agree to receive communications"""
        self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @name='LEGAL_CONSENT.subscription_type_163138980']").click()

    def test_send_message_to_qs(self):
        """Send a message to QS"""
        send_message = "Hello Im excited to join QS Family"
        self.driver.find_element(By.NAME, "message_to_qs").send_keys(send_message)

    '''def test_click_submit_button(self):
        """Submit the button"""
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()'''

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)




'''dropdown = driver.find_element(By.CLASS_NAME, "category-select")
select = Select(dropdown)
select.select_by_value("qs-news")

#getdate = driver.find_element(By.ID, "published_date_container401065")
f = driver.find_element(By.XPATH, "//a[contains(text(), 'Mark your calendars: Key QS dates for 2025')]")
driver.execute_script("arguments[0].scrollIntoView();", f)
f.click()'''