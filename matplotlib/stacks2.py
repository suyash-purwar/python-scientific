from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

employee1 = [8, 6, 5, 5, 4, 2, 1, 1, 2]
employee2 = [0, 1, 2, 2, 2, 4, 4, 4, 3]
employee3 = [0, 1, 1, 1, 2, 2, 3, 3, 3]

labels = ["Suyash", "Shubham", "Ashish"]
colors = ['#1565C0', '#f5af19', '#FC466B']

plt.stackplot(minutes, employee1, employee2, employee3, labels=labels, colors=colors)

plt.title("Team Performance")
plt.legend(loc=(0.07, 0.05))
plt.tight_layout()

plt.savefig("stack2.png")
plt.show()
