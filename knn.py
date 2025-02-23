import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score, precision_score, confusion_matrix
df = pd.read_csv('diabetes.csv')
print(df['Outcome'].value_counts())

x = df.drop('Outcome', axis=1)
y = df['Outcome']
x = np.array(x)
y = np.array(y)

scaler = StandardScaler()
X = scaler.fit_transform(x)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)

y_pred_train = knn.predict(X_train)
y_pred_test = knn.predict(X_test)

acc_train = accuracy_score(y_train, y_pred_train)
acc_test = accuracy_score(y_test, y_pred_test)

print(acc_test)
print(acc_train)


print(confusion_matrix(y_test, y_pred_test))

p = precision_score(y_test, y_pred_test)
print(p)

r = recall_score(y_test, y_pred_test)
print(r)
