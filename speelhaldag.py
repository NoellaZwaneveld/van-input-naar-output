input('verzoek')

print('Toegang')
toegang = input('Hoeveel kost toegang(in centen)? ')
personen = input('Voor hoeveel personen? ')

toegang = int(toegang)
personen = int(personen)

print('Toegang kost ' + str(toegang * personen ) + ' voor ' + str(personen) + ' personen')

print('')

print('VIP')
vip = input('Hoeveel kost VIP per minuut(in centen)? ')
minuten = input('Hoeveel minuten wil je VIP? ')

vip = int(vip)
minuten = int(minuten)

print ('VIP kost ' +  str(vip * minuten) + ' per persoon')

print('')

print('In totaal kost het ' + str(toegang * personen + (personen * (minuten * vip))) + ' voor ' + str(personen) + ' personen')