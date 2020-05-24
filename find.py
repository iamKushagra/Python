string = "she is awesome and she is great dancer"
print(string.replace("is", "was", 2))

is_pos1 = string.find("is") # is_pos1 --- number
print(string.find("is"))
is_pos2 = string.find("is", is_pos1 + 1)
print(is_pos2)