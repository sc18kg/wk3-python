#set

car_parts = {"wheels", "doors", "engine"} # uses curly braces just like dictionaries
print(car_parts)

# Sets are unordered so cannot refer to positions (cannot be indexed)
# Mutable unordered collections

car_parts.add("accelerator")
print(car_parts)

car_parts.discard("doors")

#Alot of the functions are mathmatical
#Frozen sets are unordered and immutable
fs = frozenset(['Shrek', 'Shrek 2', 'Shrek 3'])
print(fs)

#Sets can only represent each thing once

print("Shrek" in fs) # returns true if item is in the list