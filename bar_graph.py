import matplotlib.pyplot as plt

countries=['Africe','North America','Asia','Oceana','Europa','South America','Soviet Union']
areas=[11.7,9.4,10.4,3.3,1.9,6.9,7.9]

plt.bar(countries, areas)
plt.xlabel('Countries')
plt.ylabel('Area (millions of square kilometers)')
plt.title('Area of Continents')
plt.legend()
plt.grid(True)
plt.show()
