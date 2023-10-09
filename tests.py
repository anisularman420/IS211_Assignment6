import conversions
import unittest

class TestConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(0), 273.15, places=2)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(-40), 233.15, places=2)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(100), 373.15, places=2)
        # Add more test cases...

    def test_convertCelsiusToFahrenheit(self):
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(0), 32.0, places=2)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(-40), -40.0, places=2)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(100), 212.0, places=2)
        # Add more test cases...

    def test_convertFahrenheitToCelsius(self):
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(32), 0.0, places=2)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(-40), -40.0, places=2)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(212), 100.0, places=2)
        # Add more test cases...

    def test_convertFahrenheitToKelvin(self):
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(32), 273.15, places=2)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(-40), 233.15, places=2)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(212), 373.15, places=2)
        # Add more test cases...

    def test_convertKelvinToCelsius(self):
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(273.15), 0.0, places=2)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(233.15), -40.0, places=2)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(373.15), 100.0, places=2)
        # Add more test cases...

    def test_convertKelvinToFahrenheit(self):
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(273.15), 32.0, places=2)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(233.15), -40.0, places=2)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(373.15), 212.0, places=2)
        # Add more test cases...

if __name__ == '__main__':
    unittest.main()
