name, char = input("Enter the name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")

#case insensitive
#counting charcters

print(f"character count : {name.strip().lower().count(char.strip().lower())}")
#char.strip().lower()