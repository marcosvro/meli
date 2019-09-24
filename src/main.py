import pandas as pd
import numpy as np
#import dict_generator as dg
from gensim import corpora, models

def get_words():
    try:
        df = pd.read_csv('word_dict.csv', index_col=0)
        words = np.array(df)[:, 0]
        return set(words)
    except Exception:
        return dg.generate_dict()

def process_sentence(sentence):
    sentence = sentence.split(' ')
    formated_sentence = []
    for word in sentence:
        try:
            if word[-1] == ',' or word[-1] == ')' or word[-1] == ']' or word[-1] == '>' or word[-1] == '|':
                word = word[:-1]
            if word[0] == ',' or word[0] == '(' or word[0] == '[' or word[0] == '<' or word[0] == '|':
                word = word[1:]
        except Exception:
            pass
        if len(word) > 1:
            formated_sentence.append(word)
    return formated_sentence

def get_data():
    texts = []
    num_samples = 20000000

    try:
        data = pd.read_csv('../train.csv', usecols=['title'] , encoding='utf-8')
        
        for i, title in enumerate(data['title']):
            if i%1000000 == 0:
                print('progres %i/%i' %(i, num_samples))
            if i == 5000000:
                break
            texts.append(process_sentence(title))
        return texts
    except Exception:
        print(Exception)
        return {'title': []}

if __name__ == '__main__':
    
    texts = get_data()
    print(len(texts))

    dictionary = corpora.Dictionary(texts)
    dictionary.save('../words.dict')
    print(dictionary)

    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('words.mm', corpus)  # store to disk, for later use

    # LSi model
    model = models.LsiModel(corpus, id2word=dictionary, num_topics=300)
    lsi.save('../model.lsi')
    '''
    model.add_documents(another_tfidf_corpus)  # now LSI has been trained on tfidf_corpus + another_tfidf_corpus
    lsi_vec = model[tfidf_vec]  # convert some new document into the LSI space, without affecting the model

    model.add_documents(more_documents)  # tfidf_corpus + another_tfidf_corpus + more_documents
    lsi_vec = model[tfidf_vec]
    '''


    '''
    word2int = {}
    int2word = {}

    vocab_size = len(words)

    for i,word in enumerate(words):
        word2int[word] = i
        int2word[i] = word

    print(word2int['coca'])
    print(int2word[word2int['coca']])
    '''