import matplotlib.pyplot as plt
import numpy as np

n_groups = 1

men = (94)
women = (73)

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.001

opacity = 0.4

ax.bar(index, men, bar_width, alpha=opacity, color='blue', label='Men')
ax.bar(index + bar_width, women, bar_width, alpha=opacity, color='red', label='Women')

ax.set_xlabel('Gender')
ax.set_ylabel('Number of Bronze')
ax.set_title('United States Men and Women:Bronze Medals')
ax.set_xticks(index + bar_width)
ax.set_xticklabels((''))
ax.legend()

fig.tight_layout()
plt.show()