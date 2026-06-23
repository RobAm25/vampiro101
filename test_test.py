#a = "Hello, World!"
#print(len(a))

#txt = "The best things in life are free!"
#if "free" in txt:
#    print ("Yes, 'free' is present.")

#txt2 = "Tell me what you want!"
#if "money" not in txt2:
#    print("No, 'money' is not present.")

#b = "Hello world"
#print(b[-5:-2])

#c = " Hello, World! "
#print(c.strip()) # returns "Hello, World!"

#a = "Hello, World!"
#print(a.replace("H", "J"))

#a = "Hello"
#b = "World"
#c = a + " " + b
#print(c)

#price = 59
#txt = f"The price is {price:.2f} dollars"
#print(txt)

#txt = f"The price is {20 * 59} dollars"
#print(txt)

#txt = "We are the so-called \"Vikings\" from the north."
#print (txt)

# Create the variable
txt =  "Hello, World!"
# Print characters from index 2 to 5
#print(txt[2:5])
# Print in upper case
#print(txt.upper())
# Create the name variable
#name = "Python"
# Print using an f-string
#print(f"I love {name}")

#a = 200
#b = 33

#if b > a:
#  print("b is greater than a")
#else:
#  print("b is not greater than a")

#class myclass():
#  def __len__(self):
#    return 0

#myobj = myclass()
#print(bool(myobj))

#x = 200
#print(isinstance(x, int))

#num = 6
#x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"
#print(x)

#x = 5
#print(x > 0 and x < 10)

#x = 5
#print(not(x > 3 and x < 10))

#fruits = ["apple", "banana", "cherry"]
#print("pineapple" not in fruits)

#mylist = ["apple", "banana", "cherry"]
#if "banana" in mylist:
#    print("Yes, banana is in the list.")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist2)

#Insert an item as the second position:
thislist3 = ["apple", "banana", "cherry"]
thislist3.insert(2, "watermelon")
print(thislist3)

#Add to list
thislist4 = ["apple", "banana", "cherry"]
thislist4.append("orange")
print(thislist4)

#Add the elements of tropical to thislist:
thislist5 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist5.extend(tropical)
print(thislist5)

#Remove "banana"
thislist6 = ["apple", "banana", "cherry"]
thislist6.remove("banana")
print(thislist6)

#Remove the second item with pop()
thislist7 = ["apple", "banana", "cherry"]
thislist7.pop(1)
print(thislist7)

#Remove the first item with del:
thislist8 = ["apple", "banana", "cherry"]
del thislist8[0]
print(thislist8)

#Clear the list content:
thislist9 = ["apple", "banana", "cherry"]
thislist9.clear()
print(thislist9)

#Print all items in the list, one by one:
thislist10 = ["apple", "banana", "cherry"]
for x in thislist10:
  print(x)

#Print all items by referring to their index number:
thislist11 = ["apple", "banana", "cherry"]
for i in range(len(thislist11)):
  print(thislist11[i])

#Print all items, using a while loop to go through all the index numbers
thislist12 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist12):
  print(thislist12[i])
  i = i + 1

#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[]

for x in fruits:
    if "a" in x:
       newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the : operator:
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Loop through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1