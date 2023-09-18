import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import datetime
from tkinter import *
from tkinter import messagebox
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Crawler():

    def getUserPosts(self, user):
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        url = "https://www.tiktok.com/"
        driver.get(url)
        time.sleep(3)

        try:
            feld = driver.find_element(By.XPATH, "//*[@id='app-header']/div/div[2]/div/form/input")
            feld.send_keys(user)
            time.sleep(2)
        except:
            print("Problem mit Suchfeld ist aufgetaucht")

        try:
            suchen_button = driver.find_element(By.XPATH, "//*[@id='app-header']/div/div[2]/div/form/button")
            suchen_button.click()
            time.sleep(3)
        except:
            print("Suchen Button konnte nicht geklickt werden")

        try:
            konto = driver.find_element(By.XPATH, '//*[@id="tabs-0-panel-search_top"]/div/div/div[1]/div[2]/a[2]/p[1]')
            time.sleep(1.5)
            driver.execute_script("window.scrollTo(0, 968)")
            time.sleep(0.8)
            driver.execute_script("window.scrollTo(0, 0);")
            konto.click()
        except:
            print("Konto konnte nicht gefunden werden")
        print("Konto gefunden")

        time.sleep(10)