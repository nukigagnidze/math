num = int(input("Enter a number: "))
sum = 0

for i in str(num):
    sum += int(i)

if sum % 3 == 0:
    print("იყოფა")
else:
    print("არ იყოფა")