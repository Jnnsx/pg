#funkce ukazujici while
def start_while():
    print('zacatek')
    i=0

    while i<5:
     print('*')
     i += 1

    print('konec')    
#
def start_for():
    print('zacatek')

    for i in [0,  1, 2, 3, 4]:
        print('*',i)

    print('konec')    
#funkce urcujici jestli je number mezi dvema cislami     
def in_range(min_number, max_number, number):
   if number > min_number and number<max_number:
    print('is in range')
   else:
    print('is not in range')

in_range(100, 1000, 200)

#fonkce vypíše ahoj jmeno
def dopln_jmeno(jmeno):
   print('Ahoj', jmeno)

jm = input("zadej jméno:")
dopln_jmeno(jm)
