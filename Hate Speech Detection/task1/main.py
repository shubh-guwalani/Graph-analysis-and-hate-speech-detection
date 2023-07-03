import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import spacy
import csv
from sklearn.svm import SVC
import fasttext
#preprocessing
def preprocess(line):
  punc='''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
  for ch in line:
    if ch in punc:
      line=line.replace(ch, '')
  line.lower()
  return line
#Subtask1
cwd=os.getcwd()
os.chdir("..")
cwd1=os.getcwd()
os.chdir(cwd1+"/data")
train_data=pd.read_csv("train.tsv", delimiter='\t', encoding='utf-8', quoting=csv.QUOTE_NONE)
test_data=pd.read_csv("test.tsv", delimiter='\t', encoding='utf-8', quoting=csv.QUOTE_NONE)
os.chdir(cwd1)
train_data['text']=train_data['text'].apply(preprocess)
test_data['text']=test_data['text'].apply(preprocess)
vectorizer=TfidfVectorizer(max_df=0.80, min_df=5, lowercase=True)
X=vectorizer.fit_transform(train_data['text'].values.astype('U'))
Y=vectorizer.transform(test_data['text'].values.astype('U'))
clf=RandomForestClassifier()
clf.fit(X, train_data['hateful'])
y_pred=clf.predict(Y)
df=pd.DataFrame()
df['id']=test_data['id']
df['hateful']=y_pred
os.chdir(cwd1+"/predictions")
df.to_csv('RF.csv')
os.chdir(cwd1)
#Subtask2
nlp=spacy.load("en_core_web_sm")
def vec(line):
	return nlp(line).vector
train_data['sp']=train_data['text'].apply(vec)
y=test_data['text'].apply(vec)
X=train_data.sp
Y=train_data.hateful
clf=SVC(kernel='rbf')
clf.fit(list(X), Y)
y_pred=clf.predict(list(y))
df=pd.DataFrame()
df['id']=test_data['id']
df['hateful']=y_pred
os.chdir(cwd1+"/predictions")
df.to_csv('SVM.csv')
os.chdir(cwd1)
#Subtask3
os.chdir(cwd)
train_data['text']=train_data['text'].apply(preprocess)
test_data['text']=test_data['text'].apply(preprocess)
train_data['hateful']=['__label__'+str(s) for s in train_data['hateful']]
train_data.to_csv('/home/aashish/Documents/Assignment_3/task1/training.txt',columns=['hateful','text'],index=False,header=None)
model=fasttext.train_supervised('training.txt')
test_data.to_csv('/home/aashish/Documents/Assignment_3/task1/testing.txt',columns=['text'],index=False,header=None)
f=open('testing.txt', 'r', encoding="utf-8")
y_pred=[]
read=f.readlines()
for line in read:
	y_pred.append(model.predict(line[:-2]))
y_pred=[str(y_pred[i][0]) for i in range(0,5000)]
df=pd.DataFrame()
df['id']=test_data['id']
df['hateful']=y_pred
os.chdir("..")
os.chdir(cwd1+"/predictions")
df.to_csv('FT.csv')
os.chdir(cwd1)
os.chdir(cwd)
#End of code