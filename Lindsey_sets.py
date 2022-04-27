#this my my python set
thisset = {"cat","dog","rabbit"}
print(thisset)
#im using the print method to skip a line to make my code more readable
print()


#in the next line im iterating over the set by creating a for loop
for i in thisset:
  print(i)
  print()
  
  

# in this new line i will add a new member to my set

thisset = {"cat","dog","rabbit"}
thisset.add("turtle")
print(thisset)
print()



# in the next line i will be adding my phones into my set by using the update method

thisset = {"cat","dog","rabbit"}
phones = {"samsung","nokia","huawei","hisense"}
thisset.update(phones)
print(thisset)
print()



#in the next line i will add list items to my set 
thisset = {"cat","dog","rabbit"}
mylist = ['black','white','brown']
thisset.update(mylist)
print(thisset)
print()

#in the next line i will be removing an item if it is present by using remve()method
thisset= {'cat','dog','rabbit'}
thisset.remove('dog')
print(thisset)
print()

# in the next line we will find a intersection 
a = {1,2,3,4}
b = {3,4,5,6}
c = a.intersection(b)
print(c)
print()

# the next line i will create a union of sets
a = {1,2,3,4}
b = {3,4,5,6}
c = a.union(b)
print(c)
#what this union code did, it excluded the duplicates
print()

# in the next line i will create a set difference
a = {1,2,3,4}
b = {3,4,5,6}
c = a.difference(b)
print(c)
print()

#in this line i will show u howto use symmetric_difference
a = {1,2,3,4}
b = {3,4,5,6}
c = a.symmetric_difference(b)
print(c)
print()

#howto check if my set is not a subset from another subset
a = {1,2,3,4}
b = {3,4,5,6}
c = a.issubset(b)
print(c)
print()

#howto create a shallow copy of set
a = {1,2,3,4}
i = a.copy()
print(i)
print()

#this is howto remove all element from a set
a = {1,2,3,4}
a.clear()
print(a)
print()

#in the new line i will turn a list into a frozenset
a = [1,2,3,4]
i = frozenset(a)
print(i)
print()


#in this line i will find the max value inside a set

a = {1,2,3,8,5}
i = max(a)
print(i)
print()

#in this line i will find the minimum value
a = {1,2,3,8,5}
i = min(a)
print(i)
print()

#in this line we will check the lenght of a set or howmuch items are inside
a = {1,2,3,8,5}
i = len(a)
print(i)
print()

#in this line we will check if a given value is present inside a set
a = {1,2,3,8,5}
if 8 in a:
  print("yes,'8' is in this set")
  print()
  
# in this line we will check if 2 sets have common elements
a = {'rabbit','cat','dog'}
b = {5,6,7,8,9,'dog','cat'}
c = a.isdisjoint(b)
print(c)
#it found dog and cat in both sets thats why we get false.
print()


# in this line we will check out the issuperset
a = {1,2,3,4,5}
b = {6,7,8,9}
c = a.issuperset(b)
print(c)

#example if set b had 1,2,3 as a value the result would be true
print()

# in this line we going to use a for Loop to find a element thats not in another set
a = {1,2,3,4}
b = {3,5,6,7,8}
c = a.difference(b)
print(c)
print()

# remove a intersection of the second  set in the first set
cars = {'ford','nissan,lexus'}
bikes = {'ford','yamaha','suzuki'}
cars.difference_update(bikes)
print(cars)
{'nissan,lexus'}
print(bikes)
{'yamaha', 'suzuki', 'ford'}

