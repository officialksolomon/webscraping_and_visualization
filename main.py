from scraping import DataScraper
from storage import DataStorage
from visualization import PieChartVisualizer
import config

def main():
    # scrape data 
    scraper = DataScraper(config.URL)
    scraper.scrape_data(config.CSS_SELECTOR)
    # save data
    csv_store = DataStorage(config.FILE_NAME)
    print(scraper.data)
    csv_store.get_data(scraper.data)
    csv_store.store_data(config.DATA_COLUMNS)
    # visualize data
    visualizer =  PieChartVisualizer()
    visualizer.get_data(config.FILE_NAME + config.FORMAT)
    visualizer.visualize_data()


if __name__ == "__main__":
    main()
