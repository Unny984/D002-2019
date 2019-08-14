import random
print('''Welcome to the Banana Guessing Game. Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
n = random.randint(1,100)
print("shhh, Dave hides %s bananas" % n)
found = False
count = 0
p = int(input("You have 3 chances to find out many bananas Dave hid. \n"))
if p != n:
    found = False
    p = int(input("You still have 2 chances to find out. \n"))
    if p != n:
        found = False
        p = int(input("You still have 1 chance to find out \n"))
        if p != n:
            found = False
    else:
        found = True
else:
    found = True

if found == True:
    print('You got the correct guess in %d trials' % count)
    print('Dave\'s banana are now all yours!')
else:
    print("You failed to find the number of bananas Dave hid! Try again next")
