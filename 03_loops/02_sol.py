# SUM OF EVEN NUMBER
n=int(input("Enter "))
sum_even = 0



for i in range (1,n+1):
    if i % 2 == 0:
        
        sum_even += 1


print("sum of even numbers :", sum_even)