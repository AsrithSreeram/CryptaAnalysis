from Decrypters import substitution_decrypt, caesar_decrypt
from Cryptanalysis import frequencyAnalysis
from constants import possibleMessageWords

def hackSubstitution(encryptedMessage):
  #NOTE: May need to fix decrypter for uppercasing
  cipherMessage = encryptedMessage.lower() #Lowercase encrypted message
  possibleWords = possibleMessageWords() #Get all possible words in message
  likelyPunctuation = ['.', ',', '!', cipherMessage[-1]] #All punctuation including the last character of the message as the message uses proper grammar
  #This splits message by spaces. LOGIC MAY HAVE TO BE CHANGED LATER either manually or through a Frequency Analysis approach
  encryptedWords = "".join([i for i in cipherMessage if i not in likelyPunctuation]).split(" ") #Create a list of words without any punctuation
  alphabetTransformation = {i.lower(): [] for i in cipherMessage if i.isalpha()} #Get a dictionary of every unique character
  for i in likelyPunctuation: #Iterate through every punctuation
    alphabetTransformation[i] = ['/'] #/ represents punctuation. This is adding this key in alphabetTransformation.
  solutionFound = {i: False for i in alphabetTransformation}
  #while False in solutionFound.values():
  for cipherLetter in alphabetTransformation: #Iterate every letter in ciphertext
    #Find all words that use cipherLetter
    distinctCipherWordsWithLetter = {i: [] for i in encryptedWords if cipherLetter in i}
    #Check guesses for letter from 'a' to 'z'
    for guessPlaintextLetter in [chr(i) for i in range(ord('a'), ord('z')+1)]:
      #Find cipher words and see if alphabet matches
      solutionWorks = True
      for distinctCipherWord in distinctCipherWordsWithLetter: #Iterate through every distinct cipher word
        indexFoundInCipherWord = distinctCipherWord.index(cipherLetter) #Find where in the word the character is located
        possibleWordMatches = [i for i in possibleWords if len(i) == len(distinctCipherWord)] #Check which words are of the same length as the original word
        possibleWordMatches = [i for i in possibleWordMatches if i[indexFoundInCipherWord].lower() == guessPlaintextLetter.lower()] #Check which possible word matches with the same index of the character matches guess 
        solutionWorks = not len(possibleWordMatches) == 0 #If a solution was not found
      if solutionWorks: #If solution was found.
        alphabetTransformation[cipherLetter].append(guessPlaintextLetter) #Add guess letter to list
      solutionFound[cipherLetter] = len(alphabetTransformation[cipherLetter]) == 1       #If only one solution was found.

  #Cut down on repeated solutions 
  while True: #Iterate forever until manually exited
    changed = False #Initializing changed variable
    securedLetters = [alphabetTransformation[i][0] for i in alphabetTransformation if solutionFound[i]] #Get transformations that have only one possible letter 
    for cipherLetter in alphabetTransformation: #Iterate through all transformations
      if solutionFound[cipherLetter]: #If letter only has one solution
        continue #Skip this loop
      possibleTransformations = alphabetTransformation[cipherLetter] #Find all possible guesses
      for finishedLetter in securedLetters: #Iterate through every 'secured' letter
        if finishedLetter in possibleTransformations: #If the letter is in the possible guess
          #Remove this solution as it has already been used and set changed to True
          possibleTransformations.remove(finishedLetter)
          changed = True
      if len(alphabetTransformation[cipherLetter]) == 1: #A unsecured letter has eliminated all solutions except for 1. 
        #Validate that this solution is solved.
        solutionFound[cipherLetter] = True
    if not changed: #If nothing changed
      break #Break out of loop
  finalAlphabet = {i: alphabetTransformation[i][0] for i in alphabetTransformation if len(alphabetTransformation[i]) > 0} #Create alphabetTransformation. NOTE: This may be one permutation of the possible alphabet transformations. This logic may have to be improved.
  return substitution_decrypt(cipherMessage, finalAlphabet) #Return decrypted message using alphabetTransformation

def hackCaesar(encryptedMessage):
  tupleList = frequencyAnalysis(encryptedMessage) #using frequency analysis 
  solution = 0 #defined value initially
  solutions = [] #empty array to hold solutions
  for (_, key) in tupleList: #iterating through tupleList
    if(solution >= 1): #more than one solution found
      break #break 
    solution += 1 #increment solution by 1
    shift = ord(key)-ord('e') #check key from value of e
    solutions.append(caesar_decrypt(encryptedMessage, shift)) #append solutions to caeaser_decrypt results
    solutions.append(caesar_decrypt(encryptedMessage, shift, ignorePunctuationAndSpaces = True)) #append solutions to caeaser_decrypt results and make sure punctuations and spaces count
  return solutions #return values of solutions in array