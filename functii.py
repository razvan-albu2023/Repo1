def printGreeting():
    print('Buna ziua! Bine ati venit!')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')
def piValue():
    return 3.14

def mediaNr (a, b, c):
    return (a+b+c)/3

# exercitiu
#daca nr e pozitic, returnati True, altfel False
#daca persoana e majora, altfel false
def verificareMajor (varsta):
    if varsta >=18:
        return True
    else:
        return False


# zona de apelare
printGreeting()
printGreeting()

printGreetingByName('Albu', 'Razvan')
print(mediaNr(3,5,4))
print(piValue())

#se ia varsta utilizatorului
age = int(input('Introduceti varsta dvs.'))
if verificareMajor(age):
    print ('Cont creat! Bine ai venit in aplicatie')
else:
    print('Nu ai varsta minima necesara pentru a paria')

#oop
#variabile => atribute, proprietati sau field-uri
#functii => metode

