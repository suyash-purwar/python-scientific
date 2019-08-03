import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

lang_x = []
usercount_y = []

# USING CSV MODULE
# with open("data.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     lang_counter = Counter()
#
#     for row in csv_reader:
#         lang_counter.update(row["LanguagesWorkedWith"].split(";"))
#

# USING PANDAS MODULE
data = pd.read_csv("data.csv")
lang_responses = data['LanguagesWorkedWith']
lang_counter = Counter()

for response in lang_responses:
    lang_counter.update(response.split(";"))

for item in lang_counter.most_common(15):
    lang_x.append(item[0])
    usercount_y.append(item[1])

lang_x.reverse()
usercount_y.reverse()

plt.style.use("fivethirtyeight")

plt.barh(lang_x, usercount_y)

plt.title("Programming Language Users")
plt.xlabel("Users")

plt.tight_layout()

plt.savefig("bar2.png")
plt.show()