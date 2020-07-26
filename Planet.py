import math

class Planet:

    def __init__(self, name, grosse_ha, kleine_ha, lineare_ex, numerische_ex, winkel_fi):
        self.name = name
        self.grosse_ha= grosse_ha
        self.kleine_ha= kleine_ha
        self.lineare_ex= lineare_ex
        self.numerische_ex= numerische_ex
        self.winkel_fi= winkel_fi

    def radius_fi(self):
        radius_n = self.kleine_ha/math.sqrt(1-(self.numerische_ex**2)*(math.cos(self.winkel_fi)**2))
        return radius_n

    def x_coordin(self):
        x_coord = self.grosse_ha*(math.cos(self.winkel_fi))
        return x_coord
    
    def y_coordin(self):
        y_coord = self.kleine_ha*(math.sin(self.winkel_fi))
        return y_coord