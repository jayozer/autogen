# filename: search_pubmed_biopython.py
from Bio import Entrez

def search_pubmed(query, email, retmax=10):
    Entrez.email = email
    handle = Entrez.esearch(db="pubmed", term=query, retmax=retmax)
    record = Entrez.read(handle)
    handle.close()
    return record['IdList']

def fetch_details(id_list):
    ids = ','.join(id_list)
    handle = Entrez.efetch(db="pubmed", id=ids, rettype="medline", retmode="text")
    records = handle.read()
    handle.close()
    return records

email = 'YOUR_EMAIL@example.com'
query = 'fluoride impact on infants'
id_list = search_pubmed(query, email)

if id_list:
    records = fetch_details(id_list)
    print(records)
else:
    print("Failed to retrieve data from PubMed.")