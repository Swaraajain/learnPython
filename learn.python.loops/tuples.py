# tuples are immutable where as lists are mutable.
# List can hold homogeneous items.
# Tuples can only hold hetrogeneous items

my_tuple = (1,2,3,[1,2,3])
my_tuple[3][1] =4
print(my_tuple[3])

my_tuple_1 = ('a','p','p','l','e')
print(my_tuple_1.index('p'))

x = 23
print(x)


list=['banana','apple','chickoo','mango','kiwi','watermelon']
for x in list:
    if 'a' in x:
        print(x)