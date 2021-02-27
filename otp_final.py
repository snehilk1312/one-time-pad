import os
import base64
import argparse

def encrypt(plaintext, key):
	r = ''
	for i in range(len(key)):
		c =  ord(plaintext[i])^key[i]
		r += chr(c)
	return r



def decrypt(ciphertext, key):
	# we will use the property of xor operation
	return encrypt(ciphertext, key)

parser = argparse.ArgumentParser()
parser.add_argument("-e",'--encrypt_', help="encrypts")
parser.add_argument("-d" ,'--decrypt_',help="decrypts")
parser.add_argument("-f",'--encrypt_file', help="encrypts file")
parser.add_argument("-k", '--key',help="key for decryption")

args = parser.parse_args()
if args.key:
	f = open(args.key, 'rb')
	key = f.read()
	f.close()
	print(key)
	with open(args.decrypt_, 'r') as file:
		cipher = file.read() #.rstrip('\n')
	decrypted_text = decrypt(cipher, key)
	print("Decrypted Text is:	", decrypted_text)
	decrypted_file = open('plaintext.txt','w')
	decrypted_file.write(decrypted_text)
	decrypted_file.close()

else:
	if args.encrypt_:
		plaintext = args.encrypt_
		length = len(plaintext)
		key = os.urandom(length)
		key_export = base64.b64encode(key)
		ciphertext = encrypt(plaintext, key)
		print("Encrypted text is:       ", base64.b64encode(ciphertext.encode()).decode())
		print("Encoded base64 key is:	", key_export.decode())
		key_file = open("key.txt", "wb")
		key_file.write(key)
		key_file.close()
		cipher_file = open("cipher.txt", "w")
		cipher_file.write(ciphertext)
		cipher_file.close()



	if args.encrypt_file:
		with open(args.encrypt_file, 'r') as file:
			plaintext = file.read()

		length = len(plaintext)
		key = os.urandom(length)
		key_export = base64.b64encode(key)
		ciphertext = encrypt(plaintext, key)
		print("Encrypted text is:       ", base64.b64encode(ciphertext.encode()).decode())
		print("Encoded base64 key is:   ", key_export.decode())
		key_file = open("key.txt", "wb")
		key_file.write(key)  
		key_file.close()
		cipher_file = open("cipher.txt", "w")
		cipher_file.write(ciphertext)
		cipher_file.close() 
