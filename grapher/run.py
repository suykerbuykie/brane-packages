from gensim import corpora, models

import json
import gensim

if __name__ == "__main__":
    with open('data_500k.json') as f:
        data = json.load(f)

    # This is the clean corpus.
    doc_clean = [doc.split() for doc in data.values()]

    # Create dictionary out of clean data
    dictionary = gensim.corpora.Dictionary(doc_clean)
    dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

    # Turn dictionary into bag of words
    bow_corpus = [dictionary.doc2bow(doc) for doc in doc_clean]
    
    tfidf = models.TfidfModel(bow_corpus)
    corpus_tfidf = tfidf[bow_corpus]

    lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=10, id2word=dictionary, passes=50, workers=4)
    for idx, topic in lda_model_tfidf.print_topics(-1):
        print('Topic: {} Word: {}'.format(idx, topic))
