import matplotlib.pyplot as plt 
import numpy as np 

labels = "Bronze", "Silver", "Gold"
sizes = [17.12, 32.48, 50.4]
colors = ['darkgoldenrod', 'darkgray', 'gold']
explode = [0.1, 0, 0]

plt.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medal Count")
plt.xlabel("Canada")
plt.show()
