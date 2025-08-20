from selenium import webdriver
import os

def startbot(username,password,url):
    path = "C:\\Users\\hp\\Downloads\\chromedriver"


    driver=webdriver.Chrome(path)

    driver.get(url)

    driver.find_element_by_name("id/class/name_of_username").send_keys(username)

    driver.element