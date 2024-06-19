from pymongo import MongoClient
from selectolax.parser import HTMLParser

from utils.extract import extract_full_body

URL = "https://www.decathlon.ma/3702-bottes-bottines-femmes#"

if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017")
    db = client["Decathlon"]
    collection = db["Products"]
    html = extract_full_body(URL=URL, wait_for='div[class="js-algolia algolia container-fluid px0"]')
    tree = HTMLParser(html)

    divs = tree.css('ol[class="ais-InfiniteHits-list"]')
    game_data = []
    for d in divs:
        title=d.css_first("div[class='row m0'] > h3['h3 name-product mb0'] > a").text()
        # price = d.css_first("a[class='core'] > div[class='info'] > div[class='prc']").text()
        # # price_min, price_max = extract_prices(price)
        # category=d.css_first("a[class='core']").attributes.get('data-ga4-item_category')
        # original_price=d.css_first("a[class='core'] > div[class='info'] > div[class='old']",default="")
        # # shipping = d.css_first("span[class='s-item__shipping s-item__logisticsCost']", default="").text().strip()
        # link = d.css_first("a[class='core']").attributes.get('href')
        # image1 = d.css_first("a[class='core'] > div[class='img-c'] > img").attributes.get("src"),
        # image2=d.css_first("a[class='core'] > div[class='img-c'] > img").attributes.get("data-src"),
        result={
            # "tag":"Jumia",
            # "category":category,
            "title":title,
            # "price":price,
            # "original_price":original_price,
            # "image1":image1,
            # "image2":image2,
            # "link":f"https://www.jumia.ma{link}"


        }
        #game_data.append(result)
        print(result)
        # save_to_file("extract", game_data)
        #collection.insert_one(result)