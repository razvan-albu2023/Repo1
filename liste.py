# Listele in Python pot cuprinde elemente de tipuri diferite
# au dimensiune dinamica
fructe = ['mar', 'banana', 'portocala', 3, True]
print(fructe)

# accesam un element in functie de index
print(fructe[0])

# adaugam un nou element
fructe.append('rosie')
# uprascriem un element

fructe[0] = 'para'
print(fructe)
# aflam dimensiunea

print(len(fructe))
# scoatet si ne returneaza ultimul element
last = fructe.pop()
print('ultimul element pe care l-am si sters a fost - ',last)
print(fructe)

fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)

