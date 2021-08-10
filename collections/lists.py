# Lists (Arrays)

sre = ["Kieron", "Victor", "Amy", "Will", "Zeeshan"] # lists are ordered and keep the order
print(sre[0])
sre[-1] = "Michael"
print(sre)

sre.append("Ioana")
print(sre) # string methods had an output the majority work this way - append changes 

sre.remove("Amy")
print(sre)

print(sre.pop()) # Removes the last element of the list - can print 
print(sre)

print(sre.pop(0)) # can pass an index and can remove that item in list

sre.sort(reverse=True) # does not return anything but sorts
