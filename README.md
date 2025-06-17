    def launch_chrome(self,url):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get(url)

    def handle_browser_cookies(self):

        accept_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.ID, "hs-eu-confirmation-button")))
        self.driver.execute_script("arguments[0].scrollIntoView();", accept_button)
        self.driver.execute_script("arguments[0].click();", accept_button)
