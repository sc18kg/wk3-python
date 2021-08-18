import json

first_pet = {
    "name" : "Shep",
    "animal" : "Dog",
    "colour" : " Black and White"
}

first_pt_string = json.dumps(first_pet)    # dump s sumps as string
print(first_pet, type(first_pet))

with open('first_pet_file.json', 'w') as jsonfile: #this becomes the output path
    json.dump(first_pet, jsonfile)

with open("new_animal.json", "r") as jsonfile:
    cute = json.load(jsonfile)

print(cute["breed"])