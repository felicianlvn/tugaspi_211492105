val = int(input("Enter input number : "))
 
n = 0
if val == 0:
    print("The sum is 0")
else:
    for i in range(1, val + 1):
        n = n + i
    print("The sum of", val,"is",n)