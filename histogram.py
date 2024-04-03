import matplotlib.pyplot as plt

edges=[135,140,145,150,155]
heights=[4,12,16,8]

plt.hist(edges[:-1], bins=edges,weights=heights, edgecolor='black', color='red')
plt.xlabel('Heights')
plt.ylabel('No of Students')
plt.title('Histogram of Heights')
plt.show()
