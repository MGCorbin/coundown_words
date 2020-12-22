#!/usr/bin/python

##################################################
## Simple program to solve a countdown conundrum
##################################################
## 
##################################################
## Author: Marcus Corbin
## Copyright: Copyright 2020, countdown words
## Credits: [Ryan Flanagan]
## Email: corbin.mgc@gmail.com
##################################################

wordFile = open('trimmedWords.txt', 'r')    # found at https://gist.github.com/Ranagan/e8b77027d8b96cb68725a4169d8cfc3a
matches = []
bestWords = []

def matchWord(word1, word2):                # heavily inspired by Ryan's coundown solver
    isMatch = False

    for letter in word1:

        if letter in word2:
            word2.remove(letter)
        elif len(word2) == 0:
            isMatch = True
        else:
            isMatch = False

    return isMatch

def sort(lst):                              # sort a list from shortest to longest
    lst2 =  sorted(lst, key=len)
    return lst2


def solve(ipt):
    longestWord = ""

    for word in wordFile:                   # loop through every word in the file
        word = word.rstrip()

        if(matchWord(ipt, list(word))) == True:
            # if we find a match, add it to the list of matches
            matches.append(word)
            if len(longestWord) < len(word):   
                #keep track of the longest word
                longestWord = word

    return longestWord


ipt = input("Enter anagram:")                           # let the user enter the input

bestWord = solve(ipt)                                   # find the best word (longest)

for match in matches:                                   # find all other other words with that length
    if len(match) == len(bestWord):
        bestWords.append(match)

print("List of matches:")
print('\n'.join(sort(matches)))
print("--------")
print("Total of", len(matches), "words")
print ("Best word(s):", bestWords, "(" + str(len(bestWord)) + ")")
print("--------")
