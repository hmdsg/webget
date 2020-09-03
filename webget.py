from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary
import time

DIST_URL = ""
IGNORE_TEXT = ""

class GetNet:

    def __init__(self):
        self.url = DIST_URL
        self.driver = webdriver.Chrome()

    def main(self):        
        self.driver.get(self.url)
        html = self.driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, "html.parser")

        if soup.find("h1") is not None:
            h1_text = soup.find("h1").text
        else:
            h1_text = "nothing"


        if h1_text == IGNORE_TEXT:
            return True
        else:
            return False

        


if __name__=='__main__':
    d = GetNet()
    
    while d.main():
        time.sleep(3)