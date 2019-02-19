
#This script conducts some basic natural language processing by opening and then reading the text in a file
#tokenizing in the text, converting all letters into lowercase letters, removing all non-standard characters,
# and removing all stopwords and punctuation.
#Finally, the script returns the 50 most common words in the text, checking for the context of a specific word 
#that was found in the text (in this case "youth"),
#and creating a concordance chart of any word or words found in the text.
#INSTRUCTIONS:
#Edit file name on lines 24 and 45
#Edit each terms on lines 47 and 49
#Edit the language of the text on lines 22 and 34
#NOTE: Stopwords for most European languages are currently supported but use "stopwords.fileids()" to double check.
#As of February, 2019 the following languages were included: ['arabic', 'azerbaijani', 'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'greek', 'hungarian', 'indonesian', 'italian', 'kazakh', 'nepali', 'norwegian', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish', 'turkish']

from urllib import request
import nltk, re, pprint
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import nltk.corpus  
from nltk.text import Text  
set(stopwords.words('english'))
 #imports text file from my machine as "raw" variable 
f=open('FILE PATH','rU')
raw=f.read()

#tokenizing imported text
tokens = word_tokenize(raw)

#creating a list variable ("words") for all words in lowercase
words=[word.lower() for word in tokens if word.isalpha()]

#generating a list of filtered words that excludes stopwords and punctuation marks
filtered_words = [word for word in words if word not in stopwords.words('english')]

#printing the length of the "words" not including stopwords and punctuation marks
len(filtered_words)

#importing all tokens into fdist variable
fdist = FreqDist(filtered_words)
#printing the 50 most common tokens that are not stopwords or punctuation marks
print(fdist.most_common(50))

#creating a text list so word concordance can be checked, note that file must be respecified
textList = Text(nltk.corpus.gutenberg.words('FILE PATH'))
#checking cocordance of a word, eg. "youth"
textList.concordance('youth')
#creating a image of the lexical dispersion of the words in the test
textList.dispersion_plot(["youth"])

