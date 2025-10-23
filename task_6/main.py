with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    reversed_line = input_file.read()[::-1] 
    output_file.write(reversed_line)