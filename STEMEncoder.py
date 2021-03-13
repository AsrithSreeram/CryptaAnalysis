import random #Import Random Standard Library for Pseudo-Random Generators

#Code Encoder 3.0
print("Code Encoder 3.0\nThe longer your message is the harder it is to break. However, even short messages are strong and hard to brute force as this uses a variation of the one-time pad with pseudo-random number generators.") #Explanation on encoding details 
#Asks for message
message = str(input("Enter your message: ")) #Get Message to encoder
finished_message = [i for i in message] #Converting string into list of letters

#Changing message into number form
charactersToNums = {'j': 0, 'y': 1, 'Y': 2, 'r': 3, 's': 4, 'W': 5, 'b': 6, 't': 7, 'B': 8, ' ': 9, 'h': 10, 'i': 11, 'p': 12, 'k': 13, '.': 14, 'D': 15, 'z': 16, 'u': 17, '!': 18, 'v': 19, 'w': 20, 'V': 21, 'I': 22, 'M': 23, 'P': 24, 'E': 25, 'F': 26, 'G': 27, 'o': 28, 'Q': 29, 'n': 30, 'e': 31, 'q': 32, 'U': 33, 'T': 34, 'K': 35, 'f': 36, 'A': 37, 'd': 38, 'J': 39, 'm': 40, 'N': 41, ',': 42, 'a': 43, 'X': 44, 'Z': 45, 'R': 46, 'H': 47, 'l': 48, 'S': 49, 'C': 50, 'c': 51, 'g': 52, 'O': 53, 'L': 54, 'x': 55} #Plaintext Rotor Wheel + Dictionary for Number Conversion. ASCII couldn't be used because of punctuation in cipher wheel
message_numbers = [charactersToNums[i] for i in finished_message] #List for storing message as numbers
alpha_chr_len = len(message_numbers) #Defining number of characters that need to be encoded

#Cipher Alphabet Creation within array
alphabet1 = ['r', 'R', 'y', 'm', 'Z', 'K', 'X', 'V', 'n', 'h', 'q', 'f', '.', 'd', 'c', 'z', 'u', 'P', 'I', 'v', 'T', 'o', 'W', ',', 'N', 'g', 'Y', ' ', 'j', 't', 'H', 'C', 'a', 'e', 'B', 'Q', 'x', 'b', 'i', 'w', 'U', 'G', 'p', 'S', 's', 'L', 'A', 'l', 'k', 'M', '!', 'J', 'F', 'D', 'E', 'O'] #Define cipher alphabet as list
alphabet_chosen = [charactersToNums[i] for i in alphabet1] #List to store cipher alphabet as numbers

#Asks for Starting Letter and stores value
starting_letter = 42 #Setting starting letter as guide to line up rotors
myStr = input("Enter encoding keyword: ").lower() #Ask for keyword for encoding

#Make keyword transformed into seed number
rngKey = "" #Setting string to store Random Number Generator seed
for i in myStr: #Iterating through keyword
  rngKey += str(ord(i)) #Appending keyword letters into numbers through ASCII protocol

#PsuedoRNG Generation: Uses seed number to replicate same generation across devices
keys = [] #Empty array to store random keys for encoding
random.seed(rngKey) #Setting generated seed to start common random generation scheme over encoding and decoding
for nums in range(alpha_chr_len): #Iterate through the length of message to get independent keys for each message
    random_int = int(random.randint(0, 55)) #Generate random key between 0 to 25 to represent letters
    keys.append(random_int) #Add key to key list

#Encoding Process Starts
encoded_num_list = [] #List for storing encoded numbers
index = 0 #Set Index Variable
for letters in message_numbers:
    start_position = starting_letter #Align rotors with starting letter
    end_position = letters #Find position letter in plaintext on original rotor
    shift_index = int(int(end_position) - int(start_position)) #Find how "far" the letter is from the starting letter
    key_value = keys[index] #Find corresponding key for letter from RNG list
    key_index = alphabet_chosen.index(key_value) #Find location of the corresponding key on cipher alphabet wheel
    encoded_num_index = (int(int(key_index) + shift_index)) % 55 #Find the corresponding cipher rotor index for letter in plaintext letter
    encoded_num = alphabet_chosen[encoded_num_index] #Find actual corresponding cipher letter based on cipher rotor index 
    encoded_num_list.append(encoded_num) #Add to final encoded number list
    index += 1 #Increment index to get new corresponding key
#Encoding Process Ends
#Making encoded message back to letters
encoded_message = "_" #String for storing final encoded letters. _ is put for human purposes
numsToCharacters = {charactersToNums[i]: i for i in charactersToNums} #Inverting dictionary pairs from charactersToNums
for i in encoded_num_list: #Iterate through indexes of encoded number list
    encoded_message += numsToCharacters[i] #Add characters to final encrypted message
        
#Final Display
print("Your encoded message is:", encoded_message+"_") #Displays final encoded message
print(f"Keyword: {myStr}") #Keyword needed to decrypt
print("If you give the program any incorrect info of how to decode, the message will be meaningless.") #Printing warning statement if entered incorrect info
