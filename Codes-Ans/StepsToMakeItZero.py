

num = input("Enter the number please : ")
counter = 0  # To count the number of processess
while(num == 0):
    if(num % 2 != 0):
        num = num - 1
    else:
        num = num % 2
    counter = counter + 1
print(counter)
