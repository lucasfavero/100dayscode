import string
import random

print("Welcome to the Password Generator!")
letters_len = int(input("How many letters would you like?: "))
symbols_len = int(input("How many symbols would you like?: "))
numbers_len = int(input("How many numbers would you like?: "))

letters = string.ascii_letters
symbols = string.punctuation
nums = string.digits

password = random.sample(letters, letters_len) + random.sample(symbols, symbols_len) + random.sample(nums, numbers_len)
password = "".join(random.sample(password, len(password)))

print(password)