lines = []

with open('names.txt' , 'r') as f:
    for line in f:
        lines.append(line[:-1])


for line in lines:
    if line.isupper():
        fileName = line + '.csv'
    
    with open(fileName, 'a') as f:
        if line == '':
            f.write("\n,")
        elif line[0].isdigit():
            f.write(f"{line[:5]}, {line[5:]},")
            f.write('\n')
        else:
            f.write(line + ", ")
            f.write('\n')