for index,(image,label) in enumerate(digits.data[0:5],digits.target[0:5]):
    plt.subplot(1,5, index+1)
    plt.imshow(np.reshape(image, (8,8),cmap.cm.gray)
