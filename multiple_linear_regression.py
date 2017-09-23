##http://scikit-learn.org/stable/auto_examples/plot_cv_predict.html#sphx-glr-auto-examples-plot-cv-predict-py
##https://medium.com/towards-data-science/simple-and-multiple-linear-regression-in-python-c928425168f9

from sklearn import linear_model
from sklearn.model_selection import cross_val_predict
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

data = datasets.load_boston()

df = pd.DataFrame(data.data, columns=data.feature_names)

target = pd.DataFrame(data.target, columns=["MEDV"])

X = df
y = target["MEDV"]

lm = linear_model.LinearRegression()
model = lm.fit(X, y)


predictions = lm.predict(X)
predicted = cross_val_predict(lm, data.data, y, cv=10)

print("First five predictions:", predictions[0:5])
print("R-squared score:", lm.score(X,y))
print("Coefficients:")
for x in range(0,12):
    print([data.feature_names[x],lm.coef_[x]])
print("Intercept:", lm.intercept_)

fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0,0,0))
ax.plot([y.min(),y.max()],[y.min(),y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
