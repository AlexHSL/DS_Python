from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

# str = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude. "
print(sent_tokenize(mytext))

print(word_tokenize(mytext,"english"))
print(word_tokenize(mytext))

# 定义
from nltk.corpus import wordnet
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())
syn = wordnet.synsets("NLP")
print(syn[0].definition())
syn = wordnet.synsets("Python")
print(syn[0].definition())

# 同义词
synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(synonyms)

# 反义词
antonyms = []
for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)
# 词干
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem('working'))
print(stemmer.stem('worked'))

from nltk.stem import SnowballStemmer

french_stemmer = SnowballStemmer('french')

print(french_stemmer.stem("French word"))

from nltk.stem import WordNetLemmatizer

# 变体还原
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('playing', pos="v"))
print(lemmatizer.lemmatize('playing', pos="n"))
print(lemmatizer.lemmatize('playing', pos="a"))
print(lemmatizer.lemmatize('playing', pos="r"))