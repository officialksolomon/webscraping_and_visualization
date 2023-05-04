from abc import ABC, abstractmethod
import pandas as pd

from errors import error_handler


class DataStorage:
    """Stores and Retrieve data in specified format defaults to '.csv format"""

    def __init__(self, file_name, format=".csv") -> None:
        self.file_name = file_name
        self.format = format
        self.data = []

    def get_data(self, data):
        """Gets scraped data for storage."""
        self.data.append(data)

    def store_data(self, columns):
        df = pd.DataFrame(self.data, columns=columns)
        df.to_csv(f"{self.file_name}{self.format}", index=False)

    @error_handler()
    def fetch_data(self, filename):
        return pd.read_csv(filename)



if __name__ == "__main__":
    csv_store = DataStorage("coronavirus_data")
    csv_store.get_data([[5], [1], [3]])
    csv_store.store_data(["Cases", "Deaths", "Recoveries"])
    print(csv_store.fetch_data('coronavirus_data.csv'))
