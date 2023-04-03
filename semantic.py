# semantic.py
# This work uses spaCy to calculate similarities of among some variables and compares
# the performance in compilation between two spaCy compilers:  'en_core_web_md' and 
# 'en_core_web_sm'

import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car",
            "I\'d like my boat back", "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)

'''
md
0.5929930274321619
0.40415016164997786
0.22358825939615987

sm
0.6770565478895127
0.7276309976205778
0.6806929391210822

When compiled with sm, the similarity values are relatively bigger than the values resulting from
the compilation using md. Also, the similarity between the pairs for md do not correspond to those for sm.  
For example, whilst the similarity between a monkey and a banana measures the highest similarity using sm, the
same comparison records the second highest similarity using the md compilation.  Thus making the
smallest similarity in the md compilation the second highest when compiled with sm.

The results show that the two different compilations are basing the measure of similarity on different
criteria, which according to the error message, is due to the absence of word vectors
'''

