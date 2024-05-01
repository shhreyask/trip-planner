from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
class WebDriver:

  location_data = {}

  def __init__(self):

    self.PATH = "chromedriver.exe"
    self.options = Options()
#   Try adding this line if you get the error of chrome chrashed
#   self.options.binary_location = "C:/Program Files (x86)/Google/Chrome/Applic>
    self.options.add_argument("--headless")
    self.driver = webdriver.Chrome(options=self.options)

    self.location_data["rating"] = "NA"

  def get_location_data(self):

    try:
      avg_rating = self.driver.find_element(By.CLASS_NAME, "F7nice")

    except:
      pass

    try:
      self.location_data["rating"] = avg_rating.text[0:3]

    except:
      pass
      

  def scrape(self, url): # Passed the URL as a variable
    try:
      self.driver.get(url) # Get is a method that will tell the driver to open at that particular URL

    except Exception as e:
      self.driver.quit()
      return

    time.sleep(10) # Waiting for the page to load.
    self.get_location_data()

    self.driver.quit() # Closing the driver instance.

    return(self.location_data)
  

url = "https://www.google.com/maps/place/Empire+State+Building/@40.7484405,-73.9882393,17z/data=!3m2!4b1!5s0x8b398fecd1aea119:0x76fa1e3ac5a94c70!4m6!3m5!1s0x89c259a9b3117469:0xd134e199a405a163!8m2!3d40.7484405!4d-73.9856644!16zL20vMDJuZF8?entry=ttu"
x = WebDriver()
print(x.scrape(url))