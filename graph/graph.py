import pandas
import matplotlib.pyplot as plt
import numpy as np

df = pandas.read_csv('./DependencyData.csv')

plt.scatter(df['Instability'],df['Abstractness'])
plt.plot(np.linspace(1,0,11),np.linspace(0,1,11))
plt.axis([0, 1, 0, 1])
plt.xlabel('Instability')
plt.ylabel('Abstractness')
plt.show()