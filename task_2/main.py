#Анастасия
string1 = input("введите первую строку:")
string2 = input("введите вторую строку:")
if sorted(string1) == sorted(string2):
    print(f"строки '{string1}' и '{string2}' являются анаграммами")
else:
    print(f"строки '{string1}' и '{string2}'не являются анограммами")