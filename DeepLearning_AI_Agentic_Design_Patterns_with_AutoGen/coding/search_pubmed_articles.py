# filename: search_pubmed_articles.py
import requests

def search_pubmed(query, api_key, retmax=10):
    url = f"https://api.ncbi.nlm.nih.gov/lit/ctxp/v1/pubmed/?term={query}&retmode=json&api_key={api_key}&retmax={retmax}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

api_key = 'YOUR_NCBI_API_KEY'
query = 'fluoride impact on infants'
data = search_pubmed(query, api_key)

if data:
    for article in data['resultList']['result']:
        print(f"Title: {article['title']}\nURL: {article['viewURL']}\n")
else:
    print("Failed to retrieve data from PubMed.")