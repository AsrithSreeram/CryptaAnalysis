import math

def substitution_decrypt(encryptedMessage, alphabet): 
  decryptedMessage = "" #empty message defined
  for i in encryptedMessage: #looping through parameter
    if i in alphabet: #checking if alphabet exists
      decryptedMessage += alphabet[i] #incrementing value of decrypted message to alphabet array
    else:
      decryptedMessage += i #incrementing value of decrypted message to i values in encryptedMessage
  return decryptedMessage #return value of decoded


def transposition_decrypt(key, message):
  numOfColumns = int(math.ceil(len(message) / float(key))) #number of columns are defined by the math function of length of message / key length 
  numOfRows = key # number of rows are defined by key length

  numOfShadedBoxes = (numOfColumns * numOfRows) - len(message) #number of shaded boxes are defined by multiplying columns and rows and then subtracting by length of message. This makes sure that the shadedBoxes are the ones without any message inside them (will not be counted)

  plaintext = [''] * numOfColumns #empty initial array multiplied by numberOfColumns will give value of plainText
  column = 0 #initialize value
  row = 0  #initialize value

  for symbol in message:
    plaintext[column] += symbol #incrementing plainText and makes sure it equals symbol
    column += 1 #increment column value
    if (column == numOfColumns) or (column == numOfColumns - 1 and
      row >= numOfRows - numOfShadedBoxes): #when column equals numOfColumns defined but row is > numberOfRows - additional boxes (shaded)
      column = 0 #stops incrementing and goes back to 0
      row += 1 #increment row value

    return ''.join(plaintext) #takes all items in plaintext iterable and joins them into one string
  
def caesar_decrypt(message, shift, ignorePunctuationAndSpaces = False):
  finalMessage = "" #empty message defined
  puncuationsAndSpaces = [' ', '.', ',', '!'] #used to add punctuations and spaces into the alphabet dictionary for decrypting
  for i in message: #loops through message
    if ignorePunctuationAndSpaces and i in  puncuationsAndSpaces: #when true and i exists
      finalMessage += i #increment finalMessage i times
      continue #next iteration of loop
    currentChar = ord(i)-ord('a') #checking char value from first letter of alphabet
    shiftedChar = (currentChar - shift) % 26 #checking shift from calculated char and modulus of 26
    finalMessage += chr(shiftedChar+ord('a')) #final message is incremented based on the shift from first letter of alphabet
  return finalMessage #return message