import random
def game(comp,you):
    if comp==you:
        return None
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("comp turn:snake(s) or water(w) or gun(g)")
randno = random.randint(1,3)
if randno == 1:
    comp='s'
elif randno ==2:
    comp = 'w'
elif randno==3:
    comp = 'g'
you = input("snake(s) or water(w) or gun(g) :")
a = game(comp,you)
print(f"computer chose {comp} ")
print(f"you chose {you} ")
if a == None:
    print("its a tie!")
elif a:
    print("you win")
else:
    print("you lose")


