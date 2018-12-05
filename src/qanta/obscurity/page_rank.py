import os
import pickle
import numpy as np

from typing import Optional

with open('qanta/obscurity/article_index.pickle', 'rb') as f:
    article_index = pickle.load(f)

rank = np.load('qanta/obscurity/rank_matrix.npy')




def get_log_rank(title: str) -> Optional[float]:
    if title in article_index:
        return np.log(rank[article_index[title]])
    else:
        return None

def get_rank(title: str) -> Optional[float]:
    if title in article_index:
        return rank[article_index[title]]
    else:
        return None


MIN_RANK = np.min(rank)
LOG_MIN_RANK = np.log(MIN_RANK)


def is_min_rank(title: str) -> bool:
    l_r = get_log_rank(title)
    return np.abs(l_r - LOG_MIN_RANK) < 1e-5 if l_r is not None else False


