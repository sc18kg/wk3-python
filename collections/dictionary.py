# Collection of Key-Value Pairs

dict = {"a":1, 
        "b":2, 
        "name" : "Kieron",
        "age" : 24,
        "food" : "nandos"}

print(dict["age"]) #Square brackets to key
print(dict.get("name")) # if you call get and it doesnt have the key - returns None

dict["a"] = 100 # Square brackets to reassign
dict.update({"a": 500, "film" : "Inception"}) # .Update to change values or create new 

print(dict)

sre = {
    "course name" : "Deloitte SRE",
    "length" : 12,
    "trainees" : ["Ioana", "Kieron", "Will"],
    "outline" : {
        "Week 1" : "Business Week",
        "Week 2" : "Linux",
        "Week 3" : "Python"
    }

}

print(sre)
print(sre.keys()) # returns keys in the dictionary
print(sre.values()) # returns the values in the dictionary
print(sre.items()) # returns the keys and values together as tuple seperated by comma


print("Linux" in sre or sre.values())