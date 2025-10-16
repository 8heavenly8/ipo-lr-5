#Анастасия
string = input("введите строку: ")
vowels = "аеёиоуыэюяУЕЁЭИОАЫЯЮ"
consonant = "йЙцЦкКнНгГшШщЩзЗхХъЪфФвВпПрРлЛдДжЖчЧСсмМтТьЬбБ"
amount_vowels = 0
amount_consonant = 0
for char in string:
    if char in vowels:
        amount_vowels += 1
    if char in consonant:
        amount_consonant += 1
print(f"количество символов = {len(string)}")
print(f"количество гласных = {amount_vowels}")
print(f"количество согласных = {amount_consonant}")