import numpy as np
from matplotlib import pyplot as plt

plt.style.use("seaborn")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

ages_indexes = np.arange(len(ages_x))
bar_width = 0.25

plt.bar(ages_indexes - bar_width, dev_y, width=bar_width, label="All Developers")
plt.bar(ages_indexes, py_dev_y, width=bar_width, label="Python Developers")
plt.bar(ages_indexes + bar_width, js_dev_y, width=bar_width, label="JavaScript Developers")

plt.xticks(ticks=ages_indexes, labels=ages_x)

plt.title("Median Salary (USD) by age")
plt.xlabel("Median Salary (USD")
plt.ylabel("Ages")
plt.tight_layout()
plt.legend()

plt.savefig("bar1.png")

plt.show()
