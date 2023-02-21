from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import wordfind
from time import sleep

url = "https://jklm.fun"

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# enter the room code
roomcode = input("Enter room code: ").upper()
roomInput = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[2]/div[1]/form/div/input")
roomInput.send_keys(roomcode)
roomInput.send_keys(Keys.ENTER)

# enter the username
nickname = input("Enter nickname: ")
nicknameInput = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/input")
nicknameInput.send_keys(nickname)
nicknameInput.send_keys(Keys.ENTER)

# waits until join game button is shown and clicks it
#found = False
#while found == False:
#  sleep(1.5)
#  findiFrame = driver.find_elements(By.XPATH, #"/html/body/div[2]/div[4]/div[1]/iframe")
#  if len(findiFrame) > 0:
#    found = True

input("Press ENTER when loaded")

iframe = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/iframe")
driver.switch_to.frame(iframe)

joinButton = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/button")
joinButton.click()

# checks if the input box is displayed
def checkIfTurn():
  check = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
  return check.is_displayed()

wordInput = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[2]/form/input")

while 1:
  sleep(0.2)
  if checkIfTurn() == True:
    syllable = driver.find_element(By.CLASS_NAME, "syllable").text
    word = wordfind.find(syllable.lower())
    print(word)
    wordInput.send_keys(word)
    wordInput.send_keys(Keys.ENTER)