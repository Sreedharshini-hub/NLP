from nltk import ngrams

sentence = input("Enter a sentence: ")
n = int(input("Enter the value of n: "))

print("\n Word n-grams")
words = sentence.split()
word_ngrams = ngrams(words, n)

for gram in word_ngrams:
    print(gram)

print("\n Character n-grams")
char_ngrams = ngrams(sentence, n)

for gram in char_ngrams:
    print("".join(gram))


