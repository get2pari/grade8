in_list = []# [56, 34, 346, 386, 48, 259, 47]

sorted_list = []

def find_smallest_and_move_to_op():
    # find smallest number, smallest
    smallest = 999
    for x in in_list:
        if x < smallest:
            smallest = x
            print (smallest)
    sorted_list.append(smallest)
    in_list.remove(smallest)

    # add smallest number to sorted_list
    # remove smallest number from in_list
for x in range(10):
    print(x)
    a = input("Enter the number:")
    print(a)
    in_list.append(int(a))
    if a == "end":
        break

for x in range(len(in_list)):
    find_smallest_and_move_to_op()


#find_smallest_and_move_to_op()
#find_smallest_and_move_to_op()
print(in_list)
print(sorted_list)
