from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['player1', 'player2', 'player3']
colors = ['#1565C0', '#f5af19', '#FC466B']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc="upper left")
plt.title("Stack Plot")
plt.tight_layout()
plt.savefig("stack1.png")
plt.show()
