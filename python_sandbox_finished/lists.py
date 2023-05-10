# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get the last value
print(fruits[-1])

# Get length
print(len(fruits))

# Append to list (add to last)
fruits.append('Mangos')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove a specific target from list
fruits.remove('Grapes')

# Remove with pop
fruits.pop(2)

# Change value
fruits[0] = 'Blueberries'

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
