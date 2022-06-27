# Forex_Tracker

Scrapes data of foreign exchange currency conversion rates.

## Dependencies

- Python 3.10.5
- Pip 22.0.4
- Scrapy 2.6.1

## Steps to reproduce

Create a python virtual environment

```
python -m venv env
```

Active virtual enviroment

```
source env/Scripts/activate
```

Install scrapy in virtual enviroment

```
pip install scrapy
```

Navigate to tracker directory from root and run the following command to scrape data

```
scrapy crawl rates
```
