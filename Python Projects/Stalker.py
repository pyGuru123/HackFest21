# In this code,if the prices of the laptop which is currently priced at ₹1,80,990.00,falls below ₹1,80,000.00 we get the notification email

# import required files and modules

import requests
from bs4 import BeautifulSoup
import smtplib
import time

# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

# send a request to fetch HTML of the page
response = requests.get('https://www.amazon.in/Lenovo-Legion-Windows-Graphics-81YU002AIN/dp/B08FJCRGPR/ref=sr_1_1_sspa?dchild=1&keywords=lenovo+legion&qid=1628964644&s=computers&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0FFWlRGWU5HQUZBJmVuY3J5cHRlZElkPUEwNTY4NTgwMUtFUDNZQkhaM0NOVCZlbmNyeXB0ZWRBZElkPUEwMjA5NTE3MVlSM0xDRFpXWDZDWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=', headers=headers)

# create the soup object
soup = BeautifulSoup(response.content, 'html.parser')

# change the encoding to utf-8
soup.encode('utf-8')

#print(soup.prettify())

# function to check if the price has dropped below 20,000
def check_price():
  title = soup.find(id= "productTitle").get_text()
  price = soup.find(id = "priceblock_ourprice").get_text().replace(',', '').replace('₹', '').replace(' ', '').strip()
  #print(price)

  #converting the string amount to float
  converted_price = float(price[0:6])
  print(converted_price)
  if(converted_price < 180000):
    send_mail()
  else :
    print("You have to wait,The prices are still high")

  #using strip to remove extra spaces in the title
  print(title.strip())




# function that sends an email if the prices fell down
def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('sender@gmail.com', 'Password')

  subject = 'Hey XXXXX,Hurry Up ! Prices Have Fallen Down'
  body = "Check out the amazon link here -> https://www.amazon.in/Lenovo-Legion-Windows-Graphics-81YU002AIN/dp/B08FJCRGPR/ref=sr_1_1_sspa?dchild=1&keywords=lenovo+legion&qid=1628964644&s=computers&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0FFWlRGWU5HQUZBJmVuY3J5cHRlZElkPUEwNTY4NTgwMUtFUDNZQkhaM0NOVCZlbmNyeXB0ZWRBZElkPUEwMjA5NTE3MVlSM0xDRFpXWDZDWiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

  msg = f"Subject: {subject}\n\n{body}"
  
  server.sendmail(
    'sender@gmail.com',
    'receiver@gmail.com',
    msg
  )
  #print a message to check if the email has been sent
  print('Hey,Email has been sent!')
  # quit the server
  server.quit()

#loop that allows the program to regularly check for prices
while(True):
  check_price()
  time.sleep(60 * 60)