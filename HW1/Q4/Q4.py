from enum import unique
import numpy as np
from nltk.tokenize import TreebankWordTokenizer , RegexpTokenizer , WhitespaceTokenizer,WordPunctTokenizer
Shahnameh_file = open("Shahnameh.txt",encoding="utf8")
AlbertEinstein_file = open("AlbertEinstein.txt",encoding="utf8")
ShortSampleEnglish_file = open("ShortSampleEnglish.txt",encoding="utf8")
ShortSamplePersian_file = open("ShortSamplePersian.txt",encoding="utf8")

Shahnameh_txt = Shahnameh_file.read()
AlbertEinstein_txt = AlbertEinstein_file.read()
ShortSampleEnglish_txt = ShortSampleEnglish_file.read()
ShortSamplePersian_txt = ShortSamplePersian_file.read()


#پ
tokenizer=TreebankWordTokenizer()
ShortSampleEnglish_tokens= tokenizer.tokenize(ShortSampleEnglish_txt)
ShortSamplePersian_tokens = tokenizer.tokenize(ShortSamplePersian_txt)
Shahnameh_tokens = tokenizer.tokenize(Shahnameh_txt)
AlbertEinstein_tokens = tokenizer.tokenize(AlbertEinstein_txt)
print("ShortSampleEnglish:%d Tokens "  %len(ShortSampleEnglish_tokens))
print("number of types:",len(np.unique(ShortSampleEnglish_tokens)))
print("types:",np.unique(ShortSampleEnglish_tokens))
print("------------------------------------------------")
print("ShortSamplePersian:%d Tokens "  %len(ShortSamplePersian_tokens))
print("number of types:",len(np.unique(ShortSamplePersian_tokens)))
print("types:",np.unique(ShortSamplePersian_tokens))
print("--------------------------------------------------")
print("Shahnameh:%d Tokens "  %len(Shahnameh_tokens))
print("number of types:",len(np.unique(Shahnameh_tokens)))
print("types:",np.unique(Shahnameh_tokens))
print("--------------------------------------------------")
print("AlbertEinstein:%d Tokens "  %len(AlbertEinstein_tokens))
print("number of types:",len(np.unique(AlbertEinstein_tokens)))
print("types:",np.unique(AlbertEinstein_tokens))

#ت
regex_tokenizer=RegexpTokenizer('\w+|\$[\d\.]+|\S+')
num_regex_tokenizer=RegexpTokenizer('[0-9]+')
ShortSampleEnglish_Tokens_regex=regex_tokenizer.tokenize(ShortSampleEnglish_txt)
ShortSamplePersian_Tokens_regex=regex_tokenizer.tokenize(ShortSamplePersian_txt)
AlbertEinstein_number_Tokens_regex=num_regex_tokenizer.tokenize(AlbertEinstein_txt)
print(AlbertEinstein_number_Tokens_regex)
print(ShortSampleEnglish_Tokens_regex)
print(ShortSamplePersian_Tokens_regex)

#ث
Whitespace_tokenizer= WhitespaceTokenizer()
ShortSampleEnglish_Whitespace_tokens=Whitespace_tokenizer.tokenize(ShortSampleEnglish_txt)
whitespace_regex_tokenizer=RegexpTokenizer('\S+')
ShortSampleEnglish_Tokens_whitespace_with_regex=whitespace_regex_tokenizer.tokenize(ShortSampleEnglish_txt)
print(ShortSampleEnglish_Whitespace_tokens)
print(ShortSampleEnglish_Tokens_whitespace_with_regex)


#WordPunctTokenizer  
WordPunct_tokenizer=WordPunctTokenizer()
ShortSampleEnglish_wordpunc_tokens=WordPunct_tokenizer.tokenize(ShortSampleEnglish_txt)
print(ShortSampleEnglish_wordpunc_tokens)