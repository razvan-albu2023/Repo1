piesa_faina = True

if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# daca numarul este par, printam acest lucru
# altfel printam impar

nr = 2
# ce inseamna par = se imparte exact la 2
# inseamna ca restul impartirii este 0
# adica modulo

if nr % 2 == 0:
    print('numarul este par')
else:
    print('impar')
if (nr >0):
    print('pozitiv')
else:
    print('numarul nu este pozitiv')

# if, else if, else
# cum ne saluta robotelul in functie de ora
# luam date de la tastatura
# ne asiguram ca este transformat din string in int
# ora = int(input('introdu ora   '))
# if ora < 0:
#     print('ora negativa')
# elif ora <= 11:
#     print('Buna dimineata')
# elif ora <=18:
#     print('Buna ziua')
# elif ora <=21:
#     print('Buna seara')
# elif ora <= 24:
#     print('Noapte buna')
# else:
#     print('ora invalida. ora mai mare decat 24')

#CTRL + / - comenteaza sau decomenteaza
# robotel Digi telefonic
optiune = int(input('alege o optiune    ro -> 1; eng -> 2' ))
if optiune == 0:
    print('meniu anterior')
elif optiune == 1:
    print('ati ales ro')
elif optiune == 2:
    print ('ati ales eng')
else:
    print ('nu am identificat optiunea')