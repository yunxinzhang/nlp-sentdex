from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import time
txt = "This is an example showing off stop word filtration."

tokens = word_tokenize(txt)
print(tokens)
stop_words = set(stopwords.words("english"))
#print(stop_words)
st = time.time()
filted_tokens = []
for token in tokens:
	if token not in stop_words:
		filted_tokens.append(token)
print( (time.time()-st)*1000 ,'ms')
print(filted_tokens)

st = time.time()
filted_tokens2 = [ w for w in tokens if w not in stop_words ]

print( (time.time()-st)*1000 ,'ms')
print(filted_tokens2)
