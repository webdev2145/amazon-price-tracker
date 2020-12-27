import requests
from bs4 import BeautifulSoup
import smtplib

from credentials import *

'''
Track the price of a product on amazon.com.
An email is sent to me if or when the price goes down to what I'm willing to pay
'''

url = input('Copy and paste the url of the item you want to track price for: ')

headers = {'Accept-Language': 'en-US,en;q=0.5', 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'}
response = requests.get(url=url, headers=headers)

amazon_soup = BeautifulSoup(response.text, 'html.parser')

data = amazon_soup.find(name='span', id='priceblock_ourprice')

item_price = data.get_text()
item_price = item_price.replace('$', '')

item_price = float(item_price)

if item_price < 300:
    message = f"Its time to Buy!! {url}"
    with smtplib.SMTP(gmail_smtp, port=port) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=my_to_address,
                            msg='Subject: Amazon Price Watcher\n\nmessage')

else:
    print('Still waiting')