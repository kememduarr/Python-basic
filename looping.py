#This is loop. Also known as for or while function in python

#Here i'll give u some Example how to make loop

#First u need a list or a text

#if List was ur target

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in a:
	 print(x)#U can also combine it with if else function
#The x will represent the number or value inside the list

#If text is your target

a = "abcdefghijklmnop"
for x in a:
	print(x)#The x will represent the alphabets inside the text

#Now start to while
#While function will start and never end before it get it's Exceptional condition

#Example
a = 0
while a > 10: #So it will stop when a == 10
	print(a)
	a += 1

#or U can make with boolean

x = False
while not x:
	a = input("Input answer: ")
	print(a)
	if a.lower() == "done":
		x = True
