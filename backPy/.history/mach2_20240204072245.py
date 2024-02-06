from sklearn.datasets import load_digits
import matplotlib.pyplot as plt    
import numpy as np  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
digits = load_digits()

xtest, xtrain, ytest, ytrain = train_test_split(digits.data, digits.target, test_size=.25, random_state=2)

print(xtest)

log = LogisticRegression()
log.fit(xtrain, ytrain)
prediction = log.predict(xtrain)
corr = []

print(prediction)
index = 0
for predict, actual in zip(prediction, ytest):
    if predict == actual:
        corr.append(index)
    index += 1
    
print(corr)

plt.figure(figsize=(20, 5))

for plotid, var in enumerate(corr[:5]):
    plt.subplot(1, 5, plotid + 1)
    plt.imshow(np.reshape(xtest[var], (8, 8)), cmap=plt.cm.gray)
plt.show()
