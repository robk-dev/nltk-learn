import nltk
import json
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from wordcloud import STOPWORDS
_stop_words = set(STOPWORDS)

stop_words = set(stopwords.words('english'))
stop_words.update(_stop_words, ('thing', 'u', 'us', 'nt'))
lemmatizer = WordNetLemmatizer()

# Read .txt files from ./docs directory into a corpus
corpus=PlaintextCorpusReader('./docs/',".*\.txt")

# filter list of words to remove uneeded ones and punctuation
# losing U.S. which is not ideal, tried splitting sentences on spaces and preserving dots just for it

from nltk.tokenize import TweetTokenizer
tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True)
tokenized = tokenizer.tokenize(corpus.raw())

# drop punctuation
non_punct = list(filter(lambda token: nltk.tokenize.punkt.PunktToken(token).is_non_punct, tokenized))

# lowercase everything
lowercased = [word.lower() for word in non_punct]

# filter stop words
filtered = list(filter(lambda token: token not in stop_words, lowercased))

# lemmatize to get root of words
token_list = [lemmatizer.lemmatize(word) for word in filtered]

# part of speech tag it
pos = nltk.pos_tag(token_list)
# keep nouns, adjectives, verbs, adverbs, cardinal digits
filtered_pos = [x for (x,y) in pos if y in ('NN', 'NNS', 'NNP', 'JJ', 'JJR', 'JJS' 'VB', 'RB', 'CD')]

freq = nltk.FreqDist(filtered_pos)
print(freq.most_common(50))

f = open("./processed/token-list.txt", "w")
f.write(' '.join(list(token_list)))
f.close()

f = open("./processed/pos-filtered.txt", "w")
f.write(' '.join(list(filtered_pos)))
f.close()

# minimized processing with dicts because repeating too much work with loops otherwise
# 150 common_words x 6 fileids x sentences(937 total) x words + append/join sentence into string + 6x search fileids
from nltk.tokenize.treebank import TreebankWordDetokenizer

common_words = dict(freq.most_common(150))
print(common_words)

data = []
hmap = {}
detokenized = {}

for word, frequency in common_words.items():
    datum = { 'word': word, 'frequency': frequency }
    docs = []
    sents = []

    for key, fileid in enumerate(corpus.fileids()):
        if key not in hmap:
            hmap[key] = {}

        for s_id, sentence in enumerate(corpus.sents(fileid)):
            if key in hmap and s_id in hmap[key]:
                words = hmap[key][s_id]
            else:
                words = [lemmatizer.lemmatize(w.lower()) for w in sentence] 
                hmap[key][s_id] = words

            if word in words:
                s_key = f'{key}-{s_id}'
                sent = ''

                if s_key in detokenized:
                    sent = detokenized[s_key]
                else:
                    sent = TreebankWordDetokenizer().detokenize(sentence)
                    detokenized[s_key] = sent
                
                sents.append(sent)
                if fileid not in docs:
                    docs.append(fileid)
    
    datum.update({ 'docs': docs, 'sentences': sents})
    data.append(datum)

print(data[:2])


d = json.dumps(data)
f = open("./processed/data.json", "w")
f.write(d)
f.close()

df = pd.read_json('./processed/data.json')
df.to_csv('./processed/data.csv')