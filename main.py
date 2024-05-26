import re

from pymongo import MongoClient
from selectolax.parser import HTMLParser

from utils.extract import extract_full_body


def extract_prices(price_str):
    # Use regex to find all price values in the string
    prices = re.findall(r"\$([\d,]+\.\d{2})", price_str.replace(',', ''))
    prices = list(map(float, prices))
    if not prices:
        return None, None
    return min(prices), max(prices)

URL = "https://www.ebay.com/b/Fine-Earrings/261990/bn_71835358"
if __name__ == '__main__':
    collectionName="Earrings"
    client = MongoClient("mongodb://localhost:27017")
    db = client["Ebay"]
    collection = db["Products"]


    html = extract_full_body(URL=URL, wait_for='li[class="s-item s-item--large"]')
    tree = HTMLParser(html)

    divs = tree.css('li[class="s-item s-item--large"]')
    game_data = []
    for d in divs:
        # attrs=parse_row_attributes(d,config.get('item'))
        # attrs=format_and_transform(attrs)
        title = d.css_first("a[class='s-item__link'] > h3").text()
        price = d.css_first("div[class='s-item__detail s-item__detail--primary'] > span").text().strip()
        price_min, price_max = extract_prices(price)
        # original_price=d.css_first("span[class='STRIKETHROUGH']").text().strip()
        shipping = d.css_first("span[class='s-item__shipping s-item__logisticsCost']", default="").text().strip()
        link = d.css_first("div[class='s-item__info clearfix'] > a").attributes.get('href')
        image = d.css_first("div[class='s-item__image-helper'] >img").attributes.get('src')
        # images = extract_image_urls(link, "div[class='ux-image-grid-container filmstrip filmstrip-x'] > button > img")

        result = {
            "title": title,
            "price_min": price_min,
            "price_max":price_max,
            # 'original_price':original_price,
            "shipping": shipping,
            'link': link,
            'image': image,
            'category':collectionName
            # 'images': images
        }
        game_data.append(result)
        print(result)
        # save_to_file("extract", game_data)
        collection.insert_one(result)
