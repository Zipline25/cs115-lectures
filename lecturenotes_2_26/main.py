a = 3
# b = "my name is tristan"
b = 6.5
c = "my name"

if a > b:
  print("something here")

print(type(a))
print(type(b))
print(type(c))

c = 5
print(type(c))

my_list = ["another string",5, "my age", 5.67]
print(type(my_list))

# accessing a list
print(my_list[0])
print(my_list[3])

my_list.append("milk")
print(my_list)

# access first character in string
print(my_list[0][0])

# remove from string
my_list.remove(5)
print(my_list)
my_list.pop(2)
print(my_list)

# get length of list
print(len(my_list))

# exercise with list
todo = ["Call mom", "Walk the dog", "Go to the grocery store"]
todo.append("Read a book")
todo[1] = "Finish homework"
todo.remove("Call mom")
print(len(todo))

print(todo)

coordinates = [
  (100,200),
  (200,300)
]