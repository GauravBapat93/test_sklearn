#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from tools.email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

model = GaussianNB()
t0 = time()



model.fit(features_train,labels_train)

print("training time:", round(time()-t0, 3), "s")
t1 = time()
predict_value = model.predict(features_test)
print("prediction time:", round(time()-t1, 3), "s")
accuracy_score = metrics.accuracy_score(predict_value,labels_test)
print("accuracy : ",accuracy_score)
