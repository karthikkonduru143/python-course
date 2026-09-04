## sequence data types
#01-list
#list does not have fixed size.
#list is mutable.(we change elements of list)
#list will have duplicate values.
l=[]
lst = [1,2,'hello',3.5,'hello']
lst1=[1,2,]
lst[2]='world'
print(type(l))
print(type(lst))
print("index value 4 is printed:",lst[4])
print("list is updated (hello to world):", lst)

##02-tuple
#tuple has fixed size.
#tuple is immutable.(we cannot change elements of tuple)
t=()
t1=tuple()
t2=(1,2,3,4,5)
print("printing first element using index value:",t2[0])

#03-strings
#string is immutable.(we cannot change elements of string)
s=""
s1=str()
s2="hello"
print(type(s))
print(type(s1))
print(type(s2))
print("printing string:",s2)
