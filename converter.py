print('                  ----------Converter----------')

print('''\nConvert minute into second,  kilometre into metre, feet into inches,etc   ''')
print('\nFOR-')
operators = ['\nMinute into Second = 1 ','second into minute = 2','kilometre into metre = 3','Metre into kilometre = 4','feet into inches = 5','inches into feet = 6']


for t in operators :
    print(t)

print('\nPress particular number for particular function')
a = input('\nEnter the function number: ')
a = float(a)

if a == 1:
    b = input('enter the minute: ')
    b = float(b)

    b = b * 60
    print('Here your minutes are converted into second: ' + str(b) + str('second'))
if a == 2:
    b = input('enter the seconds: ')
    b = float(b)

    b = b / 60
    print('Here your seconds are converted into minute: ' + str(b)+str(' min'))

elif a == 3:
    c = input('Enter the kilometre: ')
    c = float(c)

    k = c*1000
    print('Here your kilometre are converted into metre: ' + str(k)+str(' metre'))

elif a == 4:
    c = input('Enter the metre: ')
    c = float(c)

    k = c / 1000
    print('Here your metre are converted into kilometre: ' + str(k) + str(' kilometre'))
elif a == 5:
    d = input('enter the feets: ')
    d = float(d)

    h = d*12
    print('Here your feets are converted into inches: ' + str(h) + str('inches'))

elif a == 6:
    d = input('enter the inches: ')
    d = float(d)

    h = d / 12
    print('Here your inches are converted into feets: ' + str(h) + str('feets'))

