class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a = []
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        a.append(Kelvin)
        a.append(Fahrenheit)
        return a