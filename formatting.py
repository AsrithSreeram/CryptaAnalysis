from constants import possibleMessageWords


def capitalizeMessage(msg):
  #Find words that are capitalized in possible message words
  capitalizedMessageWords = [i for i in possibleMessageWords() if True in [True for j in i if j.isupper()]]
  #Replace words that are usually capitalized 
  for i in capitalizedMessageWords:
    if i.lower() in msg:
      msg = msg.replace(i.lower(), i)
  #Find Words right after periods
  wordsSplitByPeriods = msg.split('. ')
  #Capitalize these words and then replace in original string
  for i in wordsSplitByPeriods:
    msg = msg.replace(i, i.capitalize())
  return msg

def levenshtein_distance(string1, string2):
  #Implementation of a minimum edit distance algorithm. Varaint to only include substitutions 
  if len(string1) == len(string2): #Check if there is any way these strings can be converted to each other through substitutions by checking lengths
    #Set score
    score = 0
    #Compare all strings
    for i in range(len(string1)):
      if string1[i] != string2[i]:
        if string1[i] in [',', '.', '!'] or string1[i] in [',', '.', '!']: #Check if punctuation. Punctuation based words are prefered. 
          score += 1.5 #Lower Score
        else: 
          score += 1 #Higher Score
    return score #Return Score
  else:
    return None #Return None as there is no way these strings can be converted to each other through substitutions

def generateClosestMessage(msg):
  #Split message by spaces
  words = list({ "".join([j for j in i if j.isalpha()]): None for i in msg.split(' ') }.keys())
  #Variables to limit searches
  constraintLevel = 0.7 
  acceptedLevel = 0
  #Optimization: Check if analysis is worthwhile for given message
  if len(words) >= 25:
    possibleWords = possibleMessageWords() #Get list of possible words
    newWords = [] #New Word Possibilities List
    for messageWord in words: #Iterate through every word in message
      minimumValue = None #Varaible for storing all possible words
      minimumEditWord = None #Variable for storing minimum levenshtein distance
      for possibleWord in possibleWords: #Iterate through every possible word in message
        distance = levenshtein_distance(messageWord.lower(), possibleWord.lower()) #Get levenshtein distance of the two words
        if distance != None: #Checks that the words could be transformed through substitutions 
          if distance <= round(len(messageWord)*constraintLevel): #Checks that the lowest limit
            if minimumValue == None: #Check if any word has been found that matches criterion.
              #Setting new distance and creating new list for word
              minimumValue = distance 
              minimumEditWord = [(possibleWord, distance)]
            else:
              #Setting new distance and appending word to list
              minimumValue = min(distance, minimumValue)
              minimumEditWord.append((possibleWord, distance))
        if len(messageWord) > 2: #Length threshold to limit searches of punctuation
          distance = levenshtein_distance(messageWord.lower(), possibleWord.lower()+'/') #Get distance of the possible word with punctuation
          if distance != None: #Checks that the words could be transformed through substitutions 
            if distance <= round(len(messageWord)*constraintLevel): #Checks that the lowest limit
              if minimumValue == None: #Check if any word has been found that matches criterion.
                #Setting new distance and creating new list for word
                minimumValue = distance
                minimumEditWord = [(possibleWord + '/', distance)]
              else:
                #Setting new distance and appending word to list
                minimumValue = min(distance, minimumValue)
                minimumEditWord.append((possibleWord + '/', distance))
      #Get only the best solutions based on accepted level
      minimumEditWord = [i[0] for i in minimumEditWord if i[1] <= minimumValue + acceptedLevel]
      newWords.append(minimumEditWord)
    #Initialize newMessages
    newMessages = ['']
    #Make a new dictionary of generated words
    dictionaryOfWords = {words[i]: newWords[i] for i in range(len(words))}
    #Replace new words and permutate results 
    #Initialize word parsing variables
    currentWord = ''
    currentPunctuation = ''
    newList = []
    for i in msg: #Iterate through characters in message
      if i == ' ': #Check if character is space. If so, this is the end of the old and beginning of a new word
        #Add new word
        if currentWord != '': #If the old word is indeed a word
          for message in newMessages: #Iterate through every possible existing 'layer' of messages
            for possiblePlaintext in dictionaryOfWords[currentWord]: #Iterate through all possible generated word guesses
              newList.append(message + possiblePlaintext + currentPunctuation + ' ') #Create new message
          #Reset all variables to initial
          newMessages = newList
          currentWord = ''
          currentPunctuation = ''
          newList = []
      elif i == '/': #Some sort of punctuation
        currentPunctuation += i #Add to punctuation string
      else: #Some other character in a word
        currentWord += i #Add to current word string
    #Add last word to list.
    for message in newMessages: #Iterate through every possible existing 'layer' of messages
      for possiblePlaintext in dictionaryOfWords[currentWord]: #Iterate through all possible generated word guesses
        newList.append(message + possiblePlaintext + currentPunctuation) #Create new message
    newMessages = newList #Assigning newList to newMessages 
    #print(newMessages)
    return newMessages #Return message possiblities
  else:
    return [msg] #Return old message in a list as it wasn't worth the effort
