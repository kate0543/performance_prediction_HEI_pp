import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, f1_score

output_folder='csv_files/'
db_data = pd.read_csv(output_folder+'ISDT_dataset_new - Copy.csv')
print(db_data.columns) 

X=db_data.drop(['FINAL Submission Area  [Total Pts: 100 Score] |531746'],axis=1)
for col in X.columns:
       # print(X[col].dtypes)
       if(X[col].dtypes=='object'):
              X[col] = X[col].astype('category')
              X[col] = X[col].cat.codes 
X.to_csv(output_folder+'ISDT_dummies_data.csv')
y=db_data['FINAL Submission Area  [Total Pts: 100 Score] |531746'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=300)
 

rf_clf = RandomForestClassifier()
ada_clf = AdaBoostClassifier(n_estimators=200, random_state=200)
gd_clf = GradientBoostingClassifier(n_estimators=200, random_state=200)

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

rf_f1 = f1_score(y_test, rf_pred, average='macro')
ada_f1 = f1_score(y_test, ada_pred, average='macro')
gd_f1= f1_score(y_test, gd_pred, average='macro')
voting_f1 = f1_score(y_test, voting_pred, average='macro')

print("Random Forest Accuracy:", rf_acc, " f1 score:", rf_f1)
print("AdaBoost Accuracy:", ada_acc, " f1 score:", ada_f1)
print("Gradient Boosting Accuracy:", gd_acc, " f1 score:", gd_f1)
print("Voting Classifier Accuracy:", voting_acc, " f1 score:", voting_f1) 