from gensim import corpora, models

import json
import gensim

if __name__ == "__main__":
    with open('data_50k.json') as f:
        data = json.load(f)

    # This is the clean corpus.
    doc_clean = [doc.split() for doc in data.values()]

    # for doc in doc_clean:
    #     print(doc)
    #     print()

    # Create dictionary and corpus
    # dictionary = corpora.Dictionary(doc_clean)
    # doc_term_matrix = [dictionary.doc2bow(text) for text in doc_clean]

    # # Creating the object for LDA model using gensim library (code copied from assignment)
    # Lda = gensim.models.ldamodel.LdaModel

    # # Running and Trainign LDA model on the document term matrix. (code copied from assignment, changes # of passes to 2 instead of 100 to speed things up)
    # ldamodel = Lda(doc_term_matrix, num_topics=2, id2word=dictionary, passes=2)
    
    # Print 2 topics and describe then with 4 words. (code copied from assignment)
    # topics = ldamodel.print_topics(num_topics=5, num_words=4)

    # i=0
    # for topic in topics:
    #     print ("Topic",i ,"->", topic)     
    #     i+=1

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