import matplotlib.pyplot as plt
import numpy as np

a = int(input())

def collatz(w):
    x = []
    y = []
    counter = 1
    x.append(counter)
    y.append(w)
    while w!=1:
        counter = counter + 1
        if w%2 == 1:
            w = 3 * w + 1
        else:
            w = w / 2
        x.append(counter)
        y.append(w)
    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title('Collatz Conjecture')



for i in range(1, a+1):
    collatz(i)

plt.show()

