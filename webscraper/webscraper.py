import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import scrapy
from selenium import webdriver
import sys
# https://medium.com/analytics-vidhya/counter-strike-matches-result-prediction-537f8648ee7f
class Webscraper:

    def __init__(self):
        self.driver=webdriver.Chrome()
        self. matchesLinks = []

    def scrape_results_page(self, pages):
        """

        """

        page = 0
       
        try:
            while page <= pages:
                self.driver.get('https://www.hltv.org/results?offset='+str(page))
                
                content = self.driver.page_source
                soup = BeautifulSoup(content, features="lxml")
                
                for div in soup.findAll('div', attrs={'class':'results'}):
                    for a in div.findAll('a', attrs={'class':'a-reset'}):
                        link = a['href']

                        if self.is_valid_match_url(link):
                            self.matchesLinks.append(link)
                        else:
                            continue


    
                page += 100

            # return matchesLinks

        except Exception as e:
            print(e)
    
    def is_valid_match_url(self, link):
        """
            Checks whether the scraped link starts with /matches/ which makes it syntactically valid.

            Parameters:
                link (str): Ingoing link with 

            Returns:
                Boolean
        """
        try:
            if link.startswith('/matches/', 0):
                return True
            return False
        except TypeError as e:
            print("Encountered type error:", sys.exc_info()[0])
            raise(TypeError)
        except Exception as e:
            print("Encountered unknown error:", sys.exc_info()[0])
            raise(Exception)





    
class match:
    pass
    # def __init__(self):




if __name__=='__main__':
    ws = Webscraper()
    ws.scrape_results_page(99)