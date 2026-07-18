class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a = celsius + 273.15
        b = celsius * 1.80 + 32.00
        return [a,b]