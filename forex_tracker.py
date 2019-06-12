# Objective: Display Forex exchange rates in a GUI.
# USD to PKR Conversion tracker.

from lxml import html
import requests
from tkinter import * 

# Dollar Rate data fetch from: https://hamariweb.com/finance/forex/
page = requests.get('https://hamariweb.com/finance/forex/')
tree = html.fromstring(page.content)

open_market_buy = tree.xpath('//*[@id="dollar_rate_world"]/tbody/tr[1]/td[3]/text()')
open_market_sell = tree.xpath('//*[@id="dollar_rate_world"]/tbody/tr[1]/td[4]/text()')
inter_bank_buy = tree.xpath('//*[@id="inter_bank_table"]/tbody/tr[4]/td[3]/text()')
inter_bank_sell = tree.xpath('//*[@id="inter_bank_table"]/tbody/tr[4]/td[4]/text()')

date = tree.xpath('//*[@id="main-content"]/div/div[1]/div/h1/small/text()')

# Tkinter GUI
root = Tk()
root.title("Currency Tracker USD to PKR")
#root.geometry('{}x{}'.format(325, 225)) # Commented out to disable auto sizing

l1 = Label(root, text = "Currency Rates: USD to PKR").grid(row=0, column = 1)
l2 = Label(root, text = "Inter Bank").grid(row=1, column = 1)
l3 = Label(root, text = "Buying").grid(row=2, column = 0)
l4 = Label(root, text = "Selling").grid(row=2, column = 2)
d1 = Label(root, text = inter_bank_buy).grid(row=3, column = 0) # DATA 1
d2 = Label(root, text = inter_bank_sell).grid(row=3, column = 2) # DATA 2
l5 = Label(root, text = "Open Market").grid(row=4, column = 1)
l6 = Label(root, text = "Buying").grid(row=5, column = 0)
l7 = Label(root, text = "Selling").grid(row=5, column = 2)
d3 = Label(root, text = open_market_buy).grid(row=6, column = 0) # DATA 3
d4 = Label(root, text = open_market_sell).grid(row=6, column = 2) # DATA 4

date_GUI = Label(root, text = date[0]).grid(row=7, column = 1)

root.mainloop()