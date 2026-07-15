class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15 Celsius")
        self._celsius = value
        
    @property
    def fahrenheit(self):                       # read-only, computed on the fly
        return (self._celsius * 9/5) + 32
        
temp1 = Temperature(25)

print(temp1.celsius) 
print(temp1.fahrenheit)

temp1.celsius = 280
print(temp1.celsius)
print(temp1.fahrenheit)