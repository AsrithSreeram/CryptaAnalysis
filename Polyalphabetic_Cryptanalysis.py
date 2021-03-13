from matplotlib import pyplot as plt 
from Kasiski_test import kasiski_test
from IC_Test import ICTest

def findKeyLength(encrypted_message):
  kasiski_results = kasiski_test(encrypted_message) #using kasiski test results
  x = kasiski_results[0] #length of kasiski results is assigned to x
  answersList = kasiski_results[1] #score of kasiski results is assigned to answersList
  #Toggle weighting as necessary
  weighted = 1500
  for index in range(len(x)): #loop through range of x
    answersList[index] += weighted * ICTest(encrypted_message, x[index]) #weight of score * value of IC test is incremented into answersList
  dictionary = {x[i]: answersList[i] for i in range(len(x))} #dictionary is checked and iterated through range of x
  def sortByScore(e):
    return dictionary[e] #returning dictionary
  x.sort(key = sortByScore, reverse = True)   #sorting by score
  return x #returning in sorted form