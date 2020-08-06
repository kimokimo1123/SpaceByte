import math

class Planet:

    def __init__(self, name, grosse_ha, kleine_ha, lineare_ex, numerische_ex, winkel_fi, daily_rotation):
        self.name = name
        self.grosse_ha= grosse_ha
        self.kleine_ha= kleine_ha
        self.lineare_ex= lineare_ex
        self.numerische_ex= numerische_ex
        self.winkel_fi= winkel_fi
        self.daily_rotation = daily_rotation

    def radius_fi(self):
        return self.kleine_ha/math.sqrt(1-(self.numerische_ex**2)*(math.cos(self.winkel_fi)**2))

    def get_x(self):
        return self.grosse_ha*math.cos(math.radians(self.winkel_fi))
    
    def get_y(self):
        return self.kleine_ha*math.sin(math.radians(self.winkel_fi))

    def rotate(self, days):
        self.winkel_fi += self.daily_rotation*days