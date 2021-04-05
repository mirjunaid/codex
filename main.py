import random


def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


print('Comp Turn: Rock(r) Paper(p) or Scissor(s)?')
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input('Your Turn: Rock(r) Paper(p) or Scissor(s)?')
a = gamewin(comp, you)

print(f'Computer chose {comp}')
print(f'You chose {you}')

if a == None:
    print('The game is tie')
elif a:
    print('You win')
else:
    print('You lose')
