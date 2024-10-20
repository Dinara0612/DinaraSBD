import joblib
rf1=joblib.load("rf.clf")

print(rf1.predict([[0,1,1]]))
