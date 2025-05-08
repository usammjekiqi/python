from code import interact

my_Set={1,2,3,4,2,2,1,6}
print(my_Set)
my_Set_1=set([1,2,3,4,4,4,2])
print(my_Set_1)
A={1,2,3,}
B={3,4,5}
#finde the union
unioni=A.union(B) #union = a/b
print(unioni)

#interact()
prejra=A.intersection(B)#prejre =a&b
print(prejra)

#diferenca
diferenca=A.difference(B) #defiernca = a-b
print(diferenca)

#diferenca simetrike
d_simetrike=A.symmetric_difference(B) #d_simetrike=a^b
print(d_simetrike)

#add element
A.add(6)
print(A)

#remove element
A.remove(6)

#discard - remove an element without error if it does noe egrist
A.discard(100)

#remuvese all element
A.clear()

#find the numer of element of a set
print(len(A))

list= [1,2,2,3,3,4,4]
list_c=set(list)
print(list_c)

b= {"pila", "minus", "plus"}
t= {"pila", "hesht", "tik"}
int=b&t
print(int)

#L=set[1,2,3,4,5,5]
#numri=1
#print(numri in L)
#print(numri not in L)