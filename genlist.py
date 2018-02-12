'''l = []
nl = []
for i in range(20):
    values = [0 + i, 1 + i, 2 + i]
    for i in range(20):
        if i in values:
            l.append('X')
        elif not i in values:
            l.append('P')
    nl.append(l)
    l = []

for l in nl:
    print(str(l) + ',')'''

l = []
for i in range(20):
    l.append(62 + i * 25)

print(l)
    
    
