import matplotlib.pyplot as plt


n_groups = 10
years = ('1920', '1930', '1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010')
medals = (21, 33, 20, 37, 48, 4, 12, 126, 143, 180)

plt.scatter(years, medals, c='g')
plt.title('Canada Medals over the Years')
plt.xlabel('Years')
plt.ylabel('Medals')
plt.show()