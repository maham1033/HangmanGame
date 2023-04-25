# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 04:52:23 2022

@author: dell
"""

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    This function will load words from file name stored in 
    WORDLIST_FILENAME (variable)
    
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist




def choose_word(wordlist):
    """
    For choosing random word from any list
    """
    return random.choice(wordlist)
    
wordlist = load_words()

def match_with_gaps(my_word,other_word):
    """
    This Funcion will basically Match my_word (which can be in a 
                                               format like a _ p p _ e ) 
    with other_word and will return True if they are matched otherwise returns
    False 
    
    In this program this fuction is used by function 
    show_possible_matches
    
    """

    if my_word==None:
        return False
    my_word = my_word.replace(" ","")
    k = 0
    v = 0
    if len(my_word)== len(other_word):
        for i in my_word:
            if i == "_":
                k+=1
                continue
            elif other_word[k]==i:
                v=1
            else:
                v=0
                break
    if v==1:
        return True
    else:
        return False

def show_possible_matches(my_word):
    """
    This Function will print words matching with my_word from 
    wordlist(global scope) and is using match_with_gaps function
    for verification
    
    """
    L=[]
    for i in wordlist:
        if match_with_gaps(my_word,i) == True:
            L.append(i)
    if len(L)==0:
        print("No Matches Found")
    else:
        print("Possible word matches are:")
        for i in L:
            print(i,end=" ")
    print()		

def is_word_guessed(secret_word, guess_list):
    """
    This will return True if the all letters of secret_word are 
    present in guess_list
    """
    if secret_word=="":
        return True
    elif secret_word[0] in guess_list:
        return is_word_guessed(secret_word[1:],guess_list)
    else:
        return False

def get_guessed_word(secret_word, guess_list):
    """
    This will return string consisting of underscores, letters and 
    gaps(for ease in understanding) by comparing guess_list with secre_word
    """
    if len(guess_list)==0:
        return ("_ "*len(secret_word))
    y= ""
    for i in secret_word:
        if i in guess_list:
            y= y+str(i)+" "
        else:
            y=y +"_ "
    return y
	
def get_available_letters(guess_list):
    """
    This will return string of alphabets 
    excluding alphabets present in guess_list
    """
    y = string.ascii_lowercase #will return string of all alphabets a-z
    z= ""
    for i in y:
        if i in guess_list:
            continue
        else:
            z= z +str(i)
        
    return z
			

def hangman(secret_word):
    
    print(secret_word)
    alphabet_string = string.ascii_lowercase
    unique_letters = len(set(secret_word)) #number of unique letters in secret_word and it will be used for computing score
    guess_list = []
    guesses = 6 
    warnings = 3
    print("Welcome to the game Hangman! \nI am thinking of a word that is",
         len(secret_word),"letters long.","\nYou have", warnings,
         "warnings left.\n---------------------------------------------")
    print("You have",guesses,"guesses left.")
    print("Available letters : ",get_available_letters(guess_list),end="") 
    while guesses!= 0:
        enter = input("Enter Your Guess:")
        if enter not in alphabet_string: #input not in alphabet
            if warnings !=0:
                warnings-=1  #warning will be decremented by 1 if warnings>0
                print("Oops! That is not valid letter. You have"
                      ,warnings,"warning(s) left: \n"
                      ,get_guessed_word(secret_word, guess_list))
            else:
                guesses -=1 #if warnings == 0 guesses will be decremented 
                print("Oops! That is not valid letter."
                      ," You have no warnings left so you lose one guess:"
                      ,get_guessed_word(secret_word, guess_list))
        elif enter in guess_list: #if user input same letter again (already guessed)
            if warnings !=0:
                warnings-=1
                print("you've already guessed this letter"
                      ,warnings,"warnings left: \n"
                      ,get_guessed_word(secret_word, guess_list))
            else:
                guesses-=1
                print("you've already guessed that letter,"
                      ," You have no warnings left so you lose one guess:"
                      ,get_guessed_word(secret_word, guess_list))
                
        elif enter not in secret_word: #if user input is letter and is not in secret word
            if enter not in guess_list:
                if enter in "aeiou": #if wrong guess is from vowels, 2 guesses will be subtracted
                    print("Oops! The letter is not in my word:",get_guessed_word(secret_word, guess_list))
                    guesses -=2
                else: #if wrong guess is from consonants, 1 guess will be subtracted
                    print("Oops! The letter is not in my word:",get_guessed_word(secret_word, guess_list))
                    guesses -=1
                guess_list.append(enter) #because guess is letter and is not in guess list so we need to add it in guess list
            
        elif enter in secret_word:
    
            guess_list.append(enter) #adding in guess list
            print("Good Guess :",get_guessed_word(secret_word, guess_list))

            if is_word_guessed(secret_word,guess_list)== True:
            	print("\n-----------------\nCongratulations, You Won!"
                   ,"\nYour total score for this game is:"
                   ,guesses*unique_letters)
            	break
        
        get_guessed_word(secret_word,guess_list)
        if guesses == 0:
            print("---------------------------------------------\nSorry, You ran out of guesses. The word was"
                  , secret_word)
            break
        print("---------------------------------------------")
        print("Remaining Letters : ",get_available_letters(guess_list))
        print("Remaining Guesses :  ",guesses,end="")


def hangman_with_hints(secret_word):   
   print(secret_word)
   check = string.ascii_lowercase
   unique_letters = len(set(secret_word))
   guess_list = []
   guesses = 6
   warnings = 3
   print("Welcome to the game Hangman! \nI am thinking of a word that is",
        len(secret_word),"letters long.","\nYou have", warnings,
        "warnings left.\n---------------------------------------------")
   print("You have",guesses,"guesses left.")
   print("Available letters : ",get_available_letters(guess_list),end="") 
   while guesses!= 0:
       enter = input("Enter Your Guess:")
       if enter  =="*":
           show_possible_matches(get_guessed_word(secret_word, guess_list))
       elif enter not in check:
           if warnings !=0:
               warnings-=1
               print("Oops! That is not a valid letter. You have", warnings,"warnings left:",get_guessed_word(secret_word, guess_list))
           else:
               guesses -=1
               print("Oops! That is not a valid letter. You have 0 warnings left so you lose one guess:",get_guessed_word(secret_word, guess_list))

       elif enter in guess_list:
           if warnings !=0:
               warnings-=1
               print("you've already guessed this letter"
                     ,warnings,"warnings left: \n"
                     ,get_guessed_word(secret_word, guess_list))
           else:
               guesses-=1
               print("you've already guessed that letter, You have no warnings left so you lose one guess:",get_guessed_word(secret_word, guess_list))
               
       elif enter not in secret_word:
           if enter not in guess_list:
               if enter in "aeiou":
                   print("Oops! The letter is not in my word",get_guessed_word(secret_word, guess_list))
                   guesses -=2
               else:
                   print("Oops! The letter is not in my word",get_guessed_word(secret_word, guess_list))
                   guesses -=1
               guess_list.append(enter)
           else:
               if enter in "aeiou":
                   print("Only Letter from Available Letters are allowed")
                   guesses -=2
               else:
                   print("Only Letter from Available Letters are allowed")
                   guesses -=1
           
       elif enter in secret_word:
       
           guess_list.append(enter)
           print("Good Guess :",get_guessed_word(secret_word, guess_list))
   

           
           if is_word_guessed(secret_word,guess_list)== True:
           	print("\n-----------------\nCongratulations, You Won!"
                  ,"\nYour total score for this game is:"
                  ,guesses*unique_letters)
           	break
       get_guessed_word(secret_word,guess_list)
       if guesses == 0:
           print("-------------------\nSorry, You ran out of guesses. The word was"
                 , secret_word)
           break
       print("---------------------------------------------")
       print("Remaining Letters : ",get_available_letters(guess_list))
       print("Remaining Guesses :  ",guesses,end="")




if __name__ == "__main__":
 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)






    
