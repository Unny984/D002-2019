vowelist = []


for i in range(10):
    word = input("Please enter a word.\n")
    print(word[0])
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        print(word)
        vowelist.append(word)
print(vowelist)
