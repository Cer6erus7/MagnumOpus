import unittest
import func


class CityCountryClass(unittest.TestCase):
    """
    Tests for city_country
    """
    def test_city_country(self):
        city_and_country = func.city_country("kiev", 'ukraine')
        self.assertEqual(city_and_country, "Kiev, Ukraine")

    def test_city_country_population(self):
        city_and_country = func.city_country("kiev", 'ukraine', population=2000000)
        self.assertEqual(city_and_country, "Kiev, Ukraine. Population - 2000000")


if __name__ == "__main__":
    unittest.main()