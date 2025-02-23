import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

x = np.array([0, 1, 2, 3, 4, 6, 8, 10]).reshape(-1,1)
y = np.array([30000, 40000, 55000, 60000, 70000, 80000, 85000, 87000])


# model
model = DecisionTreeRegressor(max_depth=5 )
model.fit(x,y)

y_predict = model.predict(x)


# plot
plt.plot(x, y, "*")
plt.plot(x, y_predict)
plt.show()