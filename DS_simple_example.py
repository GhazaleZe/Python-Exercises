# create a dictionary for your courses grades and print the items of it : 
my_dictionary = {'BP' : 'A', 'AP' : 'A+' , 'DS' : 'B'}

print( 'This the Dictionary', my_dictionary)

print( "This the items : " , my_dictionary.items())

# Store the items of the dictionary in a list

List_of_Dictionary = list(my_dictionary.items())

print("list of dictionary : ", List_of_Dictionary)

for course, grade in List_of_Dictionary:
    print(" In course %s the grade is %s" %(course, grade))
