### Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.

#Assigning the question to the variable.
Answer = input("What is the capital of France?:")
if Answer == "Paris" : #Selecting the answer of the question.
    print("The answer is correct.") # printing "The answer is correct" if the answer is given as Paris.
else:
    print("The answer is wrong.")#printing "The answer is wrong" if anything else is written other than Paris.
