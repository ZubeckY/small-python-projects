fruits = ["яблоко", "вишн€", "банан", "киви", "лимон", "груша", "авокадо"]

ask_fruit = input('введите номер фрукта 0-6')

n = int(ask_fruit)

if n == 0:

    print (fruits[0])

elif n == 1:

    print (fruits[1])

elif n == 2:

    print (fruits[2])

elif n == 3:

    print (fruits[3])

elif n == 4:

    print (fruits[4])

elif n == 5:

    print (fruits[5])

elif n == 6:

    print (fruits[6])

else:

   print ('error')