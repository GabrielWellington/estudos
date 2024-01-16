"""cid = str(input('Em qual cidade voce nasceu?: ')).strip().upper()
print(cid[:5]== 'SANTO')"""""

city = str(input('Em qual cidade voce nasceu?: ')).strip().upper().split()
c = city[0]
p = 'SANTO' in c
print(p)


