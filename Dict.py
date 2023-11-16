lista_goala = []
dict_gol = {}


# declaram si initializam un map
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

#Adaugam elemente
note_elevi['Sebi'] = 7
print(note_elevi)

#aflama elemente din lista

print(note_elevi['Gigel'])

#actualizam valori

note_elevi['Costel'] = 10
print(note_elevi['Gigel'])

#aflam dimensiunea
print(len(note_elevi))

#stergem valori
note_elevi.pop('Gigel')
print(note_elevi)

#returneaza doar cheile
print(note_elevi.keys())