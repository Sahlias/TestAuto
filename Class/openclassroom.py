from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from Class.logger import Logger

logger = Logger()

class OpenClassRoomsActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        

    def search_words(self, words) :
        try :
            search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.dom-services-2-dom-services100.dom-services-2-dom-services102")))
            # Vous pourriez avoir besoin de cliquer sur le champ avant d'envoyer des clés
          
            search_button.click()
            logger.log("log-openclassrooms", f"Vous avez cliqué sur le bouton de recherche")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur lors du clique sur le bouton de recherche : {e}")

        time.sleep(5)  
            
        try:    
            
            search_field = self.wait.until(EC.element_to_be_clickable((By.ID,'algolia-search-input')))
            # Vous pourriez avoir besoin de cliquer sur le champ avant d'envoyer des clés
            search_field.click()
            
            # Effacer le champ avant de taper pour éviter des problèmes de texte pré-rempli
            search_field.clear()
            search_field.send_keys(words)
            search_field.send_keys(Keys.ENTER)               
            logger.log("log-openclassrooms", f"Vous d'éffectuer la recherche sur le mots: {words}")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur la recherche a échoué : {e}")

    def selected_course(self):
        try: 
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainSearch"]/div/div/div/ul/li[3]/a/div/div/div/div')))
            # Vous pourriez avoir besoin de cliquer sur le champ avant d'envoyer des clés
            search_button.click()
                
            logger.log("log-openclassrooms", f"Vous avez selectionné le 3 ème élément de la liste de recherche")
        except Exception as e:
            logger.log("error-openclassrooms", f"Erreur lors de la selectionnion du 3 ème élément de la liste de recherche : {e}")