mass = []
sad = []
clon = []
with open('Prime.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        mass.append(line)
        line = f.readline()
with open('Second.txt', 'r')as x:
    maid = x.readline()
    while maid:
        maid = maid.strip()
        sad.append(maid)
        maid = x.readline()
for i in mass:
    if i in sad:
        clon.append(i)
print(clon)