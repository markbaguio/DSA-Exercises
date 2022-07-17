"""Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function"""
odd_numbers = []
max = int(input("Input max number: "))
print(max)

for i in range(1, max):
    if(i % 2 == 1):
        odd_numbers.append(i)

print("Odd Numbers List: ", odd_numbers)
