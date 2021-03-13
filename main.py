from Cryptanalysis import calcIC, sortByEnglishMatch, frequencyAnalysis
from Polyalphabetic_Cryptanalysis import findKeyLength
from formatting import capitalizeMessage, generateClosestMessage
#Import Hackers
from Monoalphabetic_Cipher_Hacker import hackSubstitution
from Polyalphabetic_Cipher_Hacker import hackPolyShift

#Input Message to be hacked
encryptedMessage = input("Enter encrypted message: ")
print("Submitted")
#Find Cipher being used
ioc = calcIC(encryptedMessage)
englishIOC = 0.0667
solutions = []
if 0.053 <= ioc:
  #This is a 'simple' encryption
  #Check if substitution or transposition
  #Substitution Cipher Hacking
  substitutionResult = hackSubstitution(encryptedMessage)
  solutions.append(substitutionResult)
  solutions.append(capitalizeMessage(substitutionResult))
  generatedMessages = generateClosestMessage(substitutionResult)
  for i in generatedMessages:
    solutions.append(capitalizeMessage(i))
else:
  #Probably 'complex' encryption
  #Check Polyalphabetic Shift Cipher
  hackPolyShift(encryptedMessage)

#Sort Solutions by english match
solutions.sort(key = sortByEnglishMatch, reverse = True)

#Display
print("\n\n\n\n\n")
for i in range(100):
  print(str((i+1))+". ", solutions[i]+'\n')
