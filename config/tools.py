import json

_config = {
    "url": "https://www.ebay.com/b/Home-Improvement/159907/bn_1851980",
    "container": {
        "name": "store_sale_divs",
        "selector": 'div[class="container"]',
        "match": "all",
        "type": "node"
    },
    "item": [
        {
            "name": "title",
            "selector": 'div[class*="s-item__info"] > a > h3',
            "match": "first",
            "type": "text"
        },
        # {
        #     "name": "thumbnail",
        #     "selector": 'img[class="cODQhXeXS-Yn-vLIBNwyW"]',
        #     "match": "first",
        #     "type": "node"
        # },
        {
            "name": "Price",
            "selector": 'div[class="s-item__detail s-item__detail--primary"] > span',
            "match": "all",
            "type": "text"
        },
        {
            "name": "Shipping",
            "selector": "div[class='s-item__detail s-item__detail--primary'] > span",
            "match": "first",
            "type": "text"
        },

    ]
}


def generate_config():
    with open('config.json', "w") as f:
        json.dump(_config, f, indent=4)


def get_config(load_from_file=False):
    if load_from_file:
        with open('config.json', 'r') as f:
            return json.load(f)
    return _config


if __name__ == '__main__':
    generate_config()
