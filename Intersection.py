def create_list(list1, list2):
    return list(set(list1) & set(list2))

print(create_list([1,2,3,4], [3,4,5,6]))

#Write a program that defines a function sanitize_list() to
#remove all duplicate entries from the list that it receives.

def sanitize_list(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5]
print(sanitize_list(numbers))