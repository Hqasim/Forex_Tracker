# Forex_Tracker

Simple python scrapy project which scrapes data of international forex currencies and outputs them in JSON format.

## Dependencies

- Python 3.10.5
- Pip 22.0.4
- Scrapy 2.6.1

## Steps to reproduce

Clone the repository and create a python virtual environment in root directory

```
python -m venv env
```

Active virtual enviroment (linux command)

```
source env/Scripts/activate
```

Install scrapy in virtual enviroment

```
pip install scrapy
```

Navigate to tracker folder and enter the following command to scrap data and receive output in JSON file

```
scrapy crawl rates -o rates.json
```

Sample output of script in JSON format

```
[
  {
    "Title": "Forex Curreny Rates As on Mon, Jun 27 2022, 10:46 GMT",
    "CNY": "6.6916 Units per USD",
    "EUR": "0.9472 Units per USD",
    "JPY": "135.1851 Units per USD",
    "PKR": "208.3277 Units per USD",
    "SAR": "3.75 Units per USD",
    "AED": "3.6725 Units per USD",
    "GBP": "0.8152 Units per USD"
  }
]
```
