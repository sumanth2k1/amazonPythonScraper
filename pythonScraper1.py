from bs4 import BeautifulSoup
import requests

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

    i_title = soup.find_all('span' ,{'class':'a-size-medium a-color-base a-text-normal'})
    i_price = soup.find_all('span' ,{'class':"a-price-whole"})
    i_rating = soup.find_all('span' ,{'class':"a-icon-alt"})
    i_review = soup.find_all('span' ,{'class':"a-size-base s-underline-text"})
    i_link = soup.find_all("a",  {"class":"a-link-normal s-no-outline"})
    item_links = [link['href'] for link in i_link]

    for link,name,price,rating,review  in zip(item_links,i_title,i_price,i_rating,i_review):
        #newlink = link["href"]
        print ("Item Link: "+"https://www.amazon.in" +link)
        print ("Item Name: " +name.string.strip())
        print ("Item Price:" +price.text.strip())
        print ("Item Rating: " +rating.string.strip())
        print ("Item Reviews:" +review.text.strip())
        print ('-'*70)

    i += 1
    print ("#"*70)
    print ("")
