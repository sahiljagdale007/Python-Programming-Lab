list = ["sahil", 1234, "c",55,"Jagdale"]

print(list[0])
print(list[1])
print(list[2])
print(type(list))
print(list)


#delete operation
del list[0]
print(list)

#pop operation
print(list.pop(0))
print(list)

#remove operaiton
list.remove("Jagdale")
print(list)

#Clear operation
list.clear()
print(list)