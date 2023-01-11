# lambda functions

# create a lambda function to do *
my_function = lambda x : 2 * x

print(my_function(4))

# use the list below and sort the list on the second element of each tuple

list1 = [(2,5), (9,4), (0,5) ,( 4,7), (9 , 1), (0 , 3)]

list1.sort(key = lambda x : x[1])

print("Sorted list based on second element is" , list1)

# Use list2 and add 10 to each element ( use lambda as your function)

list2 = [2, 4, 6, 8, 12, 14, 16]

added_list = list(map(lambda x : x + 10 , list2))

print(" New added list is ", added_list)

# replace ages less than 11 in kid and more or equal in teenage
age_list = [5,6,7,8,10,12,13,16,19]

new_age = list(map(lambda x : 'kid' if x < 11 else 'teenage' , age_list))

print(new_age)

# print the teenage ones

teen_list = list(filter(lambda x : x == 'teenage', new_age))

print(teen_list)