from bs4 import BeautifulSoup
import requests
import csv

i=1
while i<=20:
    start = "this is the Page {} :-"
    print(start.format(i))
    print("")
    dummyUrl='https://www.amazon.in/s?k=bags&rh=p_72%3A1318478031&dc&page={}&crid=2M096C61O4MLT&qid=1688634541&rnid=1318475031&sprefix=ba%2Caps%2C283&ref=sr_pg_{}'
    url = dummyUrl.format(i,i)
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0;Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    data = []
    
    i_title = soup.find_all('span' ,{'class':'a-size-medium a-color-base a-text-normal'})
    i_price = soup.find_all('span' ,{'class':"a-price-whole"})
    i_rating = soup.find_all('span' ,{'class':"a-icon-alt"})
    i_review = soup.find_all('span' ,{'class':"a-size-base s-underline-text"})
    i_link = soup.find_all("a",  {"class":"a-link-normal s-no-outline"})
    item_links = [link['href'] for link in i_link]

    for link,name,price,rating,review  in zip(item_links,i_title,i_price,i_rating,i_review):
        print ("Item Link: "+"https://www.amazon.in" +link)
        print ("Item Name: " +name.string.strip())
        print ("Item Price:" +price.text.strip())
        print ("Item Rating: " +rating.string.strip())
        print ("Item Reviews:" +review.text.strip())
        print ('-'*70)

        #purl = "https://www.amazon.in" +link
        #headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0;Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}

        #ppage = requests.get(purl, headers=headers)
        #soup = BeautifulSoup(ppage.content, "html.parser")
        
        #description = soup.find('span', {'id': 'productTitle'}).text.strip()
        #asin = soup.find('th', string='ASIN').find_next('td').text.strip()
        #product_description = soup.find('div', {'id': 'productDescription'}).text.strip()
        #manufacturer = soup.find('a', {'id': 'bylineInfo'}).text.strip()

        item_data = {
            'Product URL': "https://www.amazon.in" +link,
            'Product Name': name.string.strip(),
            'Product Price': price.text.strip(),
            'Rating': rating.string.strip(),
            'Number of Reviews': review.text.strip()
        }

        # Append the item data to the list
        data.append(item_data)

    i += 1
    csv_filename = 'product_data.csv'
    csv_fields = ['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews']

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(data)

    print("Data exported to", csv_filename)
    print ("#"*70)
    print ("")
