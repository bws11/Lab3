# Weather can be sunny or rainy
# Journey is disntance in miles
# budget is in £


weather: str = input("What's the weather like (sunny/rainy)? ").lower()
distance: int = int(input("How far are you planning on going in miles? "))
budget: float = float(input("What is your avaliable budget (£)? "))

if weather not in ["sunny", "rainy"]:
    print("Invalid weather, must be either sunny or rainy")

if distance <= 0:
    print("Invalid distance, you have to travel at least a little bit...")

if budget < 0:
    print("I'm not asking about your debt. I'm asking how much money can you use for this journey")

if distance <= 3 and weather == "sunny":
    print("Take a walk")
elif distance <= 3 and weather == "rainy":
    print("Take a walk but take a coat with you")
elif 3 > distance > 10 and weather == "sunny":
    print("Go and cycle there.")
elif 3 > distance > 10 and weather == "rainy" and budget >= 3:
    print("Take the bus.")
else:
    print("Drive there")