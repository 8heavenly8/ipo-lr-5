string = input("введите строку:")
list_str = string.split( )
num = 0
new_string = ""
while len(list_str) > num:
    new_string += list_str[num][0]
    num += 1
print(f"строка из первых букв: {new_string}")
    