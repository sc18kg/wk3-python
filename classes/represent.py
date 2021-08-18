class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return f"{self.latitude} , {self.longitude}"

bham_academy = Location(52.488647, -1.887249)
print(bham_academy.__repr__()) # Formats to this if no __str__ - should be like source code
print(bham_academy.__str__())  #Looks for this first - human readable 

print(repr(bham_academy))
print(str(bham_academy))

n = 0.003453
print(f"Fixed Point: {n:f}")
print(f"Exponential Notation: {n:e}")