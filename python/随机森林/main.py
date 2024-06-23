from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

wine = load_wine()

x_train,x_test,y_train,y_test = train_test_split(wine.data,wine.target,test_size=0.3)

clf = DecisionTreeClassifier(random_state=0)
rfc = RandomForestClassifier(random_state=0)
clf = clf.fit(x_train,y_train)
rfc = rfc.fit(x_train,y_train)
score_c = clf.score(x_test,y_test)
score_r = rfc.score(x_test,y_test)

