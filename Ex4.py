from nltk.stem import PorterStemmer

# Small sample text
text = "I love watching cricket"

# Simple tokenization using split()
words = text.split()

# Initialize stemmer
stemmer = PorterStemmer()

# Perform stemming
stemmed_words = []
for word in words:
    stemmed_words.append(stemmer.stem(word))

# Output
print("Original text:", text)
print("Tokenized words:", words)
print("Stemmed words:", stemmed_words)
