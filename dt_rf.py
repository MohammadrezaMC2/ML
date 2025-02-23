import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('diabetes.csv')
print(df['Outcome'].value_counts())

x = df.drop('Outcome', axis=1)
y = df['Outcome']
x = np.array(x)
y = np.array(y)

scaler = StandardScaler()
X = scaler.fit_transform(x)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

dt = DecisionTreeClassifier(max_depth=8, min_samples_split=4, min_samples_leaf=2)
dt.fit(X_train, y_train)


rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)

y_pred_train_dt = dt.predict(X_train)
y_pred_train_rf = rf.predict(X_train)

acc_train_dt = accuracy_score(y_train, y_pred_train_dt)
print('Decision tree acc: ', acc_train_dt)

acc_train_rf = accuracy_score(y_train, y_pred_train_rf)
print('Random forest acc: ', acc_train_rf)


y_pred_test_dt = dt.predict(X_test)
y_pred_test_rf = rf.predict(X_test)

acc_test_dt = accuracy_score(y_test, y_pred_test_dt)
print('Decision tree acc: ', acc_test_dt)

acc_test_rf = accuracy_score(y_test, y_pred_test_rf)
print('Random forest acc: ', acc_test_rf)




