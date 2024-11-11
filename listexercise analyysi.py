#Exercise 1.

mylist = ["apple", "banana", "cherry"]

#print all
print(mylist)
#print 1 and 2
print(mylist[:2])

#check if cherry is in the list.
if "cherry" in mylist:
    print("Yes. 'cherry' is in the list.")
else:
    print("No cherries here.")


#Exercise 2.

thrownDiceNumbers = [1,2,3,4,5]

#print list of numbers.
print(thrownDiceNumbers)
#print sum of items.
print(sum(thrownDiceNumbers))
#print highest value in list.
print(max(thrownDiceNumbers))