from matplotlib import pyplot as plt

ages_x = range(25, 36)

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316,
         64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998,
             70003, 70000, 71496, 75370, 83640]

js_dev_y= [37810, 43515, 46823, 49293, 53437, 56737, 62375,
           66674, 68754, 68746, 74583]

plt.plot(ages_x, py_dev_y, color="#5a7d9a", linewidth=3, label="Python Devs")

plt.plot(ages_x, js_dev_y, color="#adad3b", linewidth=3, label="JavaScript Devs")

plt.plot(ages_x, dev_y, color="#444444", linestyle='--', label="All Devs")
         
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.title("Median Salary (USD) by age")

plt.grid(True)

plt.legend()

plt.show()