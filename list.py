# l=[]
# print(type(l))

#append
# l.append(5)
# print(l)
# l.append(10)
# l.append(50)
# l.append(34)
# print(l)
# l.append([100,200,300])
# print(l)
# l.extend([1000,2000,3000])
# print(l)
# l.insert(6,25)
# print(l)
# l.remove(10)
# print(l)
# if 10000 in l:
#     l.remove(10000)
# print(l)
# l.pop(3)
# print(l)
l1=[1,2,3,4,5,[100,200,300]]
print(l1)
# l1.clear()
# print(l1)
# del l1
# l1=len(l1)
# print(l1)
# l=max(l)
# print(l)
# l1=min(l1)
# print(l1)
# l.sort(reverse=True)
# print(l)
# l2=sorted(l)
# print(l2)

# import copy
# l2=copy.copy(l1)
# print(l2)
# l1[0]=1000
# print(l1)
# print(l2)


import copy
l2=copy.deepcopy(l1)
print(l2)
l1[0]=1000
print(l1)
print(l2)
