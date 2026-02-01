
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
text = "Your Day is not so far"
tokens = word_tokenize(text)
tokens = [word.lower() for word in tokens]
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("Original Text:")
print(text)

print("\nTokens after Stopword Removal:")
print(filtered_tokens)

print("\nTokens after Lemmatization:")
print(lemmatized_tokens)
