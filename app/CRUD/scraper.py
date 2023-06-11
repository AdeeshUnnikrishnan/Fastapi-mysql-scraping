from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
from app.config.database import db_connect 


class BulkDealScraper:
    def __init__(self):
        self.driver = None
        self.df = pd.DataFrame(columns=['dealDate', 'securityCode', 'securityName', 'clientName', 'dealType',
                                        'quantity', 'price'])

    def setup_driver(self):
        options = Options()
        options.add_argument("--headless")
        # Set up the Chrome driver (you will need to download chromedriver and provide the path)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    def scrape_data(self):
        # Open the website
        url = 'https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx'
        self.driver.get(url)

        for i in range(2, 70):
           # elements = self.driver.find_element("xpath",f'/html/body/form/div[4]/div/div/div[3]/div/div/table/tbody/tr/td/div/table/tbody/tr[{i}]')
            dealDate = self.driver.find_element("xpath",f'/html/body/form/div[4]/div/div/div[3]/div/div/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[1]')
            securityCode = self.driver.find_element("xpath",f'/html/body/form/div[4]/div/div/div[3]/div/div/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[2]')
            securityName = self.driver.find_element("xpath",f'/html/body/form/div[4]/div/div/div[3]/div/div/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[3]')
            clientName = self.driver.find_element("xpath",f'/html/body/form/div[4]/div/div/div[3]/div/div/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[4]')
            dealType = self.driver.find_element("xpath",f'/html/body/form/div[4]/div/div/div[3]/div/div/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[5]')
            quantity = self.driver.find_element("xpath",f'/html/body/form/div[4]/div/div/div[3]/div/div/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[6]')
            price = self.driver.find_element("xpath",f'/html/body/form/div[4]/div/div/div[3]/div/div/table/tbody/tr/td/div/table/tbody/tr[{i}]/td[7]')

            new_data = {'dealDate': f"{dealDate.text}",
                        'securityCode': f"{securityCode.text}",
                        'securityName': f"{securityName.text}",
                        'clientName': f"{clientName.text}",
                        'dealType': f"{dealType.text}",
                        'quantity': f"{quantity.text}",
                        'price': f"{price.text}"
                        }

            self.df = pd.concat([self.df, pd.DataFrame(new_data, index=[i])], ignore_index=True)
            self.df['quantity'] = self.df['quantity'].str.replace(',', '')

    def display_data(self):
        print(self.df)

    def add_data(self):
        db_connect(self.df)

    def quit_driver(self):
        self.driver.quit()


def main():
    scraper = BulkDealScraper()
    scraper.setup_driver()
    scraper.scrape_data()
    scraper.display_data()
    scraper.add_data()
    scraper.quit_driver()
