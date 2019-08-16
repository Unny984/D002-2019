collection = ["Pikachu", "Bulbasaur", "Squirtle", "Nidoqueen"]
newly_caught = ["Bulbasaur", "Kakuna", "Arbok", "Jigglypuff"]

for i in newly_caught:
    if i not in collection:
        collection.append(i)
print(collection)

hsi = [20000, 21000, 21500, 22125, 21015, 22013, 19942, 24500]
change = []

for i in range(7):
    change.append(hsi[i + 1] - hsi[i])
print(change)

channels = ["TVB", "CCTV", "VIU", "RTHK", "Netflix", "TBS", "KBS"]

current_channel = 0
while True:
    print("You are now watching %s" % channels[current_channel])
    a = input("Please choose either Up/Down/Off\n")
    if a == 'U':
        current_channel = (current_channel + 1) % 7
        print()
    if a == 'D':
        current_channel = (current_channel - 1) % 7
        print()
    if a == 'O':
        print("OFF")
        break
