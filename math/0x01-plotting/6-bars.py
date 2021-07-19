#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
"""plot a stacked bar graph"""
np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# your code here
x = ['Farrah', 'Fred', 'Felicia']
y = {'apples': 'red', 'bananas': 'yellow', 'oranges': '#ff8000', 'peaches': '#ffe5b4'}

plt.title('Number of Fruit per Person')
plt.bar(x, fruit[0], color=y['apples'])
plt.bar(x, fruit[1], bottom=fruit[0], color=y['bananas'])
plt.bar(x, fruit[2], bottom=fruit[0]+ fruit[1], color=y['oranges'])
plt.bar(x, fruit[3], bottom=fruit[0]+ fruit[1] + fruit[2], color=y['peaches'])
plt.legend(list(y.keys()))
plt.ylabel("Quantity of Fruit")
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.show()
print(fruit)
