# num = (input('Enter a list of numbers: ')).split(' ')
#
# list_num = list(num)
# print(list_num)

a = (input('Enter a list of numbers: ')).split(' ')
list_a = list(a)


even = 0
odd = 0

for i in range(0, len(list_a)):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even: %d, odd: %d" % (even, odd))