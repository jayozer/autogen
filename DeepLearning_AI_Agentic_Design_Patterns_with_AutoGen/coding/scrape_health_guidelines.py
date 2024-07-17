# filename: scrape_health_guidelines.py
import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request status
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data from {url}: {e}")
        return None

def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    texts = soup.get_text()
    return texts

urls = [
    'https://www.cdc.gov/fluoridation/faqs/index.htm',
    'https://www.ada.org/en/member-center/oral-health-topics/fluoride-means-protection-against-tooth-decay',
    'https://www.who.int/news-room/fact-sheets/detail/fluorides-and-oral-health'
]

for url in urls:
    content = get_website_content(url)
    if content:
        extracted_text = extract_text(content)
        print(f"Extracted from {url[:30]}: {extracted_text[:200]}...\n")
    else:
        print(f"Failed to retrieve data from {url}")