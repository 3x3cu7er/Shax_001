from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt
img = load_sample_image("./china.jpg")
rs = plt.axes(xticks=[], yticks=[])

rs.show(rs)
