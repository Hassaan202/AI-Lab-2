import matplotlib.pyplot as plt
import numpy as np

# Reading the file
file = open("genome.txt")
data = file.read()

# Converting to a list
seqArr = list(data)
seqLen = len(seqArr)

# Plotting using Matplotlib
ax = plt.axes(projection = '3d')
t = np.linspace(0, 4 * np.pi, seqLen) # independent
x = np.cos(t) # dependent
y = np.sin(t) # dependent
coord = np.column_stack((x, y, t)) # gives us coordiates for the plot, not required for plot
colors = {"A":"red", "T":"green", "C":"blue", "G":"yellow"}
seqArr = [colors[x] for x in seqArr]
plt.xlabel("X")
plt.ylabel("Y")
ax.set_zlabel("Z")
ax.scatter(x, y, t, c=seqArr, s=80)
plt.show()