#from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

#[height, weight, shoe size]
X = [[181,80,44],[177,70,44],[181,60,44],[181,80,44],[100,80,44],[181,20,44],[160,80,44]]

Y = ['male', 'female', 'male', 'female','male', 'female','male']

#DTree = tree.DecisionTreeClassifier() 
DTree = DecisionTreeClassifier() 
DTree = DTree.fit(X,Y)
predict_DTree = DTree.predict([[190,170,43]])
print ("Output of DecisionTreeClassifier is : ",predict_DTree)

#KNN = KNeighborsClassifier()
KNN = KNeighborsClassifier(n_neighbors = 5)
#KNN.fit(X,Y) #--directly also works
KNN = KNN.fit(X,Y)
predict_KNN = KNN.predict([[190,170,43]])
print ("Output of KNeighborsClassifier is : ",predict_KNN)

LR = LogisticRegression()
LR = LR.fit(X,Y)
predict_LR = LR.predict([[190,170,43]])
print ("Output of LogisticRegression is : ",predict_LR)

#SGD = SGDClassifier()
SGD = SGDClassifier(loss = 'modified_huber', shuffle=True, random_state=101)
SGD = SGD.fit(X,Y)
predict_SGD = SGD.predict([[190,170,43]])
print ("Output of SGDClassifier is : ",predict_SGD)

GAUSSnb = GaussianNB()
GAUSSnb = GAUSSnb.fit(X,Y)
predict_GAUSSnb = GAUSSnb.predict([[190,170,43]])
print ("Output of GaussianNB is : ",predict_GAUSSnb)

#RFC = RandomForestClassifier()
RFC = RandomForestClassifier(n_estimators=70, oob_score=True, n_jobs=-1, random_state=101, max_features=None, min_samples_leaf=30)
RFC = RFC.fit(X,Y)
predict_RFC = RFC.predict([[190,170,43]])
print ("Output of RandomForestClassifier is : ",predict_RFC)