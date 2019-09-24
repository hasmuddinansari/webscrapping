import csv
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

my_url = 'https://www.flipkart.com/search?q=latest+phone+under+10000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_19_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_19_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=latest+phone+under+10000&requestId=f864e7d1-f1eb-4dfe-9faa-4ed62c7ba3dd&as-searchtext=latest%20phone%20under%20'

uClient = urlopen(my_url)
page_html = uClient.read() #reading html file from website
uClient.close()
page_soup = soup(page_html, "html.parser") #making a parser to target html page.


containers = page_soup.findAll("div", {"class": "bhgxx2 col-12-12"})
# print(len(containers))
container = containers[0]

#finding one product name;

total_list = []


for i in range(len(containers)-6):
    product_name1 = page_soup.findAll("div", {"class": "_3wU53n"})
    product_name= str(product_name1[i].text)     #name of model

    product_price1 = page_soup.findAll("div", {"class":"_1vC4OE _2rQ-NK"})
    product_price = str(product_price1[i].text)          #price of model..

    product_rating1 = page_soup.findAll("div", {"class":"hGSR34"})
    product_rating =str(product_rating1[i].text)
    my_list = [product_name, product_price,product_rating]
    # print(f'{product_name},{product_price},{product_rating}')
    total_list.append(my_list)


with open('price.csv', 'w+', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product_Name', 'Product_Price', 'Rate'])

    for listed in total_list:
        writer.writerow(listed)

file.close()
print("Done")


