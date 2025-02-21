import matplotlib.pyplot as plt

group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15, 40, 45, 50, 62]
group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]

plt.boxplot(group_A)
plt.title("Box Plot for Group A")
plt.xlabel("A")
plt.ylabel("Distribution")
plt.grid(True)
plt.show()

plt.boxplot(group_B)
plt.title("Box Plot for Group B")
plt.xlabel("B")
plt.ylabel("Distribution")
plt.grid(True)
plt.show()

plt.subplot(1, 2, 1)
plt.plot(group_A)
plt.title("Group A")
plt.subplot(1, 2, 2)
plt.plot(group_B)
plt.title("Group B")
plt.suptitle("Sub-plots for Group Data")
plt.show()
