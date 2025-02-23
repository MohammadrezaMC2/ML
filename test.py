import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from  sklearn.metrics import confusion_matrix, precision_score, recall_score
df = pd.read_csv('academic_performance_dataset_V2.csv')
print(df.head())

x = df.drop('score', axis=1)
y = df['score']
x = np.array(x)
y = np.array(y)

scaler = StandardScaler()
X = scaler.fit_transform(x)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

acc_train = accuracy_score(y_true=y_train, y_pred=y_pred_train)
acc_test = accuracy_score(y_true=y_test, y_pred=y_pred_test)

print(acc_train)
print(acc_test)


