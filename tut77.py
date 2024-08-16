import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error
iris=datasets.load_iris()
iris_x=iris.data[:,np.newaxis,2]
iris_X_train=iris_x[:-30]
iris_X_test=iris_x[-20:]
iris_Y_train=iris.target[:-30]
iris_Y_test=iris.target[-20:]
model=linear_model.LinearRegression()
model.fit(iris_X_train,iris_Y_train)
iris_Y_predicted=model.predict(iris_X_test)
print("Weights: ",model.coef_)
print("Intercept: ",model.intercept_)
plt.scatter(iris_X_test,iris_Y_test)
plt.plot(iris_X_test,iris_Y_predicted)
plt.show()