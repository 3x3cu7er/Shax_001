from sklearn.datasets import load_digits
import matplotlib.pyplot as plt    
import numpy as np  
from sklear.model_selection import train_test_split  
digits = load_digits()

xtest, xtrain, ytest, ytrain = train_test_split(digits.data, digits.target, test_size=.25, random_state=2)

print(xtest)
