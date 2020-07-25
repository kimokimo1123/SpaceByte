import unittest
from Planet import Planet

class TestPlanet(unittest.TestCase):

    def test_Earth_radius_fi(self):
        my_earth = Planet(149597890, 149577002.3, 2499813.6534358, 0.01671022, 0)
        radius_fi = my_earth.radius_fi()
        self.assertEqual(round(radius_fi), 149597890)

    def test_Jupiter_radius_fi(self):
        my_jupiter = Planet(778412020, 777500023.9, 37669428.22, 0.04839266, 0)
        radius_fi = my_jupiter.radius_fi()
        self.assertEqual(round(radius_fi), 778412020)

if __name__ == '__main__':
    unittest.main()