#numeric DT
number = 10
percentage = 10.5
c = 10 + 5j
print(number,type(number))
print(percentage,type(percentage))
print(c,type(c))

# # sequence DT
s="kahaar"
l=[1,2,3,4,5]
t=(1,2,3,4,5)
print(s,type(s))
print(l,type(l))
print(t,type(t))


#boolean DT
b=True
b1=False    
print(b,type(b))
print(b1,type(b1))    
print(b + b1)


#Mapping data types - Dictionary
d={"name":"kahaar","age":23,"city":"hyderbad"}
print(d,type(d))


#Sets
s={1,2,3,4,5,7,3,2}
print(s,type(s))

# empty data types

lst1=[] #list
t1=() #tuple
str1="" #string
d1={} #dictionary
s1=set() #set
print(lst1,type(lst1))
print(t1,type(t1))
print(str1,type(str1))
print(d1,type(d1))
print(s1,type(s1))
print(type(str()))

# explicit TC
n=input()
print(n,type(n))
n=int(n)
print(n,type(n))


#Implicit TC
n1 = 100
n2 = 10.5
print(n1,type(n1))
print(n2,type(n2))
n3 = n1 + n2
print(n3,type(n3))

str1 = "kahaar"
print(str1) 