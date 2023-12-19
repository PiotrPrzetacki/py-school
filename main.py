oceny = open('oceny.txt', 'r')
oceny.readline()
oceny_uczniow = {}
for ocena in oceny:
    o = ocena.split(';')
    id = o[0]
    ocena = o[1]
    if id in oceny_uczniow.keys():
        oceny_uczniow[id].append(ocena)
    else:
        oceny_uczniow[id] = [ocena]

print(oceny_uczniow)