def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15
    return kelvins

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    kelvins = (fahrenheit + 459.67) * 5/9
    return kelvins

def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    celsius = kelvin - 273.15
    return celsius

def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (kelvin * 9/5) - 459.67
    return fahrenheit
