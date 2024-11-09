from selenium import webdriver

def get_drvier():

#Set options to make browsing easier

    options =  webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink- features = AutomationControlled")



    driver = webdriver.Chrome(options=options)

    driver.get("http://automated.pythonanywhere.com")

    return driver



def main():
    driver = get_drvier()
    element = driver.find_element (by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())



#webdriver is a part of the Selenium library used to control the browser (like Chrome, Firefox) programmatically.




# Automatic script for login into a website
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def get_drvier():

#Set options to make browsing easier

    options =  webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink- features = AutomationControlled")



    driver = webdriver.Chrome(options=options)

    driver.get("http://automated.pythonanywhere.com/login/")

    return driver



def main():
    driver = get_drvier()

    driver.find_element (by="id", value="id_username").send_keys("automated")
    #Here automated is the username when you login into this site
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated"+ Keys.RETURN)
    #here automatedautomated is the password we want to login with
    #Keys.RETURN this is added for 'enter' key usually for login we press enter for login
    print("Eneterd automaically your username and pswd")
    print(driver.current_url)


#Now after login we want to press home button
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    print("Current UrL now is",driver.current_url)
print(main())












