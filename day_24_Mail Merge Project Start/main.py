#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os

list_of_names = []

OUTPUT_FILE_NAME = 'letter_for_'

starting_letter_format = ''

with open('./Input/Names/invited_names.txt') as data_names:
    line = data_names.readline()
    while line:
        list_of_names.append(line.strip())
        line = data_names.readline()

with open('./Input/Letters/starting_letter.txt') as starting_letter:
    starting_letter_format = starting_letter.read().strip()


for name in list_of_names:
    file_path = os.path.join('./Output/ReadyToSend/', OUTPUT_FILE_NAME + name + '.txt')

    with open(file_path,mode='w') as data:
        data.write(starting_letter_format.replace('[name]',name))


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp