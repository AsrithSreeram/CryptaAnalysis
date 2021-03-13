import math
from langdetect import detect_langs #import libraries

def sortByEnglishMatch(e): #checks the message relation with English
  prob = 0
  for i in detect_langs(e):
    if str(i)[0:2] == 'en':
      prob = float(str(i)[3:])
  if ' ' not in e:
    prob -= 0.2
  return prob

def main(): #this is the method that will be run

    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr.""" #enter message that you want to decode (transposition cipher encoded message)

    hackedMessage = hackTransposition(myMessage) #calling hackTransposition method on our encoded message

    if hackedMessage == None : 
         print('Failed to hack encryption.')
    else:
        print('Message is decrypted :')
        hackedMessage.sort(key = sortByEnglishMatch, reverse = True) #sorting hackedMessage so the key uses the probability of the sortByEnglishMatch method and reverse is true
        print("\n\n\n\n\n")
        for i in range(5): #for i in 0,1,2,3,4 - want 5 possibilities of decoded message
          print(str((i+1))+". ", hackedMessage[i]+'\n') # print 5 times the hackedMessage (i increments after each print) 
  
def decryptMessage(key, message): #decryptMessage method that will be used in hacking method
  #transposition cipher uses columns and rows for its cipher
    numOfColumns = int(math.ceil(len(message) / float(key))) #number of columns are defined by the math function of length of message / key length 
    numOfRows = key # number of rows are defined by key length

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message) #number of shaded boxes are defined by multiplying columns and rows and then subtracting by length of message. This makes sure that the shadedBoxes are the ones without any message inside them (will not be counted)

    plaintext = [''] * numOfColumns #empty initial array multiplied by numberOfColumns will give value of plainText
    column = 0 #initialize value
    row = 0  #initialize value

    for symbol in message :
        plaintext[column] += symbol #incrementing plainText and makes sure it equals symbol
        column += 1 #increment column value
        if (column == numOfColumns) or (column == numOfColumns - 1 and
            row >= numOfRows - numOfShadedBoxes): #when column equals numOfColumns defined but row is > numberOfRows - additional boxes (shaded)
            column = 0 #stops incrementing and goes back to 0
            row += 1 #incremetn row value

    return ''.join(plaintext) #takes all items in plaintext iterable and joins them into one string

def hackTransposition(message):
  decryptedMessages = [] #will be populated
  for key in range(1, 7): #for key in these values
    decryptedText = decryptMessage(key, message) #decryptedText array is assigned to the string value returned in decryptMethod
    decryptedMessages.append(decryptedText) #appending the text into the message           
  return decryptedMessages #returning final hacked message


if __name__ == '__main__': #making sure it runs the main method
    main()




  
