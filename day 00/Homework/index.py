# 1
def is_divisible_by_2(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = int(input("შეიყვანეთ რიცხვი: "))

if is_divisible_by_2(num):
    print(f"{num} იყოფა 2-ზე.")
else:
    print(f"{num} არ იყოფა 2-ზე.")

# 2
def is_divisible_by_3(number):
    if number % 3 == 0:
        return True
    else:
        return False

num = int(input("შეიყვანეთ რიცხვი: "))

if is_divisible_by_3(num):
    print(f"{num} იყოფა 3-ზე.")
else:
    print(f"{num} არ იყოფა 3-ზე.")

# 3
def is_divisible_by_5(number):
    if number % 5 == 0:
        return True
    else:
        return False

num = int(input("შეიყვანეთ რიცხვი: "))

if is_divisible_by_5(num):
    print(f"{num} იყოფა 5-ზე.")
else:
    print(f"{num} არ იყოფა 5-ზე.")