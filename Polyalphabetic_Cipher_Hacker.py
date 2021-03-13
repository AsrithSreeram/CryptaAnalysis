from Polyalphabetic_Cryptanalysis import findKeyLength
from Monoalphabetic_Cipher_Hacker import hackCaesar
import sys

def hackPolyShift(message):
  keyLengths = findKeyLength(message) #calling method to find length of message
  allMessages = [] #array defined to hold allMessages
  for i in range(3): #iterating for range of 3 times
    length = keyLengths[i] #keyLengths of i is length
    print("Length", length) #printing length
    finalMessage = [] #array defined to hold finalMessage
    for cipher in range(length): #iterating through length
      finalMessage.append(hackCaesar("".join([message[i] for i in range(0, len(message), length)]))) #appending hackCaesar value by joining all messages and iterating through message based on length
    perms = 1 #initially declared value
    for i in finalMessage: #iterating through final message
      perms *= len(i) #multiplying value of perms by length of iteration
    print(perms)
    if perms >= 10000: #warning to stop program since it is checking too many permutations
      print("WARNING: Since this program is likely to cause a MemoryError, we will stop the program now. A better of implementtaion of this will be made in the future.")
      sys.exit(0)
    #Find every message combination
    messagePossibilities = [[]] #list for message possibilities
    for shiftPossibilities in finalMessage:
      newMessagePossibilities = []
      for perm in shiftPossibilities: #iterating through shiftPossibilities
        for previousSolution in messagePossibilities: #iterating through messagePossibilities based on shift
          newList = previousSolution[:] #slicing list of previousSolution (creating new list)
          newList.append(perm) #appending new list to permutation
          newMessagePossibilities.append(newList) #appending new message possibilities to newList
      messagePossibilities = newMessagePossibilities #assigning value to each other
    print("Message Possibilities", messagePossibilities) #print statement so we know during runtime
    
    