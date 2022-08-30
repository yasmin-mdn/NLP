from nltk.tokenize import word_tokenize,sent_tokenize
f = open("Lorem Ipsum.txt", "r")
txt=f.read()
tokens=word_tokenize(txt)
sent=sent_tokenize(txt)
print(tokens)
print(sent)