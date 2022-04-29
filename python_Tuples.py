# in this python program im creating a tuple
thistuple=("chicago","vip","mega","kingdom")
print(thistuple)
print()

# tuple with different data types
thistuple=("chicago",3,False,5.8)
print(thistuple)
print()

# python tuple with numbers one item will be printed
thistuple=(1,2,3,4,5)
for i in thistuple:
  print(i)
  print()

#  unpack tuple in different variables
cars = ("nissan", "honda", "ford")

(blue, purple, white) = cars

print(blue)
print(purple)
print(white)
print()

# add a item in a tuple
cars=("honda","bmw","ford")
bikes=list(cars)
bikes[2] ="suzuki"
cars=tuple(bikes)
print(cars)
print()

# convert a tuple to a string 
tuple1=("h","a","s","h")
str="".join(tuple1)
print(str)
print()

#get the 4th element and 4th element from last of a tuple
tuple1=(1,2,3,4,5,6)
i=tuple1.index(2)
print(i)
print()

