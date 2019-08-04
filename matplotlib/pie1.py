from matplotlib import pyplot as plt

plt.style.use("Solarize_Light2")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]
plt.pie(slices, labels=labels, shadow=True, startangle=67,
        explode=explode, autopct="%1.1f%%",
        wedgeprops={'edgecolor': 'white'})

plt.title("Pie Chart")
plt.tight_layout()
plt.savefig("pie1.png")
plt.show()
