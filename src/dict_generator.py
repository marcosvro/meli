import pandas as pd

def generate_dict ():
    a = pd.read_csv('../train.csv', usecols=['title', 'label_quality', 'language', 'category'] , encoding='utf-8')
    _set = {'livro'}
    i = 0
    for title in a['title'].tolist():
        for word in title.split(' '):
            try:
                if word[-1] == ',' or word[-1] == ')' or word[-1] == ']' or word[-1] == '>' or word[-1] == '|':
                    word = word[:-1]
                if word[0] == ',' or word[0] == '(' or word[0] == '[' or word[0] == '<' or word[0] == '|':
                    word = word[1:]
            except Exception:
                pass
            
            if len(word) > 1:
                _set.add(word.lower())
                i += 1
    

    df = pd.DataFrame(_set)
    df.to_csv('word_dict.csv')
    return _set

if __name__ == '__main__':
    words = generate_dict()
    print(len(words))
