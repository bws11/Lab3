# Program that asks the user for their name, age and favourite programming language
name: str = input("Enter your name: ")
age: int = int(input("Enter your age: "))
language: str = input("Enter your favourite programming language: ")

# New line character so it looks a bit better in the console
print(f"\nHello, {name}!")

if age > 18:
    print(f"You are still learning and developing your skills.")
else:
    print("Keep developing your programming skills!")

if language.lower() == "python":
    print("Python is a great language to learn!")
else:
    print(f"Keep on learning {language}!")