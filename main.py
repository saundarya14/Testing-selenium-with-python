from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import re


class Main:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def check_xpath_exists(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def goTo(self):
        self.driver.get("https://www.thesparksfoundationsingapore.org/")
        self.driver.maximize_window()

        # checks if logo exists
        logo_xpath = '//*[@id="home"]/div/div[1]/h1/a/img'
        if (self.check_xpath_exists(logo_xpath)):
            print('Main logo exists')
        else:
            print('Couldnt find path of logo')

    def checkAboutUs(self):
        # go home
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="home"]/div/div[1]/h1/a'))).click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="link-effect-3"]/ul/li[1]/a'))).click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a'))).click()

        aboutUs = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[2]/div/div[2]/div/h4'))).get_attribute(
            'outerHTML')
        res = ''.join(re.findall(r'h4>(.+?)</h4', aboutUs[1:-1]))
        if res == "About Us":
            print("About Us typed correctly")

        vis = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                   '/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/p'))).get_attribute('outerHTML')

        res = ''.join(re.findall(r'p>(.+?)</p', vis))
        print("Vision: " + res)

    def displayContactInfo(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="link-effect-3"]/ul/li[6]/a'))).click()

        info = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                                    '/html/body/div[2]/div/div/div[3]/div[2]/p[2]'))).get_attribute(
            "outerHTML")

        res = ''.join(re.findall(r'<p>(.+?)</p>', info))
        res = res.split(',')
        print("Contact Number: " + res[0] + "\nMail: " + res[1])

    def joinUs(self):
        # go home
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="home"]/div/div[1]/h1/a'))).click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="link-effect-3"]/ul/li[5]/a'))).click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="link-effect-3"]/ul/li[5]/ul/li[2]/a'))).click()
        self.driver.execute_script("window.scrollTo(0, 500)")
        sleep(10)

        name_keys = 'enter your name here'
        name = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]')
        name.send_keys(name_keys)

        email_keys = 'enter your email here'
        mail = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]')
        mail.send_keys(email_keys)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[2]/div/div[2]/div[2]/div/form/select'))).click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[2]/div/div[2]/div[2]/div/form/select/option[2]'))).click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]'))).click()

        print(name_keys + ' registered successfully')

    def checkSocial(self):
        # go home
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '//*[@id="home"]/div/div[1]/h1/a'))).click()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # check fb
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[1]/a'))).click()
        sleep(10)
        print("Facebook checked")

        # switch to first tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        # check linkdin
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[2]/a'))).click()
        sleep(10)
        print("Linkdin checked")

        # switch to first tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        # check medium
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[3]/a'))).click()
        sleep(10)
        print("Medium checked")

        # switch to first tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        # check twitter
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[4]/a'))).click()
        sleep(10)
        print("Twitter checked")

        # switch to first tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        # check tsf
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[5]/a'))).click()
        sleep(10)
        print("TSF website checked")

        # switch to first tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        # check ig
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div[6]/div/div[1]/div[1]/div[1]/ul/li[6]/a'))).click()
        sleep(10)
        print("IG checked")

        # switch to first tab
        self.driver.switch_to.window(self.driver.window_handles[0])

    def tests(self):
        self.goTo()
        self.checkAboutUs()
        self.displayContactInfo()
        self.joinUs()
        self.checkSocial()
        self.driver.quit()


bot = Main()
bot.tests()

'''
elements:10
pages:5
'''
