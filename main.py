import random
import string




chars = " " + string.punctuation + string.digits + string.ascii_letters + string.hexdigits
chars = list(chars)
key = chars.copy()

random.shuffle(key)
#print(f" chars :{chars}")
#print(f" key :{key}")

#ENCRYPTION
plain_text = input(" Enter a message to encrypt")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f" Original message {plain_text}")
print(f" Encryptedd message {cipher_text}")


#DECRYPTION
cipher_text2 = input(" Enter a message to decrypt")
plain_text2 = ""
for letter in cipher_text2:
    index = key.index(letter)
    cipher_text += chars[index]

print(f" Encryptedd message {cipher_text}")
print(f" Original message {plain_text}")

