# PLOTTING (with matplotlib)

import matplotlib.pyplot as plt
import random

'''

plt.figure(1)  # creates a new window

plt.plot([1, 2, 4, 4])  # plots y and x against the index
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # plot(x_data, y_data)

'''

plt.figure(2) # make a second window

x1 = [x for x in range(1, 101)]
y1 = [y ** 2 for y in x1]
plt.plot(x1, y1)

x2 = [x for x in range(1, 101)]
y2 = [random.randrange(1000) for y in range(100)]
plt.plot(x2, y2, color='purple', marker='o', markersize=5, linestyle='--', alpha=1)

plt.xlabel('time (seconds)', color='black')
plt.ylabel('intensity (dB)')
plt.title('Example Plot')
plt.axis([0, 50, 0, 1000]) # xmin, xmax, ymin, ymax

plt.show()