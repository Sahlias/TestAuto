from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Class.logger import Logger

logger = Logger()

class OpenClassroomsAutomation:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by, value):
        try:
            logger.log("info", f"Tentative de clic sur l'élément: {value}")
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((by, value)))
            element.click()
            logger.log("info", f"Clic réussi sur l'élément: {value}")
        except Exception as e:
            self.driver.save_screenshot(f"screenshot_{int(time.time())}.png")
            logger.log("error", f"Erreur lors du clic sur l'élément: {value}, Erreur: {e}")
            raise

    def send_keys(self, by, value, keys):
        try:
            logger.log("info", f"Tentative d'envoi de touches à l'élément: {value}")
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((by, value)))
            element.send_keys(keys)
            logger.log("info", f"Envoi de touches réussi à l'élément: {value}")
        except Exception as e:
            self.driver.save_screenshot(f"screenshot_{int(time.time())}.png")
            logger.log("error", f"Erreur lors de l'envoi de touches à l'élément: {value}, Erreur: {e}")
            raise

    def login(self, email, password):
        try:
            logger.log("info", "Début de la procédure de connexion")
            
            # Attendre que la superposition disparaisse
            # WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "oc-body is-connected")))

            logger.log("info", "Cliquer sur l'icône de connexion")
            self.click_element(By.XPATH, "//*[name()='svg' and @data-testid='ExpandMoreIcon']")
            time.sleep(5)

            logger.log("info", "Cliquer sur le bouton 'Se connecter'")
            self.click_element(By.XPATH, "//*[@id='main-header-menu']/a[2]/div/span")
            time.sleep(5)

            logger.log("info", "Saisir l'adresse email")
            self.send_keys(By.ID, "field-userEmail-1", email)
            self.send_keys(By.ID, "field-userEmail-1", Keys.ENTER)
            time.sleep(2)

            logger.log("info", "Cliquer sur le bouton 'Continuer'")
            # self.click_element(By.CSS_SELECTOR, "#submit")

            logger.log("info", "Saisir le mot de passe")
            self.send_keys(By.NAME, "_password", password)
            self.send_keys(By.NAME, "_password", Keys.ENTER)
            # self.click_element(By.ID,"login-button")
            logger.log("info", "Connexion réussie")

        except Exception as e:
            logger.log("error", f"Erreur lors de la connexion: {e}")
            print(f"Erreur lors de la connexion: {e}")
            self.driver.quit()
            raise

    def logout(self):
        try:
            logger.log("info", "Cliquer sur l'icône de compte")
            self.click_element(By.CSS_SELECTOR, "div[data-testid='avatar-root']")
            logger.log("info", "Etape reussie")
            time.sleep(2)

            logger.log("info", "Cliquer sur le bouton de déconnexion")
            self.click_element(By.CSS_SELECTOR,"div[data-testid='avatar-root']")
            logger.log("info", "Déconnexion réussie")
            time.sleep(2)

        except Exception as e:
            logger.log("error", f"Erreur lors de la déconnexion: {e}")
            print(f"Erreur lors de la déconnexion: {e}")
            self.driver.quit()
            raise
