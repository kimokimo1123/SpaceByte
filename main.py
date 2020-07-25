from Planet import Planet

my_earth = Planet(149597890, 149577002.3, 2499813.6534358, 0.01671022, 0)
#        radius_fi = my_earth.radius_fi()
for angle in range(0, 360, 1):
    my_earth.winkel_fi = angle
    print(angle, my_earth.radius_fi())