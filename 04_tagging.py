import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_txt = state_union.raw('2005-GWBush.txt')
test_txt = state_union.raw('2006-GWBush.txt')


# nltk.help.upenn_tagset() 
sent_tokenizer = PunktSentenceTokenizer(train_txt)
tokens = sent_tokenizer.tokenize(test_txt)

try:
	for token in tokens:
		words = nltk.word_tokenize( token )
		tagged = nltk.pos_tag(words)
		print(tagged)
except Exception as e:
	print( str(e))

