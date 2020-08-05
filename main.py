#############################################
#------------FUNCTIONS FOR FILES------------#
#this is a function that opens files
def open_file(filename):
	f = open(filename, "r")
	sample = f.readlines()
	output = []
	for line in sample:
		line_words = []
		for word in line.split():
			line_words.append(word.lower())
		output.append(line_words)
	return (output)
	
#this is a function that writes files
def write_file(filename, data):
	new_file = open(filename, "w")
	for sentence in data:
		for word in sentence:
			new_file.write(word + " ")
		new_file.write("\n")
	new_file.close()

##############################################
#------------FUNCTIONS FOR CIPHER------------#
def encrypt_letter(letter, shift): 
  shiftedChar = chr(ord(letter) + shift)
  if ord(shiftedChar) > ord('z'):
    shiftedChar = chr(ord(shiftedChar) - 26)
  return shiftedChar

def decrypt_letter(letter, shift): 
  shiftedChar = chr(ord(letter) - shift)
  if (ord(shiftedChar) < ord('a')):
    shiftedChar = chr(ord(shiftedChar) + 26)
  return shiftedChar

#----------------------------------------------#
def encrypt_word(word, key):
  #assigned empty string to return
  encrypted_word = ""
  #for each index in the length of the word
  for index in range(len(word)):
    #conditional if index of the word is >= length of the key 
    if index >= len(key):
      shift = ord(key[index%len(key)].lower()) - ord("a")
    else:
      shift = ord(key[index].lower()) - ord("a")
    # adds encrypted letter to encrypted_word
    encrypted_word += encrypt_letter(word[index].lower(), shift)
  return encrypted_word

def decrypt_word(word, key): 
  decrypted_word = ""
  for index in range(len(word)):
    #conditional if index of the word is >= length of the key 
    if index >= len(key):
      shift = ord(key[index%len(key)].lower()) - ord("a")
    else:
      shift = ord(key[index].lower()) - ord("a")
    # adds decrypted letter to decrypted_word
    decrypted_word += decrypt_letter(word[index].lower(), shift)
  return decrypted_word
  
#------------------------------------------------#

def encrypt_message(message, key):
  #assign empty list message to return
  encrypted_message = []
  #for each sentence in the message
  for line in message:
    encryptedSentence = []
    #for each word in the sentence
    for word in line:
      #append each encrypted word to sentence
      encryptedSentence.append(encrypt_word(word, key))
      #append each of those sentences to message
    encrypted_message.append(encryptedSentence)
    #return encrypted_message
  return encrypted_message

def decrypt_message(message, key):
  #assign empty list message to return
  decrypted_message = []
  #for each sentence in the message
  for sentence in message:
    decryptedSentence = []
    #for each word in the sentence
    for word in sentence:
      #append each encrypted word to sentence
      decryptedSentence.append(decrypt_word(word, key))
    #append each of those sentences to message
    decrypted_message.append(decryptedSentence)
    #return decrypted_message
  return decrypted_message

############TESTING CODE HERE#####################
###-----TESTING FUNCTIONS THROUGH PRINTING-----###
#testing encryption and decryption of a letter
print('>>ENCRYPTED letter a is:', encrypt_letter('a', 5))
print('>>DECRYPTED letter f is:', decrypt_letter('f', 5))
#testing encryption and decryption of a word
print(encrypt_word('cat', 'dog'))
print(decrypt_word('foz', 'dog'))

###-----TESTING MESSAGES THROUGH FILES-----###
#testing encryption of a message 
plain_text = open_file('plain_text')
encrypt_plain = encrypt_message(plain_text, 'dog')
write_file('encrypt_plain', encrypt_plain)
#testing decryption of a message 
decrypt_plain = decrypt_message(encrypt_plain, 'dog')
write_file('decrypt_plain', decrypt_plain)


