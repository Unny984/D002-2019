from math import *

people = int(input("How many people are sharing the bill?\n"))
bill = float(input("How much is the bill?\n"))
print("Kevin paid the bill first. But Kevin only has 100 dollar notes")
print("So Kevin is going to paid $ %d." % bill)
print("The cafe s giving %f to Kevin." % abs(bill - 100))
print("Each one should give %f to Kevin." % abs(people / bill))
 
