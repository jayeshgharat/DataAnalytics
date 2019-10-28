#from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#[height, weight, shoe size]
X = [[181,80,44],[177,70,44],[181,60,44],[181,80,44],[100,80,44],[181,20,44],[160,80,44]]

Y = ['male', 'female', 'male', 'female','male', 'female','male']

#Z = [190,170,43]

print('X:[height, weight, shoe size]\n',X)
print('Y:[height, weight, shoe size]\n',Y)
print()

#DTree = tree.DecisionTreeClassifier() 
DTree = DecisionTreeClassifier() 
DTree = DTree.fit(X,Y)
#predict_DTree = DTree.predict([Z])
predict_DTree = DTree.predict(X)
print ("Output of DecisionTreeClassifier is : ",predict_DTree)
accuracy_DTree = accuracy_score(Y, predict_DTree) * 100
#print('	---Accuracy for DecisionTreeClassifier: {}'.format(accuracy_DTree))
print('	---Accuracy for DecisionTreeClassifier:',accuracy_DTree)
print()

#KNN = KNeighborsClassifier()
KNN = KNeighborsClassifier(n_neighbors = 5)
#KNN.fit(X,Y) #--directly also works
KNN = KNN.fit(X,Y)
#predict_KNN = KNN.predict([Z])
predict_KNN = KNN.predict(X)
print ("Output of KNeighborsClassifier is : ",predict_KNN)
accuracy_KNN = accuracy_score(Y, predict_KNN) * 100
print('	---Accuracy for KNeighborsClassifier:',accuracy_KNN)
print()

LR = LogisticRegression()
LR = LR.fit(X,Y)
#predict_LR = LR.predict([Z])
predict_LR = LR.predict(X)
print ("Output of LogisticRegression is : ",predict_LR)
accuracy_LR = accuracy_score(Y, predict_LR) * 100
print('	---Accuracy for LogisticRegression:',accuracy_LR)
print()

#SGD = SGDClassifier()
SGD = SGDClassifier(loss = 'modified_huber', shuffle=True, random_state=101)
SGD = SGD.fit(X,Y)
#predict_SGD = SGD.predict([Z])
predict_SGD = SGD.predict(X)
print ("Output of SGDClassifier is : ",predict_SGD)
accuracy_SGD = accuracy_score(Y, predict_SGD) * 100
print('	---Accuracy for SGDClassifier:',accuracy_SGD)
print()

Percept = Perceptron()
Percept = Percept.fit(X,Y)
#predict_Percept = Percept.predict([Z])
predict_Percept = Percept.predict(X)
print ("Output of Perceptron is : ",predict_Percept)
accuracy_Percept = accuracy_score(Y, predict_Percept) * 100
print('	---Accuracy for Perceptron:',accuracy_Percept)
print()


GAUSSnb = GaussianNB()
GAUSSnb = GAUSSnb.fit(X,Y)
#predict_GAUSSnb = GAUSSnb.predict([Z])
predict_GAUSSnb = GAUSSnb.predict(X)
print ("Output of GaussianNB is : ",predict_GAUSSnb)
accuracy_GAUSSnb = accuracy_score(Y, predict_GAUSSnb) * 100
print('	---Accuracy for GaussianNB:',accuracy_GAUSSnb)
print()


#RFC = RandomForestClassifier()
RFC = RandomForestClassifier(n_estimators=70, oob_score=True, n_jobs=-1, random_state=101, max_features=None, min_samples_leaf=30)
RFC = RFC.fit(X,Y)
#predict_RFC = RFC.predict([Z])
predict_RFC = RFC.predict(X)
print ("Output of RandomForestClassifier is : ",predict_RFC)
accuracy_RFC = accuracy_score(Y, predict_RFC) * 100
print('	---Accuracy for RandomForestClassifier:',accuracy_RFC)
print()


#SVM = SVC()
SVM = SVC(kernel="linear", C=0.025, random_state=101)
SVM = SVM.fit(X,Y)
#predict_SVM = SVM.predict([Z])
predict_SVM = SVM.predict(X)
print ("Output of SVC is : ",predict_SVM)
accuracy_SVM = accuracy_score(Y, predict_SVM) * 100
print('	---Accuracy for SVC:',accuracy_SVM)
print()

print('-------------------------------------------------------')

# The best classifier from above is
index = np.argmax([accuracy_DTree, accuracy_KNN, accuracy_LR, accuracy_SGD, accuracy_Percept, accuracy_GAUSSnb, accuracy_RFC, accuracy_SVM])
classifiers = {0: 'DTree', 1: 'KNN', 2: 'LR', 3: 'SGD', 4: 'Percept', 5: 'GAUSSnb', 6: 'RFC', 7: 'SVM'}
#print('Best gender classifier is {}'.format(classifiers[index]))
print('Best gender classifier is',classifiers[index])