import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from spacy.language import Language

# ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'
# # Extraction of Part of Speech Tags
# def preprocess(sentence):
#     sentence = nltk.word_tokenize(sentence)
#     sentence = nltk.pos_tag(sentence)
#     return sentence
#
# # preprocess(ex)

# -------------------------------Spacy
from bs4 import BeautifulSoup
import requests
import re
from nltk.corpus import stopwords
from collections import Counter
# "css-exrw3m evys1bk0"
url = "https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news"
res = requests.get(url)
html = res.content
soup = BeautifulSoup(html, 'html5lib')
entered_attr = input("enter attribute:")
t = soup.findAll("p",attrs={"class": entered_attr})

all_text = ""
all_occured = ""
for te in t:
    # split_it = te.text.split()
    # counter = Counter(split_it)
    # most_occured = counter.most_common(10)
    all_text += te.text

splt = all_text.split()


count = Counter(splt)
occur = count.most_common(10)
# print(all_text, occur)
stop = stopwords.words('english')
remove_stop = [word for word in splt if word not in stop]
# print(remove_stop)

text = "fjh3///./''1!@"
text = re.sub(r'[^\w\s]','',text)
print(text)
    # print(te.text, "\n","Most occured words here are: ", most_occured)
    # print(Counter(te).most_common(3))

# # split() returns list of all the words in the string
# split_it = data_set.split()
#
# # Pass the split_it list to instance of Counter class.
# Counter = Counter(split_it)
#
# # most_common() produces k frequently encountered
# # input values and their respective counts.
# most_occur = Counter.most_common(4)
#
# print(most_occur)
# ////////////////////////////////////////////////////////////
