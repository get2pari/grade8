a = int(input("Enter the lower limit:"))
b = int(input("Enter the upper limit:"))
even = 0
odd = 0
for i in range(a, b+1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
else:
    print("Loop terminated successfully")
print("The sum of all the even numbers in the given series is:", even)
print("The sum of all the odd numbers in the given series is:", odd)
