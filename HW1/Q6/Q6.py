import re
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from nltk import Counter
from wordcloud import WordCloud
file=open('final.csv',"w", encoding="utf8")
headers = ['Befor', 'After']
writer = csv.writer(file)
writer.writerow(headers)
def make_wordcloud(data,title=None):
    wordcloud = WordCloud(
        background_color='pink',
        width=400,
        height=200,
        max_words=200,
        scale=2,
        random_state=1  
    ).generate(str(data))

    fig = plt.figure(figsize=(10, 10))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)

    plt.imshow(wordcloud)
    plt.savefig('cloud.png')
    plt.show()
stop_words = stopwords.words('english')
porter = PorterStemmer()
tweets=[]
all_hashtags=[]
file = open("tweets.csv",encoding="utf8")
csv_txt = csv.reader(file, delimiter=',')
tweets =[data[0] for data in csv_txt] 
total_tok = []
num_tweets = 0
for tweet in tweets:
    tweet=re.sub(r"@\w+", '', tweet)
    tweet=tweet.lower()
    hashtags=[tag for tag in re.findall(r"#(\w+)", tweet)]
    tokens= [tok for tok in word_tokenize(tweet) if tok.isalpha() and tok not in stop_words and len(tok) >= 3]
    stemmed_tokens = [porter.stem(token) for token in tokens]
    writer.writerow([tweet,' '.join(stemmed_tokens)])
    total_tok += tokens
    if len(hashtags)>0:
        all_hashtags+=hashtags
    num_tweets += 1
    if num_tweets > 20000:
        break

Comon_tags=Counter(all_hashtags).most_common(10)
Comon_words=Counter(total_tok).most_common(100)
commonwords_cloud=[t[0] for t in Comon_words]
print("Comon_tags:", Comon_tags)
print("Comon_words:",Comon_words)
make_wordcloud(' '.join(commonwords_cloud), 'Common words')

