from selectolax.parser import Node
from datetime import datetime
import re
import pandas as pd
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser


#
# 
# def get_attrs_from_node(node: Node, attr: str):
#     if node is None or not issubclass(Node, type(node)):
#         raise ValueError('The function is not selectolax node to be Provided')
# 
#     return node.attributes.get(attr)
# 
# 
# def get_first_n(input_list: list, n: int = 5):
#     return input_list[:n]
# 
# 
# def reformat_date(date_row: str, input_format: str = '%b %d %Y', output_format: str = "%Y-%m-%d"):
#     dt_obj = datetime.strptime(date_row, input_format)
#     return datetime.strftime(dt_obj, output_format)
# 
# 
# def regex(input_str: str, pattern: str, do_what="findall"):
#     if do_what == "findall":
#         return re.findall(pattern, input_str)
#     elif do_what == "split":
#         return re.split(pattern, input_str)
#     else:
#         raise ValueError("the function expected findall or split")
# 
# 
# def format_and_transform(attrs: dict):
#     transform = {
#         "thumbnail": lambda n: get_attrs_from_node(n, "src"),
#         "tags": lambda input_list: get_first_n(input_list, 5),
#         # "released_date": lambda date: reformat_date(date, "%d %b. %Y", '%Y-%m-%d')
#         "views": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
#         "original_price": lambda raw: regex(raw, r'\s', "split")[0],
#         "discount_price": lambda raw: regex(raw, r'\s', "split")[0],
#     }
#     for k, v in transform.items():
#         if k in attrs:
#             attrs[k] = v(attrs[k])
#     return attrs


def save_to_file(filename="extract.csv", data: list[dict] = None):
    if data is None:
        raise ValueError('the Function expected data as list of dictionaries')
    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
    df.to_csv(filename, index=False)


def extract_image_urls(url, selector):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the URL
        page.goto(url)

        # Wait for the page to load
        page.wait_for_load_state("networkidle")

        # Get the HTML content after rendering
        html_content = page.content()

        # Close the browser


    # Parse the HTML content to extract the image URLs
    html_parser = HTMLParser(html_content)
    image_urls = [img.attributes.get('src') for img in html_parser.css(selector)]

    return image_urls
