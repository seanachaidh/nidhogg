import nltk

alicetext = '''ALICE was beginning to get very tired of sitting by her
sister on the bank, and of having nothing to do: once or twice she had
peeped into the book her sister was reading, but it had no pictures or
conversations in it, "and what is the use of a book," thought Alice,
"without pictures or conversations?"'''


tokenized = nltk.word_tokenize(alicetext)
tags = nltk.pos_tag(tokenized)


print('sentence:', alicetext)
print('tokens:', tokenized)
print('tags:', tags)
