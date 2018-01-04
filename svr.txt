import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import time

SIZE = 20
TEST_SIZE = 0.1

# #############################################################################
# Pull data
images = 'hand.csv'
fingers = 'data.csv'

# start = time.time()    # start time of program

df = pd.read_csv(images)
target = pd.read_csv(fingers, names=[0,1,2,3,4])

# cut down size if needed
if SIZE >= 0:
	df = df.iloc[0:SIZE]
	target = target.iloc[0:SIZE]

# print("finished reading", time.time() - start)

fing = target[2]    # selects only the middle finger

X_train, X_test, y_train, y_test = train_test_split(   # splits data
	df, fing, test_size=TEST_SIZE, random_state=0)
# print("split", time.time() - start)


# start = time.time()

# #############################################################################
# Fit regression model

deg = 4

# svr_rbf = SVR(kernel='rbf', C=1e2, gamma=0.3).fit(X_train, y_train)
svr_poly = SVR(kernel='poly', C=1e2, degree=deg).fit(X_train, y_train)

# print("SVR", time.time() - start)
# start = time.time()

print("DEG:", deg)
print(svr_poly.score(X_train, y_train))
print(svr_poly.score(X_test, y_test))
print(svr_poly.score(df, fing))


# print("END", time.time() - start)