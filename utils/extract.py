from playwright.sync_api import sync_playwright


def extract_full_body(URL, wait_for=None):
    TIME_OUT = 210000
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)

        page.wait_for_load_state('networkidle' )
        page.evaluate("()=> window.scroll(0,document.body.scrollHeight)")
        page.wait_for_load_state("domcontentloaded")
        if wait_for:
            page.wait_for_selector(wait_for)

        html = page.inner_html("body")
        return  html
