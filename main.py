from colorama import Fore, Back, Style

sl = []

with open('add_word.txt', 'r+') as f:
  f.write('\n')
  while True:
    print(Fore.YELLOW)
    a = input('Enter new word: ')
    if a not in sl:
      sl.append(a)
      if a == 'b':
        sl.pop()
        print(Fore.GREEN)
        print(sl)
      if a == 's':
        sl.pop()
        f.writelines(f'{sl}\n')
      if a == 'q':
        sl.pop()
        break 
    else:
      print(Fore.RED)
      print('Word in base too')