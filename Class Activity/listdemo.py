import random
a = []
x = 0

a.append(4)
a.append(5)
a.append(6)
a.insert(0,1)
#index error: index out of range means you are trying to use a number that does not exist in the list

print(a)

b = [1,1,3,5,4]
b.remove(1) #remove a specific number
del b[0] #remove a number in a certain position
print(b.pop())#take the last thing off the list
print(b)
print(b[-1])#gives you the last thing in the list, [-1] is the same as [len(b)-1]



c, d=5, 7
c, d=d, c #swap

a = c
c = d
d = a

e = [1,2,3,7,5,6,4]
e[3],e[6] = e[6], e[3]
print(e)


g = []
for x in range(100):
	g.append(7*x)
print(g)

f = []
for z in range(10):
	f.append(random.randrange(100))
	f.sort()
print(f)
#for x in range(0,700,7) numbers in the parenthesis are (starting number, ending number, step)

