input('verzoek')

print ('Croissantje')
croissantje = input ('Hoeveel kost een croissantje (in centen)? ')
cr = input ('Hoeveel croissantjes wil je? ')

croissantje = int(croissantje)
cr = int(cr)

print ('de croissantjes kosten ' + str(croissantje * cr))

print ('')


print ('Stokbrood')
stokbroden = input ('Hoeveel kost een stokbrood (in centen) ')
st = input ('Hoeveel stokbroden wil je? ')

stokbroden = int(stokbroden)
st = int(st)

print ('de stokbroden kosten ' + str(stokbroden * st))

print ('') 


print ('Kortingsbon')
kortingsbonnen = input ('Hoeveel korting krijg je per bon (in centen)? ')
ko = input ('Hoeveel kortingsbonnen heb je?')

kortingsbonnen = int(kortingsbonnen)
ko = int(ko)

print ('Je hebt ' + str(kortingsbonnen * ko) + ' cent korting')


print ('')

print  ('In totaal kost het ' + str(cr * croissantje + (st * stokbroden) - (ko * kortingsbonnen)) + ' cent')