# Encryption by key-word

VERSION = "0.0 BUILD"
MODS = "\nen - to encrypt\nde - to decrypt\nexit - to close programm"

def smart_input(type):
	if type == 0:
		print("Enter your keyword.")
		while True:
			key = input("*: ")
			if not key.isalpha():
				print("Keyword must be only in [A-Z] range. Try again")
			elif len(set(list(key))) < len(key) or len(key) > 26:
				print("Letters are repeated in the word. Try again.")
			else:
				break
		return key.upper()
	elif type == 1:
		print("Enter your message.")
		while True:
			msg = input("*: ")
			if not msg.replace(" ","").replace(",","").replace(".","").replace("?","").replace("!","").isalpha():
				print("Message can only contain letters, spaces, comas and dots. Try again.")
			else:
				break
		return msg.upper()
	else:
		print("A problem has occured with smart_input!")
		return None

ALPHABET = list("QWERTYUIOPASDFGHJKLZXCVBNM")
ALPHABET.sort()

mode = VERSION
shuffled, secret = [], []
keyword, message = "", ""


print("Hello. Key-word ecnrypter v. {}".format(VERSION))
print("Available mods: {}".format(MODS))

while mode != "exit":
	mode = input("*: ")

	if mode == "en":
		while True:
			secret = []
			keyword = smart_input(0)
			shuffled = list(keyword)

			for letter in ALPHABET:
				if letter not in shuffled:
					shuffled.append(letter)

			message = smart_input(1)

			for letter in list(message):
				if letter not in ALPHABET:
					secret.append(letter)
				else:
					secret.append(shuffled[ALPHABET.index(letter)])

		
			print("Encyrpted message: ")
			print(''.join(secret).capitalize())

			print("Continue? (y - yes, else - no)")
			mode = input("*: ")
			if mode != "y":
				mode = ""
				break

	elif mode == "de":
		while True:
			secret = []
			message = smart_input(1)
			keyword = smart_input(0)
			shuffled = list(keyword)

			for letter in ALPHABET:
				if letter not in shuffled:
					shuffled.append(letter)

			for letter in list(message):
				if letter not in ALPHABET:
					secret.append(letter)
				else:
					secret.append(ALPHABET[shuffled.index(letter)])

			print("Decrypted message: ")
			print(''.join(secret).capitalize())

			print("Continue? (y - yes, else - no)")
			mode = input("*: ")
			if mode != "y":
				mode = ""
				break

	elif mode == "exit":
		break
	else:
		print("Wrong input, try again.")