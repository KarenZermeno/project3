import numpy as np # import the library numpy to make calculations
import matplotlib.pyplot as plt # import the library matplotlyb.pyplot to generate a grafic
from random import randint # import the library random to generate aleatory numbers

levels = 12 # set the level number
lanes = [0]*(levels) # set the riles beggining in 0 to each one

for h in range(3000): # make a loop simulating 3000 positions, generate a random number
  stored = -1 # stores a  the final position of the ball a given lane
  for j in range(levels):
    stored += randint(0, 1) 
  lanes[stored] += 1 # increments the counter for the lane list
print((3000), "balls were used in totall") # print the total number of used balls
print(lanes) # print the balls in each lane

X = np.arange(-((len(lanes)/2)-.5), (len(lanes)/2)+.5) # use it to centrate the number of levels, returns the length of the lanes list, represents the number of lanes in Galton's machine
plt.suptitle('Galton Board') # set a title to the grafic
plt.bar(X + 0.00, lanes, width=0.25) # represents the positions on the x-axis where the bars will be placed. Specifies the width of the bars on the chart.
plt.show() # show the grafic
