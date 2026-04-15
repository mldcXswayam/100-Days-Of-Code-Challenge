print("Welcome to the Brand name Generator")
city = input("Enter the name of the city you live in:\n")
number_of_members = input("Enter number of members in your team:\n")
abundancy = input("Enter the area of expertise of your team(strikers, defenders, mid-fielders, passing, blocking):\n")
suggestion = city+abundancy+" "+number_of_members
print(f"Here's a name suggestion for your team: {suggestion}")