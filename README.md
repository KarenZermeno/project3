# project3
Galton's Machine

Must to import librarys like NUMPY, MATPLOTLIB.PYPLOT and RANDINT. This are used to generate aleatory numbers, make calculations ang grafics

Now define level numbers and make a list called lanes to stablish the number 12 levels in the Galton's Machine and made a list called lanes to represent the rails in the machine. All the rails start in 0 balls.

Run the loop to simulate operation of the Galton's Machine with 3000 balls droping a ball in the Machine. For each iteration, a random number (0 or 1) is generated at each level of the machine and the position of the ball is adjusted based on that number.
The stored variable stores the final position of the ball in a given lane. Then, the counter for that lane in the lanes list is incremented.

Next, we print the total number of ball used and the count of balls in each lane. Then, a bar char is created using the matplotlib.plyplot library. The lane is used to represent the data on the graph. The lanes are shown on the x-axis, while the number of balls in each lane is shown on the y-axis. Shown the grafic using plt.show().

