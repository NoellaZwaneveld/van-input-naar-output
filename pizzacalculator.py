#Noëlla Zwaneveld
#opdracht: Pizza calculator

small = 8.99 #prijs van small pizza
medium = 10.49 #prijs van medium pizza
large = 13.99 #prijs van large pizza

input ('')

print('Small')
smallpizza = input ('Hoeveel small pizza(s) wilt u? ')

print('')

print('Medium')
mediumpizza = input ('Hoeveel medium pizza(s) wilt u? ')

print('')

print('Large')
largepizza = input ('Hoeveel large pizza(s) wilt u? ')

print('')

smallpizza = int (smallpizza)
mediumpizza = int (mediumpizza)
largepizza = int (largepizza)

print('Uw bestelling ')
print('')
print('Aantal small pizza(s): ' + str(smallpizza))
print('Aantal medium pizza(s): ' + str(mediumpizza))
print('Aantal large pizza(s): ' + str(largepizza))
print('')

totaal = str(small * smallpizza + (medium * mediumpizza) + (large * largepizza))

print('Uw bestelling kost in totaal: €' + totaal) 