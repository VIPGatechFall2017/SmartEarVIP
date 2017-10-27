from sklearn import linear_model
from sklearn.model_selection import cross_val_predict
import pandas as pd;
import matplotlib.pyplot as plt

images = 'hand.csv'
fingers = 'data.csv'

df = pd.read_csv(images)
target = pd.read_csv(fingers,names=[0,1,2,3,4])

df = df.iloc[0:2888]
target = target.iloc[0:2888]

fing = target[2] ##[0:thumb,1:pointer,2:middle,3:ring,4:pinky] for right hand

lm = linear_model.LinearRegression()
model = lm.fit(df,fing)

predictions = lm.predict(df)
predicted = cross_val_predict(lm,df,fing,cv=10)
predicted = (predicted-predicted.min())/(predicted.max()-predicted.min())*100;


print("First five predictions:", predictions[0:5])
print("R-squared score:", lm.score(df,fing))
##### idea: pay attention to clusters that are very strongly correlated with
##### flex values for optimization
print("Intercept:", lm.intercept_)

fig, ax = plt.subplots()
ax.scatter(fing,predicted,edgecolors=(0,0,0))
ax.plot([fing.min(),fing.max()],[fing.min(),fing.max()],'k--',lw=4)
ax.set_xlabel('Measured (actual flex value)')
ax.set_ylabel('Predicted (model prediction for flex value)')
plt.show()
