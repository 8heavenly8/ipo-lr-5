#Анастасия
with open('text.txt', 'r' ) as text:
    content = text.read( )
    print(f"в файле содержится строка: {content}")
    print(f"колличество слов в файле: {len(content.split( ))}")