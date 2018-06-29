import numpy;
import random;
import math;
import gensim;
import cPickle
import gzip

def load(file_name):
    # load the model
    stream = gzip.open(file_name, "rb")
    model = cPickle.load(stream)
    stream.close()
    return model


def save(file_name, model):
    # save the model
    stream = gzip.open(file_name, "wb")
    cPickle.dump(model, stream)
    stream.close()

W = load("W_Vec");
Whh = load("Whh_Vec");
B = load("Wb_Vec");
Ws = load("Ws_Vec");
Bs = load("Wsb_Vec");

Hin = numpy.zeros([100,1]);
Hout = numpy.zeros([100,1]);
word_pred = '';
word_pred_vec = numpy.zeros([100,1]);

#After W , Whh, Wb,    Ws , Wsb are read from files

eng_model = gensim.models.Word2Vec.load("eng_wv");
sp_model = gensim.models.Word2Vec.load("sp_wv");

sentence = input('Enter sentence here: ');

words = sentence.strip('\r\n').split(' ');

for i in range(0, len(words)):
	word = words[i];
	X1 = eng_model.wv[word];
	X = X1.reshape(100,1);
	if(i==0):
		X0 = X;

	Ho = numpy.dot(W,X) + numpy.dot(Whh,Hin) + B;
	Hout = 1.0 / (1.0 + numpy.exp(-1.0 * Ho));
	Hin = Hout;


#count = 0;
outArr = [''];

vocab_obj = sp_model.wv.vocab["endsen"];
ind = vocab_obj.index;
flag = 0;

for j in range(0, 20):
	if(j==0):
		X = X0;
	else:
		#Word vector of last predicted word     ----------------------------------------put here
		X = word_pred_vec.reshape(100,1)
		
	Ho = numpy.dot(W,X) + numpy.dot(Whh,Hin) + B;
  	Hout = 1.0 / (1.0 + numpy.exp(-1.0 * Ho));
  	Hin = Hout;


  	#Softmax
	HsIn = Hout;		
	ot = numpy.dot(Ws,HsIn) + Bs;
	soft_ele = numpy.exp(ot - numpy.max(ot));
    HsOut = soft_ele / soft_ele.sum();
	maxInd = HsOut.argmax(axis=0);
	
	if maxInd==ind:
		flag = 1;
		break;
	else:
		word_pred = sp_model.index2word[maxInd]
		word_pred_vec = model.wv[word_pred];
	#---------------------------------------------------------------Get the word vector of MaxInd index and find that word
	outArr.insert(j,word_pred);


if(flag==0 && len(words)+2<=20):
	for w in range(0,len(words)+2):
		print(outArr[w],' ')
else:
	for w in outArr:
		print(w,' ')