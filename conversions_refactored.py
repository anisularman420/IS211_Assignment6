class ConversionNotPossible(Exception):
    """Custom exception to handle cases where conversion is not possible."""
    pass

def convert(fromUnit, toUnit, value):
    """Convert a value from one unit to another."""

    conversion_factors = {
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda x: (x + 459.67) * 5/9,
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x * 9/5) - 459.67
    }

    if (fromUnit, toUnit) in conversion_factors:
        conversion_function = conversion_factors[(fromUnit, toUnit)]
        result = conversion_function(value)
        return result
    else:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible.")
