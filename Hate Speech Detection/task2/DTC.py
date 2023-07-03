import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn import tree
from sklearn.datasets import make_classification
import csv
#preprocessing
def preprocess(line):
  punc='''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
  for ch in line:
    if ch in punc:
      line=line.replace(ch, '')
  line.lower()
  return line
#Subtask:Decision Tree Classifier
cwd=os.getcwd()
os.chdir("..")
cwd1=os.getcwd()
os.chdir(cwd1+"/data")
train_data=pd.read_csv("train.tsv", delimiter='\t', encoding='utf-8', quoting=csv.QUOTE_NONE)
test_data=pd.read_csv("test.tsv", delimiter='\t', encoding='utf-8', quoting=csv.QUOTE_NONE)
os.chdir(cwd1)
train_data['text']=train_data['text'].apply(preprocess)
test_data['text']=test_data['text'].apply(preprocess)
vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(train_data['text'].values.astype('U'))
Y=vectorizer.transform(test_data['text'].values.astype('U'))
clf=tree.DecisionTreeClassifier()
clf.fit(X, train_data['hateful'])
y_pred=clf.predict(Y)
df=pd.DataFrame()
df['id']=test_data['id']
df['hateful']=y_pred
os.chdir(cwd1+"/predictions")
df.to_csv('T2.csv')
os.chdir(cwd1)