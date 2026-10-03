"""Question 1 — Sum of numbers
Ask the user for a number n, then use a for loop to calculate the sum of numbers from 1 to n.
Example:
Enter a number: 5
Sum = 15
Because:
1 + 2 + 3 + 4 + 5 = 15"""

number=int(input("enter a number"))
sum=0

for i in  range(1,number+1):
   sum = sum+i
print(sum)
print("hello sumit")
