import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

db_data = pd.read_csv('ISDT_bb_dataset.csv')
print(db_data.columns)

# X = db_data.drop(['Latest Grade', 'Numeric Grade', 'Component Grade', 'Component Grade Letter'], axis=1)
# X = pd.get_dummies(X)
# y = db_data['Latest Grade']

X=db_data.drop(['Last Name', 'First Name', 'Username', 'Student ID','FINAL Submission Area  [Total Pts: 100 Score] |531746'],axis=1)
print(X.columns)
X = pd.get_dummies(X)

y=db_data['FINAL Submission Area  [Total Pts: 100 Score] |531746']
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_clf = RandomForestClassifier()
ada_clf = AdaBoostClassifier(n_estimators=200, random_state=42)
gd_clf = GradientBoostingClassifier(n_estimators=200, random_state=42)

rf_clf.fit(X_train, y_train)
ada_clf.fit(X_train, y_train)
gd_clf.fit(X_train, y_train)

voting_clf = VotingClassifier(estimators=[("rf", rf_clf), ("ada", ada_clf), ("gd", gd_clf)], voting="hard")
voting_clf.fit(X_train, y_train)

rf_pred = rf_clf.predict(X_test)
ada_pred = ada_clf.predict(X_test)
gd_pred = gd_clf.predict(X_test)
voting_pred = voting_clf.predict(X_test)

rf_acc = accuracy_score(y_test, rf_pred)
ada_acc = accuracy_score(y_test, ada_pred)
gd_acc = accuracy_score(y_test, gd_pred)
voting_acc = accuracy_score(y_test, voting_pred)

print("Random Forest Accuracy:", rf_acc)
print("AdaBoost Accuracy:", ada_acc)
print("Gradient Boosting Accuracy:", gd_acc)
print("Voting Classifier Accuracy:", voting_acc)
