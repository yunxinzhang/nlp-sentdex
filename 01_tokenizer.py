from nltk.tokenize import sent_tokenize, word_tokenize

txt = "Hello, Mr. Han, how are you today? The weather is good."

print( sent_tokenize(txt) )
print()
print( word_tokenize(txt) )

txt = "你好，我是中国人."

print( word_tokenize(txt) )
