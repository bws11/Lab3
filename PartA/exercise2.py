# Ask the user for their age so you can tell watch films they can watch
age = int(input("How old are you? "))

if age < 12:
    print("You can watch a childrens film.")
elif 12 <= age <=14:
    print("You can watch a 12+ film.")
elif 15 <= age <= 17:
    print("You can watch a 15+ film.")
else:
    print("You can watch any age-rated film in this example.")

