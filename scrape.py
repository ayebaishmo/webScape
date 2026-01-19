from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

URL = "https://everything-ug.netlify.app/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, timeout=60000)

    # Get rendered html 

    html = page.content()
    browser.close()


# Parse html 
soup = BeautifulSoup(html, "html.parser")

# example 1 page title 
title = soup.title.text.strip()
print("Page title:", title)


# example 2 All page headings 
headings = [h.text.strip() for h in soup.find_all(["h1", "h2", "h3"])]
print("Headings:")


for h in headings:
    print ("_", h)
