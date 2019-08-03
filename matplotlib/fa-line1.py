import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("data2.csv")
ages = data["Age"]
dev_salaries = data["All_Devs"]
py_salaries = data["Python"]
js_salaries = data["JavaScript"]

plt.style.use("fivethirtyeight")

plt.plot(ages, dev_salaries, linestyle="--", color="#444444", label="All Devs")
plt.plot(ages, py_salaries, label="Python Devs")

median_salary = 57287

# plt.fill_between(ages, py_salaries, alpha=0.25)
# plt.fill_between(ages, py_salaries, median_salary, where=(py_salaries > median_salary),
#                  interpolate=True, alpha=0.3)
# plt.fill_between(ages, py_salaries, median_salary, where=(py_salaries <= median_salary),
#                  interpolate=True, alpha=0.3)
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries),
                interpolate=True, alpha=0.3, label="Above Avg")
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries <= dev_salaries),
                interpolate=True, alpha=0.3, label="Below Avg")

plt.legend()
plt.title("Median Salary (USD) by age")
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.tight_layout()

plt.savefig("fa-line1.png")
plt.show()
