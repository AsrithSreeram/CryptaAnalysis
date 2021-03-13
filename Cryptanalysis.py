from langdetect import detect_langs
def calcIC(cipher_text):
  import collections
  #Calculate the Index of Coincidence of a piece of text. Allows for identification of a cipher encryption method.
  # Removing all non alpha and whitespace and uppercasing
  cipher_flat = "".join([x.upper() for x in cipher_text.split() if  x.isalpha()])
  # Setting up variables
  N = len(cipher_flat)
  freqs = collections.Counter( cipher_flat )
  alphabet =  map(chr, range( ord('A'), ord('Z')+1))
  freqsum = 0.0
  # Calculations
  for letter in alphabet:
      freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )
  IC = freqsum / ( N*(N-1) )
  return IC

def sortByEnglishMatch(e):
  prob = 0
  try:
    for i in detect_langs(e):
      if str(i)[0:2] == 'en':
        prob = float(str(i)[3:])
    if ' ' not in e:
      prob -= 0.2
  except:
    print(f"EXCEPTION: {e}") #Throw exception
  return prob

def frequencyAnalysis(encryptedMessage):
  allCharacters = {}
  for i in encryptedMessage:
    if i in allCharacters:
      allCharacters[i] += 1
    else:
      allCharacters[i] = 1

  tupleList = [(allCharacters[key], key) for key in allCharacters]
  def mySort(e):
    return e[0]
  tupleList.sort(key=mySort, reverse=True)
  return tupleList
