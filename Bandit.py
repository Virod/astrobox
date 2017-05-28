import random
import time
 
while True:
    try:
        credit = int(input('Введи нужное тебе колличество кредитов: '))
        print ('И так! Игра началась. У тебя есть ' + str(credit) +
           ' единиц, с помощью них ты можешь делать ставки')
        cash = int(input('Введи ставку: '))
    except:
        print ('ВЕДИ ЦИФРЫ')
    try:
        while credit > 0:
                print('Отлично, ставка сделана!')
                time.sleep(0.1)
                print('Генерирую...')
                time.sleep(0.1)
   
                m = random.randint(1, 3)
                o = random.randint(1, 3)
                n = random.randint(1, 3)
                e = random.randint(1, 3)
       
                print(m, o, n, e)
                credit = credit - cash
                if m == 1 and o == 1 and n == 1 and e == 1 or m == 2 and o == 2 and n == 2 and e == 2 or m == 3 and o == 3 and n == 3 and e == 3 :
               
                    b = random.randint(2, 2000)
                    print('О БОЖЕ!!!!!!!!!!! ВЫ ВЫИГРАЛИ ' + str(cash * b))
                    credit = credit + (cash * b)
                    time.sleep(2)
                    y = input('Введи "y" если хочешь сменить ставку: ')
                    time.sleep(2)
                    if y == 'y':
                        cash = int(input('Введи ставку: '))
                    else:
                        continue
                    time.sleep(2)
                print('Oсталось кредитов ' + str(credit))
                input('Press enter...!')
    except:
        print('ERROR ENTER')