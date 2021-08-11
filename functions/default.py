def repeat_greeting(message="Boo", numb_times=3, upper=False): #If you specify - If no arg it will default to this amount
    if upper:
        print(message.upper() * numb_times)
    else:    
        print(message * numb_times)

repeat_greeting("Hello", 10)
repeat_greeting("Loser")
repeat_greeting(upper=True)