import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from nltk.tag import HiddenMarkovModelTrainer

nltk.download('punkt')
nltk.download('brown')
nltk.download('universal_tagset')

train_data = brown.tagged_sents(tagset='universal')

trainer = HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(train_data)

text = input("Enter a sentence: ")

tokens = word_tokenize(text)

tagged_words = hmm_tagger.tag(tokens)

print("\nTokens:")
print(tokens)
print("\nPOS Tags (HMM):")
for word, tag in tagged_words:
    print(word, "->", tag)

print("\nTag Meanings:")
print("NOUN -> Noun")
print("VERB -> Verb")
print("ADJ -> Adjective")
print("ADV -> Adverb")
print("PRON -> Pronoun")
print("DET -> Determiner")

print("\nTotal Words:", len(tokens))
