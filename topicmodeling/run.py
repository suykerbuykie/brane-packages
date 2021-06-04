from gensim import corpora, models

import json
import gensim
import yaml
import os
import sys

def topicmodeling(input:str, output:str) -> str:
    with open('input') as file:
        data = json.load(file)

    # This is the clean corpus.
    doc_clean = [doc.split() for doc in data.values()]

    # Create dictionary out of clean data
    dictionary = gensim.corpora.Dictionary(doc_clean)
    dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

    # Turn dictionary into bag of words
    bow_corpus = [dictionary.doc2bow(doc) for doc in doc_clean]

    # Create model and run
    tfidf = models.TfidfModel(bow_corpus)
    corpus_tfidf = tfidf[bow_corpus]
    lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=10, id2word=dictionary, passes=50, workers=4)
    
    # Create topics
    topics = {}
    for idx, topic in lda_model_tfidf.print_topics(-1):
        topics[idx] = topic

    # Create outputs
    textfile = open(output, "w")
    for element in topics:
        textfile.write(element + "\n")
    textfile.close()
    return topics


if __name__ == "__main__":
    # Get arguments
    command = sys.argv[1]
    argument_input = os.environ["INPUT"]
    argument_output = os.environ["OUTPUT"]

    # Define function
    functions = {
        "topicmodeling": topicmodeling,
    }

    # Run function
    output = functions[command](argument_input, argument_output)
    print(yaml.dump({"output": output}))
