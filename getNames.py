lines = []

with open('names.txt' , 'r') as f:
    for line in f:
        lines.append(line)


for i in range(len(lines)):
    if "Name" in lines[i]:
        k = i + 1
        while "Name" not in lines[k]:
            print(lines[k])
            k += 1        
