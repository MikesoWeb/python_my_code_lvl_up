from colorama import Fore
from time import sleep

db = []
sleep(1)
print(Fore.LIGHTMAGENTA_EX)
print('Добро пожаловать в мой проект')
print('Чтобы узнать подробнее, нажмите help')

with open('add_word.txt', 'a') as f:
    while True:
        print(Fore.YELLOW)
        word = input('Enter a new word: ')
        if word not in db:
            db.append(word)
            if word == 'show':
                db.pop()
                print(Fore.GREEN)
                print(db)
            if word == 'help':
                db.pop()
                print(Fore.LIGHTMAGENTA_EX)
                print('1) Чтобы посмотреть что вы вели, нажмите show')
                sleep(0.6)
                print('2) Чтобы сохранить данные, нажмите save')
                sleep(0.6)
                print('3) Чтобы выйти из программы, нажмите quit')
            if word == 'save':
                db.pop()
                with open('db.txt',  'a', encoding='utf-8') as file:
                    file.writelines(f'{db}\n')
                print(f'Сохранено в текстовом файле {file.name}')
            if word == 'quit':
                db.pop()
                break

        else:
            print(Fore.RED)
            print('Word in base too')
