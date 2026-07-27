import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
text=input("Enter a sentence: ")
sentence=sent_tokenize(text)

text=input("Enter a Sentence: ")
tokens=word_tokenize(text)
stemmer=PorterStemmer()
stemmed_words=[stemmer.stem(word) for word in tokens]

lemmatizer=WordNetLemmatizer()
lemmatized_words=[lemmatizer.lemmatize(word) for word in  tokens]

print("\nOriginal Text:")
print(text)
print("\nSentence:")
for i,sentence in enumerate(sentence,1):
    print(f"{i}.{sentence}")

print("\nTokens:")
print(tokens)

print("\nStemmed Words:")
print(stemmed_words)
print("\nLemmatized Words:")
print(lemmatized_words)


print("\nComparison:")
print("Stemming reduces words to root forms, which may not be meaningful.")
print("Lemmatization converts words to meaningful base forms.")