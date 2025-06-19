import  numpy as np


#create a 2d array
arr_2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)


element=arr_2d[1,2]
print(element)

#dimensions
dimensionet=arr_2d.ndim
print(dimensionet)


#seperate
sub_arrey=arr_2d[:2,:2]#selectes the first 2 rows nad the first two culumns

print(sub_arrey)



sub_arrey=arr_2d[-4:,-4:] #the lest 4 leemenst of each row
print(sub_arrey)



sum=np.sum(arr_2d)
print(sum)


mesatarja=np.mean(arr_2d)
print(mesatarja)


