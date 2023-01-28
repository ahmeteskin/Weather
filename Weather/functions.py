import values
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Weather(webdriver.Chrome):
    def __init__(self, t = True):
        super(Weather, self).__init__()
        self.city = values.inp
        self.t = t

    def onoff(self):

        return self.t
    def opener(self):
        self.get("https://www.msn.com/en-us/weather/forecast/")
        self.implicitly_wait(15)
        self.maximize_window()

    def enter_values(self):
        self.implicitly_wait(15)
        try:
            i = self.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for location"]')
            i.click()
            i.send_keys(values.inp)
        except:

            i = self.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for location"]')
            i.click()
            i.send_keys(values.inp)


        try:
            self.find_element(By.XPATH, "//*[@id=\"m-locs\"]/div/div/div/div/div/span/div/div[1]")
            print("Location not found")
            self.t = False

        except:
         try:
            b = self.find_element("id", "locationSuggestions_0")
            b.click()
         except:
            b = self.find_element("xpath", "//*[@id=\"m-locs\"]/div/div/div/button[2]/span/svg/path")
            b.click()
        time.sleep(3)

    def get_values(self):
        self.implicitly_wait(15)
        q = self.find_element("xpath", "//*[@id=\"OverviewCurrentTemperature\"]/a")
        a = q.text.split()
        m = "".join(a)
        self.m = m
        q = self.find_element("xpath", "//*[@id=\"WeatherOverviewLocationName\"]/a").text
        self.q = q

    def convert(self):
            a = self.m.split("°")
            cel = (int(a[0]) - 32) * (5 / 9)
            print(f"""
Temperature of {self.q} in Celsius: {cel}‎°C
Temperature of {self.q} in Fahrenheit: {self.m}""")

    def exit(self):
        self.close()

