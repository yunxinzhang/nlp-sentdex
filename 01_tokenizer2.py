import nltk

txt = "Hello, Mr. Zhang. My name is Han Meimei. How are you today?"

tokens = nltk.word_tokenize(txt)
print(tokens)

sent_tokens = nltk.sent_tokenize(txt)
print(sent_tokens)
