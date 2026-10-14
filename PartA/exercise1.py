weather: str = input("How's the weather? ")
weather = weather.lower() # Lower case so it's easier for the if statements later

if weather == "sunny":
    print("Great! Go for a walk.")
elif weather == "rainy":
    print("Take an umbrella.")
elif weather == "snowy":
    print("Stay warm and be careful!")
else:
    print("I don't recognise that weather.")
