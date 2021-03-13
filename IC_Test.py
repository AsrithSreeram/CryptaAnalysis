from Cryptanalysis import calcIC
from matplotlib import pyplot as plt
"""
#Getting Input
encrypted_message = input("Enter Encrypted Message: ")
#Message without spaces
encrypted_message=encrypted_message.replace(' ',"")
#Make divisions based on length of message
"""
def ICTest(cipher_text, keyLength): # 2 parameters for ICTest passed
  shift_texts  = ["" for i in range(keyLength)] #checking for shifts within the keyLength param
  for index in range(len(cipher_text)): #when index is in the length of the cipher_text
    shift_texts[index % keyLength] += cipher_text[index]
  average = 0 #default value of average to start off with
  for text in shift_texts: #when text is in shift_texts
    average += calcIC(text) #increment average by the calc IC text
  average /= len(shift_texts) #divide average by the length of shift texts
  return average #returning value so it can be used in main file

"""
x = [i+1 for i in range(40)]
icResults = [ICTest(encrypted_message, i) for i in x]
plt.plot(x, icResults)
plt.show()
"""