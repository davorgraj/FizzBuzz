# -*- coding: utf-8 -*-

stevilo = int(raw_input("Vnesite število med 1 in 100: "))
max = 100

for x in range(1, stevilo + 1)[:max]:
    if (x % 3) == 0 and (x % 5) == 0:
        print "fizzbuzz"
    elif (x % 3) == 0:
        print "fizz"
    elif (x % 5) == 0:
        print "buzz"
    else:
        print x