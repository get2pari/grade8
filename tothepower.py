a = input("Enter the number:")
a_int=int(a)
print(type(int(a)))
print(type(a))
print(type(a_int))
b = input("Enter the required power:")
b_int=int(b)
print(type(b_int))
print(type(b))
output=1

for x in range(b_int):
    output=output*a_int

print(output)