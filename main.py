from Planet import Planet
import math
import numpy

my_earth = Planet('Earth', 149597890, 149577002.3, 2499813.6534358, 0.01671022, 0)

for angle in numpy.arange(0, 2*math.pi+math.pi/180, math.pi/180):
    my_earth.winkel_fi = angle
    print(angle, round(my_earth.x_coordin()), round(my_earth.y_coordin()))

    