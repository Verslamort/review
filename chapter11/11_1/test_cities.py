import unittest
from city_functions import get_city_country


class CitiesTestCase(unittest.TestCase):
    """测试get_city_country"""

    def test_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country = get_city_country('santiago', 'chile',
                                        'population 5000000')
        self.assertEqual(city_country, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
