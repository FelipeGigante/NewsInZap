# News Scraper and API Consumer

 ![Screen-Recording-_11-05-2021-20-47-33_](https://github.com/FelipeGigante/SimpleApp-Flutter/assets/61218356/92237d43-fd2a-407b-be4c-04d83bd03c4e)

## Getting Started

To get started with this project, you'll need to clone the repository, install the necessary dependencies, and configure the project with your API key and target URLs.

## Prerequisites

Python 3.7+
pip (Python package installer)

## Technologies Used

- Python: The main programming language used for this project.
- Requests: A simple HTTP library for Python, used to make API requests.
- BeautifulSoup: A library used for web scraping to pull the data out of HTML and XML files.

## Objective


## How to use?
1. Scraping News and Sending to API: Run the main.py script to start scraping news headlines and sending them to the API.
```
python main.py
```

2. Script Details:

- main.py: The main script that initiates the scraping process and handles API requests.
- news_scraper.py: Contains functions for scraping news headlines from the target website.
- api_consumer.py: Contains functions for making requests to the API.

## Debugging

- If you encounter any issues, ensure that your API key and endpoint URL are correctly configured in config.py. You can also check the error messages for more details on what might be going wrong.