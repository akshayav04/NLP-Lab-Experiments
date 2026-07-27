import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')

# User input
text = input("Enter a sentence: ")

# Character Tokenization
tokens = list(text)

# Stemming
stemmer = PorterStemmer()
stemmed_characters = [stemmer.stem(char) for char in tokens]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_characters = [lemmatizer.lemmatize(char) for char in tokens]

# Display results
print("\nOriginal Text:")
print(text)

print("\nCharacter Tokens:")
print(tokens)

print("\nStemmed Characters:")
print(stemmed_characters)

print("\nLemmatized Characters:")
print(lemmatized_characters)

print("\nComparison:")
print("Stemming reduces text to root forms.")
print("Lemmatization converts words to meaningful base forms.")