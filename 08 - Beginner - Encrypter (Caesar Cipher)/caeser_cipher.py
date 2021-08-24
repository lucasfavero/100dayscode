import string
import art

alphabet = string.ascii_lowercase + string.ascii_lowercase
punctuation = string.punctuation
space = string.whitespace


def encrypt(encrypted_message, encrypted_shift_num):
    cipher_message = []
    for digit in encrypted_message:
        for char in range(len(alphabet)):
            if (digit == alphabet[char]) and (digit not in punctuation + space):
                cipher_message += alphabet[char + encrypted_shift_num]
                break
            elif digit in punctuation + space:
                cipher_message += digit
                break
    print(f"{''.join(cipher_message)}")


def decrypt(decrypted_message, decrypted_message_shift_num):
    decrypted_cipher_message = []
    for digit in decrypted_message:
        for char in range(len(alphabet)):
            if (digit == alphabet[char]) and (digit not in punctuation + space):
                decrypted_cipher_message += alphabet[char - decrypted_message_shift_num]
                break
            elif digit in punctuation + space:
                decrypted_cipher_message += digit
                break
    print(f"{''.join(decrypted_cipher_message)}")


print(art.logo)

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()

if direction == "encode":
    message = input("Type your message: ").lower()
    shift_num = int(input("Type the shift number: "))
    encrypt(message, shift_num)
elif direction == "decode":
    message = input("Type your message: ").lower()
    shift_num = int(input("Type the shift number: "))
    decrypt(message, shift_num)
