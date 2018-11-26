import matplotlib.pyplot as plt


n_groups = 10
years = ('1920', '1930', '1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010')
medals = (27, 57, 16, 56, 42, 36, 46, 69, 136, 161)

plt.scatter(years, medals, c='g')
plt.title('USA Medals over the Years')
plt.xlabel('Years')
plt.ylabel('Medals')
plt.show()