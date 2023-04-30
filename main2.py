from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#opens the encryption file and decrypts it

with open("key.bin", "rb") as f:
    key = f.read()

with open("encrypted.bin", "rb") as f:
    iv = f.read(16)
    data_to_be_decrypted = f.read()


cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original_msg = unpad(cipher.decrypt(data_to_be_decrypted), AES.block_size)
print(original_msg)