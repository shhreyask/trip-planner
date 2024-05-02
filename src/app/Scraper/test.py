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

  rating=""

  def __init__(self):

    self.PATH = "chromedriver.exe"
    self.options = Options()
#   Try adding this line if you get the error of chrome chrashed
#   self.options.binary_location = "C:/Program Files (x86)/Google/Chrome/Applic>
    self.options.add_argument("--headless")
    self.driver = webdriver.Chrome(options=self.options)
    self.rating = "NA"

  def get_location_data(self, name, ratings):

    try:
      avg_rating = self.driver.find_element(By.CLASS_NAME, "F7nice")

    except:
      pass

    try:
      ratings[name] = avg_rating.text[0:3]

    except:
      pass
      

  def scrape(self, url, ratings): # Passed the URL as a variable
    try:
      for name in url:
        self.driver.get(url[name]) # Get is a method that will tell the driver to open at that particular URL
        time.sleep(4)
        self.get_location_data(name, ratings)

    except Exception as e:
      self.driver.quit()
      return
    
    self.driver.quit()# Closing the driver instance.
  

def url_maker(name):
  formatted_name = name.replace(" ", "+")
  url = f"https://www.google.com/maps/search/{formatted_name}"
  return url

poi = ["Jehangir Art Gallery", "Empire state Building", "Pvr xperia dombivli"]
url = {}
ratings={}

for name in poi:
  url[name] = url_maker(name)

x = WebDriver()
x.scrape(url, ratings)

# for i in range(0 , len(poi)):
#     ratings[poi[i]] = x.scrape(url[poi[i]], ratings)

#print(ratings)
  
