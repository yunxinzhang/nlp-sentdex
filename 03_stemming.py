from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ['walk', 'walking', 'walked', 'walks']
for word in words:
	print(ps.stem(word))

sentence = "I walked in a park. The weather was good. I saw some children playing football. And a dog was chasing a cat."

tokens = word_tokenize(sentence)
for token in tokens:
	print(ps.stem(token))
