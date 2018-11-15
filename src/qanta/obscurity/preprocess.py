import json
import pickle

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

if __name__ == '__main__':
    pickle_word_counts_wiki()