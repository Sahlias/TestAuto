from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Class.logger import Logger

logger = Logger()

class CookieHandler:
    def __init__(self, driver):
        self.driver = driver
        
    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "truste-consent-button"))
            ).click()
            logger.log("log-openclassroom", "Les cookies ont bien été acceptés")
        except Exception as e:
            logger.log("error-openclassroom", f"Erreur lors de l'acceptation des cookies : {e}")
            
    def decline_cookies(self):
        try:
            decline_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/shreddit-app/shreddit-async-loader[2]/reddit-cookie-banner//div/shreddit-interactable-element[2]/button/span/span"))
            )
            decline_button.click()
            logger.log("log-openclassroom", "Les cookies ont bien été refusés")
        except Exception as e:
            logger.log("error-openclassroom", f"Erreur lors du refus des cookies : {e}")
