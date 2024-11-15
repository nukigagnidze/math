# # 1
# num = int(input("Enter a number: "))
# sum = 0

# for i in str(num):
#     sum += int(i)

# if sum % 2 == 0:
#     print("მარტივია")
# else:
#     print("არამარტივია")


# def is_prime(num):
#     """ამოწმებს, არის თუ არა რიცხვი მარტივი"""
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True


# def prime_factors(num):
#     """დაშლის რიცხვს მარტივ მამრავლებად"""
#     factors = []
#     divisor = 2
#     while num > 1:
#         while num % divisor == 0:
#             factors.append(divisor)
#             num //= divisor
#         divisor += 1
#     return factors


# def main():
#     try:
#         number = int(input("შეიყვანეთ რიცხვი: "))
#         if is_prime(number):
#             print(f"{number} არის მარტივი რიცხვი.")
#         else:
#             factors = prime_factors(number)
#             print(f"{number} არის შედგენილი რიცხვი და მისი მარტივი მამრავლებია: {factors}")
#     except ValueError:
#         print("გთხოვთ, შეიყვანოთ მთელი რიცხვი!")


# if _name_ == "_main_":
#     main()

