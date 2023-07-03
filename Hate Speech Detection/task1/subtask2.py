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
#Subtask2
cwd=os.getcwd()
os.chdir("..")
cwd1=os.getcwd()
os.chdir(cwd1+"/data")
train_data=pd.read_csv("train.tsv", delimiter='\t', encoding='utf-8', quoting=csv.QUOTE_NONE)
test_data=pd.read_csv("test.tsv", delimiter='\t', encoding='utf-8', quoting=csv.QUOTE_NONE)
os.chdir(cwd1)
train_data['text']=train_data['text'].apply(preprocess)
test_data['text']=test_data['text'].apply(preprocess)
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