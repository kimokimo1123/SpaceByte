import unittest
from Planet import Planet

class TestPlanet(unittest.TestCase):

    def test_Earth_radius_fi(self):
        my_earth = Planet('Earth',149597890, 149577002.3, 2499813.6534358, 0.01671022, 0, 1)
        radius_fi = my_earth.radius_fi()
        self.assertEqual(round(radius_fi), 149597890)

    def test_Jupiter_radius_fi(self):
        my_jupiter = Planet('Jupiter',778412020, 777500023.9, 37669428.22, 0.04839266, 0, 2)
        radius_fi = my_jupiter.radius_fi()
        self.assertEqual(round(radius_fi), 778412020)
    
    def test_rotate_1_day(self):
        planet = Planet('Jupiter',778412020, 777500023.9, 37669428.22, 0.04839266, 0, 2)
        self.assertEqual(planet.winkel_fi, 0)
        planet.rotate_1_day()
        self.assertEqual(planet.winkel_fi, 2)

if __name__ == '__main__':
    unittest.main()