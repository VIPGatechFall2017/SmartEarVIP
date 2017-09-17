from sklearn import linear_model
from sklearn import datasets
import pandas as pd

data = datasets.load_boston()

df = pd.DataFrame(data.data, columns=data.feature_names)

target = pd.DataFrame(data.target, columns=["MEDV"])

X = df
y = target["MEDV"]

lm = linear_model.LinearRegression()
model = lm.fit(X, y)

predictions = lm.predict(X)
print("First five predictions:", predictions[0:5])
print("R-squared score:", lm.score(X,y))
print("Coefficients:", lm.coef_)
print("Intercept:", lm.intercept_)
