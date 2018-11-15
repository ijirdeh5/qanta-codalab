import os
import pickle
import numpy as np
from typing import Optional


# This runs on first import
# fix path stuff
if os.getcwd().split('/')[-1] != 'obscurity':
    os.chdir('obscurity')

with open('wiki_wc.pickle', 'rb') as f:
    wc = pickle.load(f)


def get_article_len(title: str) -> Optional[int]:
    """"
    :return the word count of the article corresponding to the title given if found, or None if not found
    """
    return wc[title] if title in wc else None


def get_log_wc(title: str) -> Optional[float]:
    """
    :param title: the Article Name
    :return: the log (ln) of the wc
    """
    num_words = get_article_len(title)
    if num_words is not None:
        return np.log(num_words)
    else:
        return None
