import pickle
from typing import Optional

# This runs on first import
with open('wiki_wc.pickle', 'rb') as f:
    wc = pickle.load(f)


def get_article_len(title: str) -> Optional[int]:
    """"
    :return the word count of the article corresponding to the title given if found, or None if not found
    """
    return wc[title] if title in wc else None
