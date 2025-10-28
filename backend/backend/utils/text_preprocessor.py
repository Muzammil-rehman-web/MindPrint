import re

def clean_text(text):
    """
    Cleans input text by removing punctuation, numbers,
    and converting to lowercase.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip()

nltk
