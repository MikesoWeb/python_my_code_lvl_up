from colorama import Fore, Back, Style
from time import sleep

sl = []
sleep(1)
print(Fore.LIGHTMAGENTA_EX)
print('Добро пожаловать в мой проект')
print('Чтобы узнать подробнее, нажмите h')

with open('add_word.txt', 'a') as f:
  while True:
    print(Fore.YELLOW)
    a = input('Enter new word: ')
    if a not in sl:
      sl.append(a)
      if a == 'b':
        sl.pop()
        print(Fore.GREEN)
        print(sl)
      if a == 'k':
        sl.pop()
        print(Fore.LIGHTMAGENTA_EX)
        print('1) Чтобы посмотреть что вы вели, нажмите b')
        sleep(1)
        print('2) Чтобы сохранить данные, нажмите s')
        sleep(1)
        print('3) Чтобы выйти из программы, нажмите q')
      if a == 's':
        sl.pop()
        f.writelines(f'{sl}\n')
      if a == 'q':
        sl.pop()
        break 
     
    else:
      print(Fore.RED)
      print('Word in base too')