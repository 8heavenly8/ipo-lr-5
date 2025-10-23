with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:# открываем первый файл и создаем второй файл 
    reversed_line = input_file.read()[::-1] # читаем файл и с помощью срезов переворачиваем текст, записываем в переменную
    output_file.write(reversed_line)#записываем то что получилось в новый текстовый файл