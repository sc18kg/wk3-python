#IF
prompt_user = True

while prompt_user:
    age = input("What is your age?:\n")
    if age.isdigit():
        age = int(age)
        prompt_user = False
    else:
        print("Please Input a number for age!")
prompt_user = True

while prompt_user:
    cert = input("What is the film rating youd like to watch? U, PG, 12A, 15, 18?:\n")
    if cert == ["U", "u", "PG", "pg", "12A", "12a", "15", "18"]:
        prompt_user = False
        if cert == "U": #Something that will be resolved true or false followed by :
            print("Everyone can watch this regardless of age!")
        elif cert == "PG" and age > 15:
            print(f"You are {age} so are able to watch these films rated {cert}")
        elif cert in ("12A", "12") and age > 12:
            print(f"You can watch {cert} films!")
        elif cert == "15" and age >= 15:
            print(f"Wooo, being {age} You can watch age certificate: {cert} films you wanted")
        elif cert == "18" and age >= 18:
            print(f"Being {age}, You can go enjoy {cert} films")
        else: 
            print(f"As you are {age} You are unable to watch you're requested age certificate of {cert}")
    else:
        print("Please enter a valid certificate of  U, PG, 12A, 15, 18")

