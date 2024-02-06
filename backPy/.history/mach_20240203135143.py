import matplotlib.pyplot as plt
import numpy as  np  
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix 

plt.figure(figsize=(20, 4))
digits = load_digits()

# for index, (image, label) in enumerate(zip(digits.data[0:10], digits.target[0:10])):
#     plt.subplot(1, 10, index + 1)
#     plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
# plt.show()

log = LogisticRegression()
xtrain, xtest, ytrain, ytest = train_test_split(digits.data, digits.target, test_size=.25, random_state=2)
log.fit(xtrain, ytrain)
print(log.predict(xtest[0].reshape(1, -1)))
prediction = log.predict(xtest)

score = log.score(xtest, ytest)

cm = confusion_matrix (ytest, prediction)
# print(prediction)

accuracy = []
index = 0
for predict, actual in zip(prediction, ytest):
    if predict == actual:
        accuracy.append(index)
    index += 1

# print(accuracy)
plt.figure(figsize=(20, 5))
for plotid, wrg in enumerate(accuracy[:5]):
    plt.subplot(1, 5, plotid + 1)
    plt.imshow(np.reshape(xtest[wrg], (8, 8)), cmap=plt.cm.gray)
    plt.title(f"Prediction: {prediction[wrg]} actual :{wrg}")

plt.show()
