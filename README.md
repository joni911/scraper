Web Scraper for Novel Translation

This script is a web scraper that extracts information from a series of web pages and saves it to a series of text files. It does this by making HTTP requests to the web pages using the requests module, parsing the HTML content of the pages using the BeautifulSoup module, and extracting relevant information from the parsed HTML using the json module.
How to Use

To use this script, you will need to have Python 3 and the following modules installed:

    requests
    beautifulsoup4
    json

You can install these modules using pip, the Python package manager. For example, to install the requests module, you can use the following command:

pip install requests

Once you have the required modules installed, you can run the script using the following command:

python scraper.py

The script will then scrape the web pages, extract the relevant information, and save it to a series of text files.
Configuration

You can customize the behavior of the script by modifying the following variables at the beginning of the script:

    ID_RANGE: A range of IDs to scrape. The script will scrape one web page for each ID in this range.
    BASE_URL: The base URL of the web pages to scrape. The script will append the ID to this URL
