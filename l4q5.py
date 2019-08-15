def printer(secret, opened):
  i = 0
  while i < len(secret):
    if i in opened:
      x = secret[i]
    else:
      x = "_"
    i = i+1
    print(x, end="")

printer("apple",[1, 2])
printer("orange", [0, 5])
printer("cat",[])
