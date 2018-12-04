import json
import pickle
import scipy.sparse
from scipy.sparse import csc_matrix
import numpy as np

def pickle_word_counts_wiki():
    WIKI_FILE_PATH = '../../../data/wiki_lookup.json'

    word_counts = {}

    print("Loading file...")
    with open(WIKI_FILE_PATH) as f:
        wiki = json.load(f)

        iterations = 0
        total_iterations = len(wiki.keys())

        for article in wiki.keys():
            text = wiki[article]['text']
            word_count = len(text.split())
            word_counts[article] = word_count

            iterations += 1
            if iterations % 1000 == 0:
                print("Processing: " + "{:.0%}".format(iterations / total_iterations))

    with open('word_count.pickle', 'wb') as handle:
        pickle.dump(word_counts, handle)

def pickle_article_indices():
    WIKI_FILE_PATH = '../../../data/wiki_lookup.json'
    article_index = {}
    with open(WIKI_FILE_PATH) as f:
        wiki = json.load(f)
        index = 0
        for article in wiki.keys():
            article_index[article] = index
            article_index[index] = article
            index += 1

    with open('article_index.pickle', 'wb') as handle:
        pickle.dump(article_index, handle)

def pagerank(G, beta=0.85, epsilon=10**-4):
    n,_ = G.shape
    deg_out_beta = G.sum(axis=0).T/beta
    ranks = np.ones((n,1)) / n
    time = 0
    converged = False
    while not converged:
        time +=1
        with np.errstate(divide='ignore'):
            new_ranks = G.dot((ranks/deg_out_beta))
        new_ranks += (1-new_ranks.sum())/n
        if np.linalg.norm(ranks-new_ranks,ord=1) <= epsilon:
            converged = True
        ranks = new_ranks
    return(np.squeeze(np.asarray(ranks)), time)

def run_pagerank():
    WIKI_FILE_PATH = '../../../data/wiki_lookup.json'

    with open(WIKI_FILE_PATH) as f:
        wiki = json.load(f)
        sparse = scipy.sparse.load_npz('sparse_links_n.npz')
        sparse_t = np.transpose(sparse)

    for i in range(len(wiki.keys())):
        if sparse_t[i].nnz == 0:
            sparse[i, i] = 1
    scaled_sparse = sparse / sparse.sum(axis=0)
    rank, iters = pagerank(scaled_sparse)
    np.save('rank_matrix.npy', rank)

if __name__ == '__main__':
    pickle_word_counts_wiki()
    pickle_article_indices()
    run_pagerank()