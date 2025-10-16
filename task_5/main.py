consonants = "йцкнгшщзхъфвпрлджчсмтьб"
string = (input("введите строку: "))
index = 0
for num in string.lower():
    if num in consonants:
        print(f"индекс согласной буквы: {index} ({num})")
    index += 1
