from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt


class DataVisualizer(ABC):
    @abstractmethod
    def get_data(self, file_name):
       pass

    @abstractmethod
    def visualize_data(self, data):
        pass



class PieChartVisualizer(DataVisualizer):
    def __init__(self) -> None:
        self.data  = None
        self._data_columns = None
    

    def get_data(self, file_name):
        dataframe = pd.read_csv(file_name)
        self.data_columns = list(dataframe.head(0).columns)
        self.data = dataframe.to_numpy()[0]

    def visualize_data(self):
        fig, ax = plt.subplots()
        if self.data is not None:
            ax.pie([data.replace(",", "") for data in self.data], labels=self.data_columns)
            ax.set_title('Coronavirus cases, deaths, and recovered cases worldwide.')
            fig.savefig('coronavirus_data.png')
            plt.show()

         

if __name__ == "__main__":
    visualizer =  PieChartVisualizer()
    visualizer.get_data('coronavirus_data.csv')
    print(visualizer.data)
    print(visualizer.data_columns)
    visualizer.visualize_data()

    
