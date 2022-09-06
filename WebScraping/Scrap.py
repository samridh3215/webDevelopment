from bs4 import BeautifulSoup as bs
import requests as r

link = "https://www.amazon.in/boAt-BassHeads-100-Headphones-Black/dp/B071Z8M4KX/ref=sr_1_3?crid=GWBFZ54KX5H2&keywords=wired+earphones&qid=1661184160&sprefix=%2Caps%2C267&sr=8-3"
page = r.get(link)
print(page)
soup = bs(page.content, 'html.parser')
print(soup.prettify())
productName = bs.find_all('span', class_ = 'a-size-large product-title-word-break')
