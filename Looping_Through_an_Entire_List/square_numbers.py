# Make a list of the first 10 square numbers

squares =[]
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print (squares)

# A few Python functions are useful (when) for working with lists.
# print a minimum in the list
print (min(squares))

# print a maximum in the list

print (max(squares))
