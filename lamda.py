def cube(y):
    return y*y*y
lambda_cube = lambda y: y*y*y
print("Using lambda function, cube:", lambda_cube(5))


# iterate on each lambda function
# and invoke the function to get the calculated value
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())