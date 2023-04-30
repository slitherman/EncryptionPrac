from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#uses the same salt and password to generate the same key as the encryption script
#uses the key to decrypt the file
salt = b'\xbb\x06\xa4\xaa\xa8d\xf2h\x1d\x19\xab;\x93\x13\x87\x02\x93\xfd|"\xbf&\xe4\x10\xd2\xa2\x92gh&\xb9\xe4"\xb3\xc7{\x15I\xad\xdfW\xa2\xd7\x00\xbev\x8a\x91\x97Xa\x02\xb0\xba\xe0\x12\x9b\xf6I\x89\x0bN]\xc0\xa3\x87W\xb9\x1cy\\\x96*3T\xbf\x0e\xff\xdd\x19I`?0,!\xa9\xdf\xb66\x96\xf2\xbc\xa2XbP\x8a\x84\x93\xabA+\x84\x85L\xefjMf\xa3\xaa\xe7j\xdb\x13\xec\xaf\xc3\\]\x10\x7f\x7f\x90\xe4t\n'
password ="1234"

key = PBKDF2(password,salt,dkLen= 32)

with open("encrypted.bin", "rb") as f:
    iv = f.read(16)
    data_to_be_decrypted = f.read()


cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original_msg = unpad(cipher.decrypt(data_to_be_decrypted), AES.block_size)
print(original_msg)