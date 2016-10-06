import ast


a = open('List','r')
atext = a.read()
b = open('UndergradList','w')
c = []
d = []
f = []
c = atext.split('\n')
for i in c:
    try:
        f.append(ast.literal_eval(i))
    except:
        print('Oooops')

key = 'Classification:'
value = 'Undergraduate Student'

g = []
for line in f:
    try:
        if key in line:
            if value in line[key]:
                g.append(line)
        
    except:
        print(line)

for rows in range(len(g)):
    b.write(str(g[rows]) + '\n')

print('Write Complete')
