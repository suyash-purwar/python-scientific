import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data4.csv')
views = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(views, likes, c=ratio, cmap='summer', edgecolor='black', linewidth=1)
cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ration')

plt.xscale('log')
plt.yscale('log')

plt.title("Correlation between views and likes of trending 200 videos on Youtube")
plt.xlabel("Views")
plt.ylabel("Likes")

plt.tight_layout()

plt.savefig("scatterplot2.png")
plt.show()
