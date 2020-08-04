# Web Page scrapper
# This program is to extract images from the depth map images from the website
# and then store it in the folder from which we can collect the necessary depth data

# Library Imports
import os
import time             # Used to pause after certain commands to ensure that each command is completely processed
from selenium import webdriver              # Selenium is used for opening the browser and carrying out actions in it
from selenium.webdriver.firefox.options import Options
import pyautogui                # Pyautogui helps with onscreeen clicks and typing and overall location on buttons

# Setting up folder


#pyautogui.PAUSE = 5             # All pyautogui function calls will wait 5 secs after the previous function call
# Using firefox browser for the scraping
options = Options()
options.set_preference('browser.download.folderList', 2)
options.set_preference('browser.download.dir','C:\Games\captured_images')
options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/png')
driver = webdriver.Firefox(executable_path='C:\Windows\geckodriver.exe',firefox_options=options)
driver.get('https://www.photopea.com')
x_butt = pyautogui.locateOnScreen('close.png', confidence=0.5)              # Will locate the close button for a in-web message to close it
                                                                            # Here pyautogui is used since the in-web message does not have an XPath
x_point = pyautogui.center(x_butt)                                          # Allows us to find the center of the button that we need to click
x_px, x_py = x_point                                                        # saving x and y coordinates of the button on the screen
pyautogui.click(x_px, x_py)

# Uploading image
open_butt = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/div[2]/div/div[2]/div/ul/li[2]/button")
open_butt.click()
time.sleep(3)
pyautogui.write('C:\Documents\image.jpg')
pyautogui.press('enter')

# Checking depth map
time.sleep(15)
layer_butt = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div[1]/span/button[4]')
layer_butt.click()
del_butt = pyautogui.locateOnScreen('plah.png', confidence= 0.5)
print(del_butt)
del_point = pyautogui.center(del_butt)
print(del_point)
del_x, del_y = del_point
time.sleep(5)
pyautogui.click(del_x, del_y)

# Saving image
save_butt = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[2]/span[4]/button[1]')
save_butt.click()


