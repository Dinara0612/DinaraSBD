from sklearn.ensemble import RandomForestClassifier
import joblib

X = [[0,0, 0], [0,0,1],[1,1,0],[0,1, 1]]
Y = ['o','o',"ii", "ii"]
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, Y)

print(clf.predict([[0,1,1]]))

joblib.dump(clf, "rf.clf")  


