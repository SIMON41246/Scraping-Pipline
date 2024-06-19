import re

from pymongo import MongoClient
from selectolax.parser import HTMLParser

from utils.extract import extract_full_body

URL = "https://www.jumia.ma/catalog/?q=ring&page=4#catalog-listing"
category = "Rings"


# Remove currency
def extract_prices(price_str):
    # Use regex to find all price values in the string
    prices = re.findall(r"[\d,]+(?:\.\d{2})?", price_str)
    # Convert the prices to float
    prices = [float(price.replace(',', '')) for price in prices]
    if not prices:
        return None
    return min(prices),max(prices)
if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017")
    db = client["Jumia"]
    collection = db["Products"]
    html = extract_full_body(URL=URL, wait_for='div[class="-pvs col12"]')
    tree = HTMLParser(html)

    divs = tree.css('article[class="prd _fb col c-prd"]')
    game_data = []
    for d in divs:
        title=d.css_first("a[class='core'] > div[class='info'] > h3").text()
        price = d.css_first("a[class='core'] > div[class='info'] > div[class='prc']").text()
        price_min, price_max = extract_prices(price)
        #original_price=extract_prices(d.css_first("a[class='core'] > div[class='info'] > div[class='old']",default=""))
        # shipping = d.css_first("span[class='s-item__shipping s-item__logisticsCost']", default="").text().strip()
        link = d.css_first("a[class='core']").attributes.get('href')
        image=d.css_first("a[class='core'] > div[class='img-c'] > img").attributes.get("data-src"),

        if isinstance(image, tuple):
            image_url = image[0]
        else:
            image_url = image
        result={
            "title": title,
            "price_min":price_min,
            "price_max":price_max,
            "shipping": "Free",
            "link":f"https://www.jumia.ma{link}",
            "image": image_url,
            "category": category,
        }
        game_data.append(result)
        print(result)
        # save_to_file("extract", game_data)
        collection.insert_one(result)