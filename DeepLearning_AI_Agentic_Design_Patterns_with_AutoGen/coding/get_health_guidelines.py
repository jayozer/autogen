# filename: get_health_guidelines.py
import requests

def get_health_guidelines(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

urls = [
    'https://www.cdc.gov/fluoridation/index.html',
    'https://www.ada.org/en/public-programs/health-issues/fluoride-topical-and-systemic',
    'https://www.who.int/news-room/facts-in-pictures/detail/fluorides-for-oral-health'
]

guidelines = []
for url in urls:
    guideline = get_health_guidelines(url)
    if guideline:
        guidelines.append(guideline)
    else:
        print(f"Failed to retrieve data from {url}")

# Check data retrieval
for index, guideline in enumerate(guidelines):
    print(f"Data from URL {urls[index]}: \n{guideline[:200]}...\n")