from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.corpus import words
correct_words = words.words()
incorrect_words=['looove', 'correct', 'happpy']
for word in incorrect_words:
    temp = [(jaccard_distance(set(ngrams(word, 2)),
                              set(ngrams(w, 2))),w)
            for w in correct_words if w[0]==word[0]]
    print(sorted(temp, key = lambda val:val[0])[0][1])