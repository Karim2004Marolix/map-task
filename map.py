#map and lamda
#addition
numbers = (1,2,3,4,5,6,7,8,9) 
result = map(lambda x: x + x, numbers) 
print(list(result))


# Add two lists using map and lambda 
  
numbers1 = [1,2,3] 
numbers2 = [4,5,6] 
numbers3 = [10,15,16]
  
result = map(lambda x, y, z: z - x + y, numbers3, numbers1, numbers2) 
print(list(result)) 




# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 
test = list(map(list, l)) 
print(test)