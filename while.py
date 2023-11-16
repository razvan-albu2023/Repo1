# masina merge cat timp inca are benzina
litri_benzina = 10
while litri_benzina > 0:
    #acceleram
    print('Vrrum Vrrum!')
    #scadem benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <=3:
        print('beculetul rosu ! Mai ai doar ', litri_benzina, 'litri benzina')
print('Stop! Nu mai avem benzina')
