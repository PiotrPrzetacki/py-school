oceny = open('oceny.txt', 'r')
oceny.readline()
oceny_uczniow = {}
for ocena in oceny:
    o = ocena.split(';')
    id = o[0]
    ocena = int(o[1])
    if id in oceny_uczniow.keys():
        oceny_uczniow[id].append(ocena)
    else:
        oceny_uczniow[id] = [ocena]

max_avg = {'id': '0', 'avg': 0}
for id in oceny_uczniow.keys():
    oceny_ucznia = oceny_uczniow[id]
    avg = sum(oceny_ucznia) / len(oceny_ucznia)
    if avg>max_avg['avg']:
        max_avg['avg'] = avg
        max_avg['id'] = id

def getUczen():
    uczniowie = open('uczniowie.txt', 'r')
    uczniowie.readline()
    for uczen in uczniowie:
        u = uczen.split(';')
        if u[0] == max_avg['id']:
            return (u[2], u[1])
        
print(getUczen(), max_avg['avg'])