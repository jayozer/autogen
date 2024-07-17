# filename: summarize_text.py
import spacy

def summarize_text(text, max_sentences=3):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents][:max_sentences]
    return ' '.join(sentences)

# Example to summarize one abstract
abstract = "Full abstract text from one retrieved article"
summary = summarize_text(abstract)
print(summary)