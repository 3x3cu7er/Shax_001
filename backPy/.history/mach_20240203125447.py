import matplotlib.pyplot as plt
import numpy as  np  
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

plt.figure(figsize=(20, 4))
digits = load_digits()

# for index, (image, label) in enumerate(zip(digits.data[0:10], digits.target[0:10])):
#     plt.subplot(1, 10, index + 1)
#     plt.imshow(np.reshape(image, (8, 8)), cmap=plt.cm.gray)
# plt.show()

log = LogisticRegression()
xtrain, xtest, ytrain, ytest = train_test_split(digits.data, digits.target, test_size=.25, random_state=2)
log.fit(xtrain, ytrain)
print(log.predict(xtrain.reshape(1, -1)))
