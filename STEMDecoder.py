import random #Import Random Standard Library for Pseudo-Random Generators
from langdetect import detect_langs
from langdetect import DetectorFactory
DetectorFactory.seed = 10 #Makes the deterministic instead of nondeterministic nature of langdetect langdetect

#Code Decoder
#Asks for message
message = str(input("Enter your encoded message: ")) #Get Message to encoder
finished_message = [i for i in message] #Converting string into list of letters

#Changing message into number form
charactersToNums = {'j': 0, 'y': 1, 'Y': 2, 'r': 3, 's': 4, 'W': 5, 'b': 6, 't': 7, 'B': 8, ' ': 9, 'h': 10, 'i': 11, 'p': 12, 'k': 13, '.': 14, 'D': 15, 'z': 16, 'u': 17, '!': 18, 'v': 19, 'w': 20, 'V': 21, 'I': 22, 'M': 23, 'P': 24, 'E': 25, 'F': 26, 'G': 27, 'o': 28, 'Q': 29, 'n': 30, 'e': 31, 'q': 32, 'U': 33, 'T': 34, 'K': 35, 'f': 36, 'A': 37, 'd': 38, 'J': 39, 'm': 40, 'N': 41, ',': 42, 'a': 43, 'X': 44, 'Z': 45, 'R': 46, 'H': 47, 'l': 48, 'S': 49, 'C': 50, 'c': 51, 'g': 52, 'O': 53, 'L': 54, 'x': 55} #Plaintext Rotor Wheel + Dictionary for Number Conversion. ASCII couldn't be used because of punctuation in cipher wheel
message_numbers = [charactersToNums[i] for i in finished_message] #List for storing message as numbers
alpha_chr_len = len(message_numbers) #Defining number of characters that need to be decoded

#Cipher Alphabet Creation within array
alphabet1 = ['r', 'R', 'y', 'm', 'Z', 'K', 'X', 'V', 'n', 'h', 'q', 'f', '.', 'd', 'c', 'z', 'u', 'P', 'I', 'v', 'T', 'o', 'W', ',', 'N', 'g', 'Y', ' ', 'j', 't', 'H', 'C', 'a', 'e', 'B', 'Q', 'x', 'b', 'i', 'w', 'U', 'G', 'p', 'S', 's', 'L', 'A', 'l', 'k', 'M', '!', 'J', 'F', 'D', 'E', 'O'] #Define cipher alphabet as list
alphabet_chosen = [charactersToNums[i] for i in alphabet1] #List to store cipher alphabet as numbers

myStr = input("Enter keyword used in encoding: ").lower() #Ask for keyword used for encoding
#Make keyword transformed into seed number
rngKey = "" #Setting string to store Random Number Generator seed
for i in myStr: #Iterating through keyword
  rngKey += str(ord(i)) #Appending keyword letters into numbers through ASCII protocol
  
#PsuedoRNG Generation: Uses seed number to replicate same generation across devices
keys = [] #Empty array to store random keys for encoding
random.seed(rngKey) #Setting generated seed to start common random generation scheme over encoding and decoding
for nums in range(alpha_chr_len): #Iterate through the length of message to get independent keys for each message
    random_int = int(random.randint(0, 55)) #Generate random key between 0 to 55 to represent letters
    keys.append(random_int) #Add key to key list
#Asks for Starting Letter and stores value
solutions = []
for starting_letter in range(len(alphabet1)): #Looping through all possibilities of starting cipher alphabet to find which one was used in encoding program
  #Decoding Process Starts
  decoded_num_list = [] #List for storing encoded numbers
  index = 0 #Set Index Variable
  for letters in message_numbers:
      start_position = alphabet_chosen.index(keys[index]) #Align rotors with starting letter
      end_position = int(alphabet_chosen.index(letters)) #Find position letter in plaintext on original rotor
      shift_index = int(int(end_position) - int(start_position)) #Find how "far" the letter is from the starting letter
      decoded_num_index = int(int(starting_letter) + int(shift_index)) % 55 #Find the corresponding plaintext rotor index for letter in ciphertext letter
      decoded_num_list.append(decoded_num_index) #Add to final decode number list
      index += 1 #Increment index to get new corresponding key
  #Decode Process Ends
  #Making decoded message back to letters
  decoded_message = "_" #String for storing final decoded letters. _ is put for human purposes
  numsToCharacters = {charactersToNums[i]: i for i in charactersToNums} #Inverting dictionary pairs from charactersToNums
  for i in decoded_num_list: #Iterate through indexes of decoded number list
      decoded_message += numsToCharacters[i] #Add characters to final encrypted message
  solutions.append(decoded_message) #Add to solution list

def sortByEnglishMatch(e): #Function for grading 'englishness' of a message
  prob = 0 #Probability score
  try: #Try clause as exception may be thrown
    for i in detect_langs(e): #Iterate through all detected languages
      if str(i)[0:2] == 'en': #If english in these languages
        prob = float(str(i)[3:]) #Make probability equal to calculated probability percentage
    if ' ' not in e: #Check if message contains spaces
      prob -= 0.2 #Take off points for messages with no spaces
  except: #In the case an exception is thrown
    print(f"EXCEPTION: {e}") #Throw exception
  return prob #Return probability

solutions.sort(key = sortByEnglishMatch, reverse = True) #going to sort by englishMatch method return values in greatest to least
#Final Display
print("\nTop 3 solutions: ") 
for i in range(3):
  print(f'{i+1}. _{solutions[i]}_\n') #Displays top 3  decoded message in relation to English language
