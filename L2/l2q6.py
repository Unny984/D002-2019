import random
print('''Welcome to the Banana Guessing Game. Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
n = random.randint(1,100)
print("shhh, Dave hides %s bananas" % n)
found = False
count = 0
while count < 3:
    p = int(input("Try to find out how many bananas Dave hid \n"))
    if p > n:
        count = count + 1
        print("Too Big")
        
    elif p < n:
        count = count + 1
        print("Too Small")
    else:
        found = True
        break
if found == True:
    print('You got the correct guess in %d trials' % count)
    print('Dave\'s banana are now all yours!')
else:
    print("You failed to find the number of bananas Dave hid! Try again next")
