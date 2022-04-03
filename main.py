# Write your introduction function here:
def introduction(first_name, last_name):
    last = last_name + ', '
    first = last + first_name + ' '
    full_introduction = first + last_name
    return full_introduction


print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
