# Web Scraping and Data Visualization Python Project

A Python project that scrapes coronavirus data from `"https://www.worldometers.info/coronavirus/"` and visualizes the collected data. The project can be used as a starting point for data analysis.

The codes are generic that they can be used with other urls.

## Installation

To use this project, you need to have Python 3 installed on your machine. You can download Python 3 from the official website <https://www.python.org/downloads/>.

Once you have installed Python 3, you can install the necessary libraries by running the following command in the terminal:

```
pip install -r requirements.txt
```

This will install the required libraries, including requests, BeautifulSoup, and pandas.

## Usage

To use this project, you need to first clone the repository to your local machine by running the following command:

```
git clone https://github.com/officialksolomon/webscraping_and_visualization.git
```

Then, navigate to the project directory:

```
cd your-repository
```

Open the `main.py` file and run the file.

The script will scrape the data from the url, save to a  CSV file in the current working directory, create a visual representation of the data using Matplotlib and also store visua as a png file in the current working directory.

## Configuration

You can configure the project by modifying the `config.py` file. The file contains variables that control the behavior of the scraper and the visualizer. You can modify the URL of the website to scrape, the CSS selectors to extract data, and the columns to include in the CSV file and the visualizations.

For more advanced users, you can modify the `main.py` file and change the variables directly.

`NOTE: We expect your final scraped data values to be of type integer so it can be plotted by Matplotlib...`

## License

This project is licensed under the MIT License.

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request. I welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## Credits

This project was created by `Solomon Uche (https://github.com/officialksolomon/)`.
