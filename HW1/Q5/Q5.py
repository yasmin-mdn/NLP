from nltk.tokenize import TreebankWordTokenizer 
from nltk.stem import *
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag
AlbertEinstein_file = open("AlbertEinstein.txt",encoding="utf8")
AlbertEinstein_txt = AlbertEinstein_file.read()


tokenizer=TreebankWordTokenizer()
AlbertEinstein_tokens = tokenizer.tokenize(AlbertEinstein_txt)
# stems=[]
# stems2=[]
# porter_stemmer = PorterStemmer()
# Lancaster_Stemmer = LancasterStemmer()
# for i in [2,10,18,19,21,22,42]:
#     stem = porter_stemmer.stem(AlbertEinstein_tokens[i]) 
#     stems.append(stem)
#     stem2=Lancaster_Stemmer.stem(AlbertEinstein_tokens[i])
#     stems2.append(stem2)
# idx=0
# print("Stemming using PorterStemmer")
# for i in [2,10,18,19,21,22,42]:
#     print(AlbertEinstein_tokens[i]+"==> %s" %stems[idx])
#     idx+=1
# print("-----------------------------")
# idx=0
# print("Stemming using LancasterStemmer")
# for i in [2,10,18,19,21,22,42]:
#     print(AlbertEinstein_tokens[i]+"==> %s" %stems2[idx])
#     idx+=1


lemmatizer = WordNetLemmatizer()
st="Waves fishing rocks was corpora better ate broken"
words=word_tokenize(st)
print("lemmatize with deafult values")
for word in words:
    lem=lemmatizer.lemmatize(word)
    print(word+"==>%s" %lem)
print("---------------------------")


from collections import defaultdict
tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV


print("lemmatize with giving apropriate POS")
for word,tag in pos_tag(words):
    lem=lemmatizer.lemmatize(word,tag_map[tag[0]])
    print(word+"==>%s" %lem)




