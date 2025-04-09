from matplotlib import pyplot as plt

countries=['Africe','North A','Asia','Oceeana','Europa','South A','Soviet']
areas=[11.7,9.4,10.4,3.3,1.9,6.9,7.9]

plt.bar(countries,areas,color=['r','b','y','violet'])
plt.xlabel("Countires")
plt.ylabel("Areas")
plt.ylim(-10,15)
plt.yticks(range(0,15,2))
plt.title("Count/ar")
plt.legend()
plt.show()
