print "Hola mundo"

n = int(input("Enter the number of values to add: "))
numbers = []

for i in range(n):
  num = float(input(f"Enter number {i+1}: "))
  numbers.append(num)

total = sum(numbers)
print(f"The sum of the numbers is: {total}")
