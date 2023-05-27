import random
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# We will run the function only once to fill the set of
# prime numbers
# A set will be the collection of prime numbers,
# where we can select random primes p and q
prime = set()
public_key = None
private_key = None
n = None


def primefiller():
	# Method used to fill the primes set is Sieve of
	# Eratosthenes (a method to collect prime numbers)
	seive = [True] * 250
	seive[0] = False
	seive[1] = False
	for i in range(2, 250):
		for j in range(i * 2, 250, i):
			seive[j] = False

	# Filling the prime numbers
	for i in range(len(seive)):
		if seive[i]:
			prime.add(i)


# Picking a random prime number and erasing that prime
# number from list because p!=q
def pickrandomprime():
	global prime
	k = random.randint(0, len(prime) - 1)
	it = iter(prime)
	for _ in range(k):
		next(it)

	ret = next(it)
	prime.remove(ret)
	return ret


def setkeys():
	global public_key, private_key, n
	prime1 = pickrandomprime() # First prime number
	prime2 = pickrandomprime() # Second prime number

	n = prime1 * prime2
	fi = (prime1 - 1) * (prime2 - 1)

	e = 2
	while True:
		if math.gcd(e, fi) == 1:
			break
		e += 1

	# d = (k*Φ(n) + 1) / e for some integer k
	public_key = e

	d = 2
	while True:
		if (d * e) % fi == 1:
			break
		d += 1

	private_key = d


# To encrypt the given number
def encrypt(message):
	global public_key, n
	e = public_key
	encrypted_text = 1
	while e > 0:
		encrypted_text *= message
		encrypted_text %= n
		e -= 1
	return encrypted_text


# To decrypt the given number
def decrypt(encrypted_text):
	global private_key, n
	d = private_key
	decrypted = 1
	while d > 0:
		decrypted *= encrypted_text
		decrypted %= n
		d -= 1
	return decrypted


# First converting each character to its ASCII value and
# then encoding it then decoding the number to get the
# ASCII and converting it to character
def encoder(message):
	encoded = []
	# Calling the encrypting function in encoding function
	for letter in message:
		encoded.append(encrypt(ord(letter)))
	return encoded


def decoder(encoded):
	s = ''
	# Calling the decrypting function decoding function
	for num in encoded:
		s += chr(decrypt(num))
	return s

def EncryptYourText():
	primefiller()
	setkeys()
	message = initMessageEntry.get()
	if(message == ''):
		messagebox.showerror("Error","Please Enter a message")
	else:
		coded = encoder(message)

		codedMsg = ''.join(str(p) for p in coded)
		plainMessageVar.set(message)
		primeNumberVar.set(n)
		publicKeyVar.set(public_key)
		privateKeyVar.set(private_key)
		encryptedMessageVar.set(codedMsg)

		decoded = decoder(coded)
		decodedMsg = ''.join(str(p) for p in decoded)
		decryptedMessageVar.set(decodedMsg)

		initMessageValue = ''



root = Tk()

# Initialization
plainMessageVar = StringVar()
plainMessageVar.set('')

primeNumberVar = StringVar()
primeNumberVar.set('')

publicKeyVar = StringVar()
publicKeyVar.set('')

privateKeyVar = StringVar()
privateKeyVar.set('')

encryptedMessageVar = StringVar()
encryptedMessageVar.set('')

decryptedMessageVar = StringVar()
decryptedMessageVar.set('')






root.geometry("644x434")
root.title('Mini-Project')

initMessageLabel = Label(text="Message")
initMessageLabel.grid(row=0,column=0,padx=20,pady=20)

initMessageValue = StringVar()

initMessageEntry = ttk.Entry(root, textvariable = initMessageValue)

initMessageEntry.grid(row=0, column=1,padx=10)

initMessageValue = initMessageEntry.get()

ttk.Button(text="Submit",command = EncryptYourText).grid(row=1, column=1)

MessageLabelPlainText = Label(text="Message : ")
MessageLabelPlainText.grid(row=2,column=0)

MessageLabelPlainText1 = Label(textvariable = plainMessageVar)
MessageLabelPlainText1.grid(row=2,column=1)

primeNumberLabel = Label(text="Prime1 * Prime2 : ")
primeNumberLabel.grid(row=3,column=0)

primeNumberLabel1 = Label(textvariable = primeNumberVar)
primeNumberLabel1.grid(row=3,column=1)

publicKeyLabel = Label(text="Public Key : ")
publicKeyLabel.grid(row=4,column=0)

publicKeyLabel1 = Label(textvariable = publicKeyVar)
publicKeyLabel1.grid(row=4,column=1)

privateKeyLabel = Label(text="Private Key : ")
privateKeyLabel.grid(row=5,column=0)

privateKeyLabel1 = Label(textvariable = privateKeyVar)
privateKeyLabel1.grid(row=5,column=1)

encryptedMessageLabel = Label(text="Encrypted Message : ")
encryptedMessageLabel.grid(row=6,column=0)

encryptedMessageLabel1 = Label(textvariable = encryptedMessageVar)
encryptedMessageLabel1.grid(row=6,column=1)

decryptedMessageLabel = Label(text="Decrypted Message : ")
decryptedMessageLabel.grid(row=7,column=0)

decryptedMessageLabel1 = Label(textvariable = decryptedMessageVar)
decryptedMessageLabel1.grid(row=7,column=1)

root.mainloop()