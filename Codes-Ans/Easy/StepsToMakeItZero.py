# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
# Input : num = 14
# Output : 6

num = int(input("Enter the number please : "))
counter = 0  # To count the number of processess
while(num != 0):
    if(num % 2 == 0):
        num = num / 2
    else:
        num = num - 1
    counter = counter + 1
print(counter)
