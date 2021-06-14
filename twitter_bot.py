from selenium import webdriver
import time
from creds import MY_EMAIL, MY_PASS
class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_driver_path = "E:\Documentos\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.UP = 10
        self.DOWN = 15

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net")
        time.sleep(10)
        self.driver.find_element_by_xpath("""//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]""").click()
        time.sleep(60)
        self.download_speed = self.driver.find_element_by_xpath("""//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span""").text
        self.download_speed_number = int(self.download_speed.split(".")[0])
        self.upload_speed = self.driver.find_element_by_xpath("""//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span""").text
        self.upload_speed_number = int(self.upload_speed.split(".")[0])

        return self.download_speed_number, self.upload_speed_number

    def tweet_at_provider(self):
        if self.download_speed_number < 15:
            self.driver.get("https://twitter.com")
            time.sleep(5)
            self.driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div""").click()
            time.sleep(5)
            self.email = self.driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input""")
            self.email.send_keys(MY_EMAIL)
            self.senha = self.driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input""")
            self.senha.send_keys(MY_PASS)
            self.driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div""").click()
            time.sleep(5)
            search = self.driver.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div""")

            search.send_keys(f"Hey @internet_provider, my current download speed is {self.download_speed_number}mb/s and my upload speed is {self.upload_speed_number}mb/s and they should be xxxx")
