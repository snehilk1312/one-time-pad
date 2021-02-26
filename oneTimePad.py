#! /usr/bin/env python3

import os
import base64

plaintext = input("Enter the Plaintext:	")
length = len(plaintext)


key = os.urandom(length)
#print(key)


#key_b64 = base64.b64encode(key)
#print(key_b64)


def encrypt(plaintext, key):
	#print(len(key))
	r = ''
	for i in range(len(key)):
		c =  ord(plaintext[i])^key[i]
		r += chr(c)
		#print(chr(c),c)
	#print(r.encode())
	retval = base64.b64encode(r.encode())
	return retval


ciphertext = encrypt(plaintext, key)
print("Encrypted text is:	", ciphertext)


def decrypt(ciphertext, key):
	r = ''
	med1 = base64.b64decode(ciphertext)
	med2 = med1.decode()
	#print(type(med2), len(med2))
	for i in range(len(key)):
		c = ord(med2[i])^key[i]
		#print(c)
		r += chr(c)
	#print(r)
	return r

decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text is:	", decrypted_text)
