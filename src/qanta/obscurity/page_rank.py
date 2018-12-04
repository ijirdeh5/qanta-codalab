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



