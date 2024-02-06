import matplotlib.pyplot as plt
import numpy as  np  
from sklearn.datasets import load_digits
plt.figure(20, 8)
digits = load_digits()
for index, (image, label) in enumerate(digits.data[0:5], digits.target[0:5]):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (8, 8), cmap.cm.gray))
