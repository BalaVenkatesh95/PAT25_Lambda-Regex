'''
Lamdbda function to check element in list is integer or String
'''

#Using map()
mixed_list = [5, 'HELLO', 80.3, 'WORLD', 3, 'BALA', 30.5]
int_or_string = lambda x : isinstance(x, (int, str))
result_list = list(map(int_or_string,mixed_list))
print(result_list)


#Using filter()
mixed_list = [5, 'HELLO', 80.3, 'WORLD', 3, 'BALA', 30.5]
int_or_string = lambda x : isinstance(x, (int, str))
result_list = list(filter(int_or_string,mixed_list))
print(result_list)

'''
Note:
isinstance() function:
 To check if an object is an instance of a specified class ,
 in our case we are validating objects in provided list is
 instance of str or int.
 
 map() - returns result value of all elements present in class
 filter() - returns result with values which satisfied given condition
 
'''
