# creating an outer and inner function
def outerFunc():
   sample_str = 'marolix technologies hydarabad'
   def innerFunc():
      print(sample_str)
   innerFunc()
outerFunc()

# creating an outer function and  calling an inner function inside the outer function
def outerFunc():
   sample_str = 'python developer backend operations'
   def innerFunc():
      sample_str = 'Welcome to the marolix'
      print(sample_str)
   innerFunc()
   print(sample_str)
outerFunc()

#numarical
def number_1(a):
   def number_2(b):
      return a*b
   return number_2
print(number_1(5)(18))