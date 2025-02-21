from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
irisArr = np.array(iris.data)
irisTarget = np.array(iris.target)

meanVals = np.mean(irisArr, axis=0)
print("Means: ", meanVals)
medianVals = np.median(irisArr, axis=0)
print("Medians: ", medianVals)
stdDevVals = np.std(irisArr, axis=0)
print("Standard Deviations: ", stdDevVals)

sepalLenArr = [arr[0] for arr in irisArr]
sepalWidthArr = [arr[1] for arr in irisArr]
petalLenArr = [arr[2] for arr in irisArr]
petalWidthArr = [arr[3] for arr in irisArr]
plt.scatter(sepalLenArr, sepalWidthArr, c="blue")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter Plot")
plt.show()

ax = plt.axes()
ax.hist(sepalLenArr, edgecolor="black")
plt.title("Histogram - Sepal length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

plt.plot(petalLenArr, petalWidthArr)
plt.title("Line Plot")
plt.xlabel("Petal Lengths")
plt.ylabel("Petal Widths")
plt.show()