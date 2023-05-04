from bs4 import BeautifulSoup
import requests

from errors import  error_handler, request_error_handler


class DataScraper:
    def __init__(self, url):
        self.url = url
        self.data = None

    @request_error_handler
    def get_content(self):
        content = requests.get(self.url).content
        return content

    @error_handler([TypeError])
    def scrape_data(self, selector):
        soup = BeautifulSoup(self.get_content(), "html.parser")
        data_element = soup.select(selector)
        self.data =  [data.text.strip() for data in data_element]
        

    


if __name__ == "__main__":
    scraper = DataScraper("https://www.worldometers.info/coronavirus/")
    print(scraper.get_content())
    scraper.scrape_data('.maincounter-number>span')
    print(scraper.data)
