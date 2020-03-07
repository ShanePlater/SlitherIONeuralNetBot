


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:/chromedriver')
driver.get("http://www.slither.io")

    
##nick
#//*[@id="nick"]
CSSSelector = '#nick'
usernameInput = driver.find_element_by_css_selector(CSSSelector)
usernameInput.send_keys('UnBayleefable')

playButton = '#playh'
playElement = driver.find_element_by_css_selector(playButton)
playElement.click()
actions = ActionChains(driver)


while(True):
    actions.move_by_offset(200,0) 
    actions.perform()
    actions.pause(5)
    actions.move_by_offset(0,200) 
    actions.perform()
    actions.pause(5)
    actions.move_by_offset(-200,0) 
    actions.perform()
    actions.pause(5)
    actions.move_by_offset(0,-200)
    actions.perform()
    actions.pause(5)


# class Wrapper(object):
# 	# Some static variables that we will use later

# 	def __init__(self):
# 		# Start the game
		
		
		


# 	def control(self, values):
# 		# This is the function that is called by the game.
# 		# The values dict contains important information
# 		# that we will need to use to train and predict

# 		# Do some work here

# 		# Finally, return the prediction

# 	def gameover(self, score):
# 		# The game has completed. Do cleanup stuff here
