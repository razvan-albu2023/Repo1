# #dalmatienii
#
# for i in range (1,102):
#     print(f'Dalmatianul nu nr. {i}')

# for i in range(1, 102, 2):
#     print(f'Dalmatianul nu nr. {i}')


# numere = [3, 7, 10, 20, 30]
# # parcurgere lista cu for prin intermediul indexului
# for i in range(0, len(numere)):
#     print(f'indexul curent este {i}')
#     print(f'Numarul curent este {numere[i]}')

# # for each
# s=0
# for numar in numere:
#     print(f'Numarul curent este {numar}')
#     s= s+numar
# print(f'Suma este {s}')

#de cate ori apare 3 in [3, 2, 3, 5, 3]

i=0 #initializam numarul de incidentze 'i'
numere = [3, 2, 3, 5, 3, 11 ,3, 31, 3]

for numar in numere:
    if numar == 3:
        i=i+1
print(f'3 apare in sir de {i} ori')
