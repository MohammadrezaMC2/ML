import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df = pd.read_csv('diabetes.csv')
print(df['Outcome'].value_counts())

x = df.drop('Outcome', axis=1)
y = df['Outcome']
x = np.array(x)
y = np.array(y)

scaler = StandardScaler()
X = scaler.fit_transform(x)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
