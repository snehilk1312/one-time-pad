#! /usr/bin/env python3

import os
import base64

def encrypt(plaintext, key):
	r = ''
	for i in range(len(key)):
		c =  ord(plaintext[i])^key[i]
		r += chr(c)
	return r


def decrypt(ciphertext, key):
	# we will use the property of xor operation
	return encrypt(ciphertext, key)



plaintext = input("Enter the text to be Encrypted:	")
length = len(plaintext)

key = os.urandom(length)

# Encryption
ciphertext = encrypt(plaintext, key)
print("Encrypted then base64 encoded text is:       ", base64.b64encode(ciphertext.encode()))
print("Encoded base64 key is:	", base64.b64encode(key))

# Decryption
decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text is:      ", decrypted_text)

