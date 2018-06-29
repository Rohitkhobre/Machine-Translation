import numpy;
import random;
import math;
import gensim;

sentences = gensim.models.word2vec.LineSentence('english.txt')
model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
model.save("eng_wv")

sentences = gensim.models.word2vec.LineSentence('spanish.txt')
model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
model.save("sp_wv")
